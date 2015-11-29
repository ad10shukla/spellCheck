import sys
from PySide.QtCore import *
from PySide.QtGui import *
import operator
import math
import pre_final4
import find
import trienode
import freqlist  


class MainWindow(QMainWindow, pre_final4.Ui_MainWindow):
    
    def __init__(self, parent=None):            # Constructor 
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)          # SetupUi method called from class pre_final4      
        self.plainTextEdit.installEventFilter(self)         # Event filter detects key strokes
        self.cursor = self.plainTextEdit.textCursor()       # Set the cursor in plain text editor    
        self.tmp = ''
 
        # Connections corresponding to different actions. Triggered method is for mouse clicks
        self.actionExit_2.triggered.connect(self.exitApp)   
        self.actionOpen.triggered.connect(self.open)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_as.triggered.connect(self.save)
        self.actionFont.triggered.connect(self.font)
        self.actionFind.triggered.connect(self.find)
    
    def find(self):         # Method to find anything in plain text editor
        form = QDialog()
        ui_form = find.Ui_Dialog()          # Create a dialog box of find
        ui_form.setupUi(form)
        form.exec_()    

    def font(self):         # Method for font setting in the plain text editor.
        item, ok = QFontDialog.getFont()
        
        if ok is True:
            self.plainTextEdit.setFont(item)
        else:
            pass
    
    # method to exit application with no error
    def exitApp(self,): 
        sys.exit(0)

    # method to open a text document in plain text editor    
    def open(self):
        dir= "."
        fileobj = QFileDialog.getOpenFileName(self, "Open File Dialog", dir=dir)
        filename = fileobj[0]
        
        file = open(filename, "r")
        read = file.read()
        self.plainTextEdit.setPlainText(read)
        file.close()
    
    # method to save a file in text mode
    def save(self):
        dir="."
        fileobj = QFileDialog.getSaveFileName(self, "Save as", dir=dir, filter="Text files(*.txt)")
        filename = fileobj[0]
        filedata = self.plainTextEdit.toPlainText()
        open(filename, mode="w").write(filedata)          
    
    # Event filter detects key strokes. widget is the plain text editor in which key strokes will be detected. Event is a particular key detection    
    def eventFilter(self, widget, event):           

        if (event.type() == QEvent.KeyPress and widget is self.plainTextEdit):
            key = event.key()   
            
            if key == Qt.Key_F1:
                
                self.plainTextEdit.setTextCursor(self.cursor)
                self.cursor.movePosition(self.cursor.PreviousWord, self.cursor.KeepAnchor)
                self.cursor.insertHtml("<FONT color=black  >"+self.res[0][0]+"</FONT>")
                self.plainTextEdit.insertPlainText(' ')                
                return True    
            
            if key == Qt.Key_F2:
                
                self.plainTextEdit.setTextCursor(self.cursor)
                self.cursor.movePosition(self.cursor.Left, self.cursor.KeepAnchor, (self.length+1))
                self.cursor.insertHtml("<FONT color=black  >"+self.res[1][0]+"</FONT>")
                self.plainTextEdit.insertPlainText(' ') 
                return True
                
            if key == Qt.Key_F3:

                self.plainTextEdit.setTextCursor(self.cursor)
                self.cursor.movePosition(self.cursor.Left, self.cursor.KeepAnchor, (self.length+1))
                self.cursor.insertHtml("<FONT color=black  >"+self.res[2][0]+"</FONT>")
                self.plainTextEdit.insertPlainText(' ')
                return True
                
            if key == Qt.Key_Space:
    
                self.cursor.select(QTextCursor.WordUnderCursor)
                self.s2 = self.cursor.selectedText()  
                self.plainTextEdit.insertPlainText(' ') 

                if self.s2 == '':
                    pass
                    
                else:    
                    
                    self.s3 = self.s2.lower()
                    self.length = len(self.s2)
                    
                    self.plainTextEdit.setTextCursor(self.cursor)
                    self.cursor.insertHtml("<FONT color=red  >"+self.s2+' '+"</FONT>")
                   
                    self.res = self.callback(self.s3)
                    
                    for key, value in self.res:
                        print key, value    
                    print '\n'
                    
                    # opo variable is the traceback exception handler
                    opo = len(self.res)
                    if opo == 0:
                        pass
                        
                    if opo == 1:
                        self.label.setText(self.res[0][0])
        
                    if opo == 2:    
                        self.label.setText(self.res[0][0])
                        self.label_3.setText(self.res[1][0])
                        
                    if opo >= 3:   
                        self.label.setText(self.res[0][0])
                        self.label_3.setText(self.res[1][0])
                        self.label_2.setText(self.res[2][0])

                return True
  
        return QMainWindow.eventFilter(self, widget, event)
    
    '''
    First method of algorithm. Called by Callback method. Argument passed is the word inputted by user.
    Second argument is the maximum edit distance up to which words will be searched in trie.
    '''
    
    def search(self, word, maxCost):            
        currentRow = range(len(word) + 1)
        for letter in trie.children:
            self.searchRecursive(trie.children[letter], letter, word, currentRow, dict, maxCost)    
        return self.dict
    '''
    Called by search method to calculate insertion, deletion and substitution costs and then uses the minimum of all
    costs to match a word in trie.    
    '''    
    def searchRecursive(self, node, letter, word, previousRow, dict, maxCost):
        columns = len(word) + 1
        currentRow = [previousRow[0] + 1]
        for column in xrange(1, columns):
            self.insertCost = currentRow[column - 1] + 1
            self.deleteCost = previousRow[column] + 1
            if word[column - 1] != letter:
                self.replaceCost = previousRow[column - 1] + 1
            else:
                self.replaceCost = previousRow[column - 1]
            currentRow.append(min(self.insertCost, self.deleteCost, self.replaceCost))
    
        if currentRow[-1] <= maxCost and node.word != None:
            
            if float(currentRow[-1]) == 0.0:
                
                print 'Found'
                self.cursor.movePosition(self.cursor.Left, self.cursor.KeepAnchor, (self.length+1))
                self.plainTextEdit.setTextCursor(self.cursor)
                self.cursor.insertHtml("<FONT color=black  >"+self.s2+' '+"</FONT>")
    
            else:    
                '''
                Arithmetic calculations are done here to determine wMED (weighted Maximum Edit Distance). 
                Different weights are used as calculated in the training.
                '''
                wMED = 16.179/(float(currentRow[-1]))
                
                if node.word in lst:
                    freq = float(lst[lst.index(node.word)+1])
                    wMED += math.log(freq, 1.5)
                    
                if node.word[0] == self.tmp[0]:
                    wMED += 8.089  

                if node.word not in self.dict:
                    self.dict[node.word] = wMED

        if min(currentRow) <= maxCost:
            for letter in node.children:
                self.searchRecursive(node.children[letter], letter, word, currentRow, dict, maxCost)

    # Main method called by the application interface. Argument passed is the word input by the user            
    def callback(self, word_inp):
        
        self.dict = {}
        self.s2_dict = {}   
        self.tmp = word_inp
        
        self.dict = self.search(word_inp, 2)
        self.dict = sorted(self.dict.items(), key = operator.itemgetter(1), reverse=True)[:3]
        return self.dict 
    
lst = freqlist.freqlst()        # Creates an instance of freqlist class which holds the frequency of the words  
trie = trienode.TrieNode()      # Creates an instance of trienode class     
 
for word in open("dictionary.txt", 'r').read().split(): #Creates trie of the dictionary
    trie.insert(word)              
   
app = QApplication(sys.argv)
form = MainWindow()     # Creates instance of Main Window class.        
form.show()             # Show Main window
app.exec_()
