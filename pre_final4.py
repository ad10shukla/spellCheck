# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spell.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(740, 567)
        MainWindow.setMaximumSize(QtCore.QSize(1366, 630))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1366, 630))
        self.centralwidget.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:1 rgba(197, 215, 252, 255));"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 741, 491))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(1366, 630))
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setStyleSheet(_fromUtf8(""))
        self.plainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 469, 741, 24))
        self.frame.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(197, 215, 252);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 231, 24))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(244, 255, 255); font: 75 12pt 'Comic Sans MS';"))
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(250, 0, 231, 24))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(244, 255, 255); font: 75 12pt 'Comic Sans MS';"))
        self.label_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(0)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(490, 0, 241, 24))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(244, 255, 255); font: 75 12pt 'Comic Sans MS';"))
        self.label_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(0)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setStyleSheet(_fromUtf8(""))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuFormat = QtGui.QMenu(self.menubar)
        self.menuFormat.setObjectName(_fromUtf8("menuFormat"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet(_fromUtf8("background-color: rgb(230, 229, 236);"))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/New.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setVisible(True)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Save_as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon3)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionAdgcdh = QtGui.QAction(MainWindow)
        self.actionAdgcdh.setObjectName(_fromUtf8("actionAdgcdh"))
        self.actionPrint = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon4)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        self.actionExit_2 = QtGui.QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        self.actionUndo = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon5)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionCut = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Cut.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon6)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon7)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Paste.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon8)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionDelete = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon9)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionFind = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon10)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionReplace = QtGui.QAction(MainWindow)
        self.actionReplace.setObjectName(_fromUtf8("actionReplace"))
        self.actionFont = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Font.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFont.setIcon(icon11)
        self.actionFont.setObjectName(_fromUtf8("actionFont"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Information.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon12)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionRedo = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon13)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionNew_2 = QtGui.QAction(MainWindow)
        self.actionNew_2.setIcon(icon)
        self.actionNew_2.setObjectName(_fromUtf8("actionNew_2"))
        self.actionOpen_2 = QtGui.QAction(MainWindow)
        self.actionOpen_2.setIcon(icon1)
        self.actionOpen_2.setObjectName(_fromUtf8("actionOpen_2"))
        self.actionUndo_2 = QtGui.QAction(MainWindow)
        self.actionUndo_2.setIcon(icon5)
        self.actionUndo_2.setObjectName(_fromUtf8("actionUndo_2"))
        self.actionRedo_2 = QtGui.QAction(MainWindow)
        self.actionRedo_2.setIcon(icon13)
        self.actionRedo_2.setObjectName(_fromUtf8("actionRedo_2"))
        self.actionCut_2 = QtGui.QAction(MainWindow)
        self.actionCut_2.setIcon(icon6)
        self.actionCut_2.setObjectName(_fromUtf8("actionCut_2"))
        self.actionCopy_2 = QtGui.QAction(MainWindow)
        self.actionCopy_2.setIcon(icon7)
        self.actionCopy_2.setObjectName(_fromUtf8("actionCopy_2"))
        self.actionPaste_2 = QtGui.QAction(MainWindow)
        self.actionPaste_2.setIcon(icon8)
        self.actionPaste_2.setObjectName(_fromUtf8("actionPaste_2"))
        self.actionPrint_2 = QtGui.QAction(MainWindow)
        self.actionPrint_2.setIcon(icon4)
        self.actionPrint_2.setObjectName(_fromUtf8("actionPrint_2"))
        self.actionDelete_2 = QtGui.QAction(MainWindow)
        self.actionDelete_2.setIcon(icon9)
        self.actionDelete_2.setObjectName(_fromUtf8("actionDelete_2"))
        self.actionFind_2 = QtGui.QAction(MainWindow)
        self.actionFind_2.setIcon(icon10)
        self.actionFind_2.setObjectName(_fromUtf8("actionFind_2"))
        self.actionSave_2 = QtGui.QAction(MainWindow)
        self.actionSave_2.setIcon(icon2)
        self.actionSave_2.setObjectName(_fromUtf8("actionSave_2"))
        self.actionSave_as_2 = QtGui.QAction(MainWindow)
        self.actionSave_as_2.setIcon(icon3)
        self.actionSave_as_2.setObjectName(_fromUtf8("actionSave_as_2"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_2)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionReplace)
        self.menuFormat.addAction(self.actionFont)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew_2)
        self.toolBar.addAction(self.actionOpen_2)
        self.toolBar.addAction(self.actionSave_2)
        self.toolBar.addAction(self.actionSave_as_2)
        self.toolBar.addAction(self.actionPrint_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut_2)
        self.toolBar.addAction(self.actionCopy_2)
        self.toolBar.addAction(self.actionPaste_2)
        self.toolBar.addAction(self.actionDelete_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo_2)
        self.toolBar.addAction(self.actionRedo_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFind_2)
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionNew, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Spell", None))
        self.label.setText(_translate("MainWindow", "the", None))
        self.label_3.setText(_translate("MainWindow", "of", None))
        self.label_2.setText(_translate("MainWindow", "and", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuFormat.setTitle(_translate("MainWindow", "Format", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionNew.setStatusTip(_translate("MainWindow", "Open a New File...", None))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionOpen.setText(_translate("MainWindow", "Open...", None))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open an Existing File...", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save this File", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save As...", None))
        self.actionSave_as.setStatusTip(_translate("MainWindow", "Save this File As... ", None))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Alt+S", None))
        self.actionAdgcdh.setText(_translate("MainWindow", "adgcdh", None))
        self.actionPrint.setText(_translate("MainWindow", "Print...", None))
        self.actionPrint.setStatusTip(_translate("MainWindow", "Print this File", None))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.actionExit_2.setText(_translate("MainWindow", "Exit", None))
        self.actionExit_2.setStatusTip(_translate("MainWindow", "Exit Application", None))
        self.actionExit_2.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionUndo.setStatusTip(_translate("MainWindow", "Undo ", None))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z", None))
        self.actionCut.setText(_translate("MainWindow", "Cut", None))
        self.actionCut.setStatusTip(_translate("MainWindow", "Cut", None))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy", None))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste", None))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionDelete.setStatusTip(_translate("MainWindow", "Delete", None))
        self.actionDelete.setShortcut(_translate("MainWindow", "Del", None))
        self.actionFind.setText(_translate("MainWindow", "Find...", None))
        self.actionFind.setStatusTip(_translate("MainWindow", "Find What...", None))
        self.actionFind.setShortcut(_translate("MainWindow", "Ctrl+F", None))
        self.actionReplace.setText(_translate("MainWindow", "Replace...", None))
        self.actionReplace.setStatusTip(_translate("MainWindow", "Replace With...", None))
        self.actionReplace.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionFont.setText(_translate("MainWindow", "Font", None))
        self.actionFont.setStatusTip(_translate("MainWindow", "Select Font...", None))
        self.actionFont.setShortcut(_translate("MainWindow", "Ctrl+Shift+A", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionRedo.setText(_translate("MainWindow", "Redo", None))
        self.actionRedo.setStatusTip(_translate("MainWindow", "Redo", None))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y", None))
        self.actionNew_2.setText(_translate("MainWindow", "New", None))
        self.actionNew_2.setToolTip(_translate("MainWindow", "New File", None))
        self.actionNew_2.setStatusTip(_translate("MainWindow", "Create a New File...", None))
        self.actionOpen_2.setText(_translate("MainWindow", "Open", None))
        self.actionOpen_2.setToolTip(_translate("MainWindow", "Open File", None))
        self.actionOpen_2.setStatusTip(_translate("MainWindow", "Open an Existing File...", None))
        self.actionUndo_2.setText(_translate("MainWindow", "Undo", None))
        self.actionUndo_2.setToolTip(_translate("MainWindow", "Undo", None))
        self.actionUndo_2.setStatusTip(_translate("MainWindow", "Undo", None))
        self.actionRedo_2.setText(_translate("MainWindow", "Redo", None))
        self.actionRedo_2.setToolTip(_translate("MainWindow", "Redo", None))
        self.actionRedo_2.setStatusTip(_translate("MainWindow", "Redo", None))
        self.actionCut_2.setText(_translate("MainWindow", "Cut", None))
        self.actionCut_2.setToolTip(_translate("MainWindow", "Cut", None))
        self.actionCut_2.setStatusTip(_translate("MainWindow", "Cut", None))
        self.actionCopy_2.setText(_translate("MainWindow", "Copy", None))
        self.actionCopy_2.setToolTip(_translate("MainWindow", "Copy", None))
        self.actionCopy_2.setStatusTip(_translate("MainWindow", "Copy", None))
        self.actionPaste_2.setText(_translate("MainWindow", "Paste", None))
        self.actionPaste_2.setToolTip(_translate("MainWindow", "Paste", None))
        self.actionPaste_2.setStatusTip(_translate("MainWindow", "Paste", None))
        self.actionPrint_2.setText(_translate("MainWindow", "Print", None))
        self.actionPrint_2.setToolTip(_translate("MainWindow", "Print", None))
        self.actionPrint_2.setStatusTip(_translate("MainWindow", "Print this File", None))
        self.actionDelete_2.setText(_translate("MainWindow", "Delete", None))
        self.actionDelete_2.setToolTip(_translate("MainWindow", "Delete", None))
        self.actionDelete_2.setStatusTip(_translate("MainWindow", "Delete", None))
        self.actionFind_2.setText(_translate("MainWindow", "Find", None))
        self.actionFind_2.setToolTip(_translate("MainWindow", "Find", None))
        self.actionFind_2.setStatusTip(_translate("MainWindow", "Find What...", None))
        self.actionSave_2.setText(_translate("MainWindow", "Save", None))
        self.actionSave_2.setToolTip(_translate("MainWindow", "Save", None))
        self.actionSave_2.setStatusTip(_translate("MainWindow", "Save this File", None))
        self.actionSave_as_2.setText(_translate("MainWindow", "Save_as", None))
        self.actionSave_as_2.setToolTip(_translate("MainWindow", "Save As", None))
        self.actionSave_as_2.setStatusTip(_translate("MainWindow", "Save this File As...", None))

import icons_rc
