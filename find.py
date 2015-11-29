# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'find.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(365, 116)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Dialog.setWindowOpacity(1.0)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 10, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 40, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 191, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 90, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(150, 50, 120, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 41, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 30, 51, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Find", None))
        self.pushButton.setText(_translate("Dialog", "Find Next", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancel", None))
        self.label.setText(_translate("Dialog", "Find What:", None))
        self.checkBox.setText(_translate("Dialog", "Match Case", None))
        self.groupBox.setTitle(_translate("Dialog", "Direction", None))
        self.radioButton.setText(_translate("Dialog", "UP", None))
        self.radioButton_2.setText(_translate("Dialog", "Down", None))

