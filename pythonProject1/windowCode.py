# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowCode.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(574, 482)
        self.tab3_newWindow2 = QtWidgets.QWidget(MainWindow)
        self.tab3_newWindow2.setObjectName("tab3_newWindow2")
        self.tab3_win2tablewidget = QtWidgets.QTableWidget(self.tab3_newWindow2)
        self.tab3_win2tablewidget.setGeometry(QtCore.QRect(0, 40, 571, 441))
        self.tab3_win2tablewidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab3_win2tablewidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab3_win2tablewidget.setAlternatingRowColors(True)
        self.tab3_win2tablewidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tab3_win2tablewidget.setObjectName("tab3_win2tablewidget")
        self.tab3_win2tablewidget.setColumnCount(0)
        self.tab3_win2tablewidget.setRowCount(0)
        self.tab3_win2label = QtWidgets.QLabel(self.tab3_newWindow2)
        self.tab3_win2label.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.tab3_win2label.setObjectName("tab3_win2label")
        self.tab3_win2lineEdit = QtWidgets.QLineEdit(self.tab3_newWindow2)
        self.tab3_win2lineEdit.setGeometry(QtCore.QRect(60, 10, 71, 21))
        self.tab3_win2lineEdit.setObjectName("tab3_win2lineEdit")
        self.tab3_win2lineEdit_2 = QtWidgets.QLineEdit(self.tab3_newWindow2)
        self.tab3_win2lineEdit_2.setGeometry(QtCore.QRect(140, 10, 191, 21))
        self.tab3_win2lineEdit_2.setObjectName("tab3_win2lineEdit_2")
        self.tab3_win2pushButton = QtWidgets.QPushButton(self.tab3_newWindow2)
        self.tab3_win2pushButton.setGeometry(QtCore.QRect(490, 10, 75, 23))
        self.tab3_win2pushButton.setObjectName("tab3_win2pushButton")
        MainWindow.setCentralWidget(self.tab3_newWindow2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tab3_win2tablewidget.setSortingEnabled(False)
        self.tab3_win2label.setText(_translate("MainWindow", "펀드검색"))
        self.tab3_win2pushButton.setText(_translate("MainWindow", "조회"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())