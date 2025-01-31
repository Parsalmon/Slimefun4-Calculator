# Form implementation generated from reading ui file 'QT Main.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from solver import Solver

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.craftablesTable = QtWidgets.QTableWidget(self.centralwidget)
        self.craftablesTable.setGeometry(QtCore.QRect(10, 45, 491, 181))
        self.craftablesTable.setObjectName("craftablesTable")
        self.craftablesTable.setColumnCount(2)
        self.craftablesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.craftablesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.craftablesTable.setHorizontalHeaderItem(1, item)
        self.inputlabel = QtWidgets.QLabel(self.centralwidget)
        self.inputlabel.setGeometry(QtCore.QRect(11, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inputlabel.setFont(font)
        self.inputlabel.setObjectName("inputlabel")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 227, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.outputLabel.setFont(font)
        self.outputLabel.setObjectName("outputLabel")
        self.solveButton = QtWidgets.QPushButton(self.centralwidget)
        self.solveButton.setGeometry(QtCore.QRect(510, 185, 120, 40))
        self.solveButton.setObjectName("solveButton")
        self.inputDivider = QtWidgets.QFrame(self.centralwidget)
        self.inputDivider.setGeometry(QtCore.QRect(10, 30, 621, 16))
        self.inputDivider.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.inputDivider.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.inputDivider.setObjectName("inputDivider")
        self.outputDivider = QtWidgets.QFrame(self.centralwidget)
        self.outputDivider.setGeometry(QtCore.QRect(10, 243, 621, 16))
        self.outputDivider.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.outputDivider.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.outputDivider.setObjectName("outputDivider")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(510, 140, 120, 40))
        self.removeButton.setObjectName("removeButton")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(510, 40, 120, 40))
        self.AddButton.setObjectName("AddButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.craftablesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.craftablesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Count"))
        self.inputlabel.setText(_translate("MainWindow", "To Craft"))
        self.outputLabel.setText(_translate("MainWindow", "Output"))
        self.solveButton.setText(_translate("MainWindow", "Solve"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.AddButton.setText(_translate("MainWindow", "Add"))

    def connectSlots(self):
        self.AddButton.clicked.connect(lambda x: self.insertButtonHandler())
        self.removeButton.clicked.connect(lambda x: self.craftablesTable.removeRow(self.craftablesTable.currentRow()))
        self.solveButton.clicked.connect(lambda x: Solver().importUI(self))

    def insertButtonHandler(self):
        self.craftablesTable.insertRow(self.craftablesTable.currentRow()+1)
        self.craftablesTable.setItem(self.craftablesTable.currentRow()+1, 1, QtWidgets.QTableWidgetItem("1"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.show()
    a = Ui_MainWindow()
    a.setupUi(window)
    a.connectSlots()
    a.insertButtonHandler()
    a.craftablesTable.setItem(0, 0, QtWidgets.QTableWidgetItem("slimefun4:advanced_circuit_board"))
    a.craftablesTable.setItem(0, 1, QtWidgets.QTableWidgetItem("32"))
    app.exec()