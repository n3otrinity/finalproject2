# Form implementation generated from reading ui file 'tictactoeGUI.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.square1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.square1.setGeometry(QtCore.QRect(50, 50, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square1.setFont(font)
        self.square1.setText("")
        self.square1.setObjectName("square1")
        self.square9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.square9.setGeometry(QtCore.QRect(350, 350, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square9.setFont(font)
        self.square9.setText("")
        self.square9.setObjectName("square9")
        self.square8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.square8.setGeometry(QtCore.QRect(200, 350, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square8.setFont(font)
        self.square8.setText("")
        self.square8.setObjectName("square8")
        self.square7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.square7.setGeometry(QtCore.QRect(50, 350, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square7.setFont(font)
        self.square7.setText("")
        self.square7.setObjectName("square7")
        self.square6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.square6.setGeometry(QtCore.QRect(350, 200, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square6.setFont(font)
        self.square6.setText("")
        self.square6.setObjectName("square6")
        self.square5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.square5.setGeometry(QtCore.QRect(200, 200, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square5.setFont(font)
        self.square5.setText("")
        self.square5.setObjectName("square5")
        self.square4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.square4.setGeometry(QtCore.QRect(50, 200, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square4.setFont(font)
        self.square4.setText("")
        self.square4.setObjectName("square4")
        self.square2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.square2.setGeometry(QtCore.QRect(200, 50, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square2.setFont(font)
        self.square2.setText("")
        self.square2.setObjectName("square2")
        self.square3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.square3.setGeometry(QtCore.QRect(350, 50, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square3.setFont(font)
        self.square3.setText("")
        self.square3.setObjectName("square3")
        self.turnLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.turnLabel.setGeometry(QtCore.QRect(570, 20, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.turnLabel.setFont(font)
        self.turnLabel.setObjectName("turnLabel")
        self.xWinLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.xWinLabel.setGeometry(QtCore.QRect(550, 160, 50, 75))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.xWinLabel.setFont(font)
        self.xWinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.xWinLabel.setObjectName("xWinLabel")
        self.oWinLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.oWinLabel.setGeometry(QtCore.QRect(700, 160, 50, 75))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.oWinLabel.setFont(font)
        self.oWinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.oWinLabel.setObjectName("oWinLabel")
        self.xPoints = QtWidgets.QLabel(parent=self.centralwidget)
        self.xPoints.setGeometry(QtCore.QRect(550, 250, 50, 75))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.xPoints.setFont(font)
        self.xPoints.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.xPoints.setObjectName("xPoints")
        self.oPoints = QtWidgets.QLabel(parent=self.centralwidget)
        self.oPoints.setGeometry(QtCore.QRect(700, 250, 50, 75))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.oPoints.setFont(font)
        self.oPoints.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.oPoints.setObjectName("oPoints")
        self.saveButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(520, 340, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.loadButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(660, 340, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.loadButton.setFont(font)
        self.loadButton.setObjectName("loadButton")
        self.reset_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.reset_Button.setGeometry(QtCore.QRect(590, 430, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.reset_Button.setFont(font)
        self.reset_Button.setObjectName("reset_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.turnLabel.setText(_translate("MainWindow", "X\'s Turn"))
        self.xWinLabel.setText(_translate("MainWindow", "X"))
        self.oWinLabel.setText(_translate("MainWindow", "O"))
        self.xPoints.setText(_translate("MainWindow", "0"))
        self.oPoints.setText(_translate("MainWindow", "0"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.loadButton.setText(_translate("MainWindow", "Load"))
        self.reset_Button.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
