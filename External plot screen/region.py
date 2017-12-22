# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'region.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1421, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_plotAndSelect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plotAndSelect.setGeometry(QtCore.QRect(300, 100, 187, 57))
        self.pushButton_plotAndSelect.setObjectName("pushButton_plotAndSelect")
        self.textBrowser_messages = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_messages.setGeometry(QtCore.QRect(15, 181, 1391, 311))
        self.textBrowser_messages.setObjectName("textBrowser_messages")
        self.pushButton_getValues = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getValues.setGeometry(QtCore.QRect(740, 100, 361, 57))
        self.pushButton_getValues.setObjectName("pushButton_getValues")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1421, 47))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_plotAndSelect.setText(_translate("MainWindow", "plot and select"))
        self.pushButton_getValues.setText(_translate("MainWindow", "get values selected in plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

