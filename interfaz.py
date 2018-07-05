# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.sourceText = QtGui.QTextEdit(self.centralwidget)
        self.sourceText.setGeometry(QtCore.QRect(80, 60, 651, 181))
        self.sourceText.setWhatsThis(_fromUtf8(""))
        self.sourceText.setAutoFillBackground(False)
        self.sourceText.setObjectName(_fromUtf8("sourceText"))
        self.compilarButton = QtGui.QPushButton(self.centralwidget)
        self.compilarButton.setGeometry(QtCore.QRect(360, 260, 88, 29))
        self.compilarButton.setObjectName(_fromUtf8("compilarButton"))
        self.resultText = QtGui.QTextEdit(self.centralwidget)
        self.resultText.setGeometry(QtCore.QRect(80, 310, 651, 191))
        self.resultText.setObjectName(_fromUtf8("resultText"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 151, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 280, 151, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.abrirMenu = QtGui.QMenu(self.menubar)
        self.abrirMenu.setObjectName(_fromUtf8("abrirMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.abrirMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Compilador", None))
        self.compilarButton.setText(_translate("MainWindow", "Compilar", None))
        self.label.setText(_translate("MainWindow", "Codigo fuente:", None))
        self.label_2.setText(_translate("MainWindow", "Resultado:", None))
        self.abrirMenu.setTitle(_translate("MainWindow", "Abrir archivo", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
