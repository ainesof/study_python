# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowGroup.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1189, 354)
        self.tab5_newWindow1 = QtWidgets.QWidget(MainWindow)
        self.tab5_newWindow1.setObjectName("tab5_newWindow1")
        self.tab5_win1tableWidget = QtWidgets.QTableWidget(self.tab5_newWindow1)
        self.tab5_win1tableWidget.setGeometry(QtCore.QRect(0, 70, 1181, 281))
        self.tab5_win1tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab5_win1tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab5_win1tableWidget.setAlternatingRowColors(True)
        self.tab5_win1tableWidget.setObjectName("tab5_win1tableWidget")
        self.tab5_win1tableWidget.setColumnCount(0)
        self.tab5_win1tableWidget.setRowCount(0)
        self.tab5_win1label_5 = QtWidgets.QLabel(self.tab5_newWindow1)
        self.tab5_win1label_5.setGeometry(QtCore.QRect(1111, 28, 31, 21))
        self.tab5_win1label_5.setObjectName("tab5_win1label_5")
        self.tab5_win1label_4 = QtWidgets.QLabel(self.tab5_newWindow1)
        self.tab5_win1label_4.setGeometry(QtCore.QRect(430, 10, 51, 21))
        self.tab5_win1label_4.setObjectName("tab5_win1label_4")
        self.tab5_win1dateEdit = QtWidgets.QDateEdit(self.tab5_newWindow1)
        self.tab5_win1dateEdit.setGeometry(QtCore.QRect(470, 10, 91, 22))
        self.tab5_win1dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab5_win1dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.tab5_win1dateEdit.setCalendarPopup(True)
        self.tab5_win1dateEdit.setObjectName("tab5_win1dateEdit")
        self.tab5_win1comboBox = QtWidgets.QComboBox(self.tab5_newWindow1)
        self.tab5_win1comboBox.setGeometry(QtCore.QRect(260, 10, 151, 22))
        self.tab5_win1comboBox.setObjectName("tab5_win1comboBox")
        self.tab5_win1label_3 = QtWidgets.QLabel(self.tab5_newWindow1)
        self.tab5_win1label_3.setGeometry(QtCore.QRect(230, 10, 31, 21))
        self.tab5_win1label_3.setObjectName("tab5_win1label_3")
        self.tab5_win1pushButton = QtWidgets.QPushButton(self.tab5_newWindow1)
        self.tab5_win1pushButton.setGeometry(QtCore.QRect(1130, 0, 51, 21))
        self.tab5_win1pushButton.setObjectName("tab5_win1pushButton")
        self.tab5_win1label_2 = QtWidgets.QLabel(self.tab5_newWindow1)
        self.tab5_win1label_2.setGeometry(QtCore.QRect(97, 10, 51, 21))
        self.tab5_win1label_2.setObjectName("tab5_win1label_2")
        self.tab5_win1lineEdit = QtWidgets.QLineEdit(self.tab5_newWindow1)
        self.tab5_win1lineEdit.setGeometry(QtCore.QRect(150, 10, 61, 21))
        self.tab5_win1lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.tab5_win1lineEdit.setReadOnly(True)
        self.tab5_win1lineEdit.setObjectName("tab5_win1lineEdit")
        self.tab5_win1lineEdit_2 = QtWidgets.QLineEdit(self.tab5_newWindow1)
        self.tab5_win1lineEdit_2.setGeometry(QtCore.QRect(0, 50, 1181, 21))
        self.tab5_win1lineEdit_2.setReadOnly(True)
        self.tab5_win1lineEdit_2.setObjectName("tab5_win1lineEdit_2")
        self.tab5_win1lineEdit_3 = QtWidgets.QLineEdit(self.tab5_newWindow1)
        self.tab5_win1lineEdit_3.setGeometry(QtCore.QRect(200, 50, 391, 21))
        self.tab5_win1lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.tab5_win1lineEdit_3.setReadOnly(True)
        self.tab5_win1lineEdit_3.setObjectName("tab5_win1lineEdit_3")
        self.tab5_win1lineEdit_4 = QtWidgets.QLineEdit(self.tab5_newWindow1)
        self.tab5_win1lineEdit_4.setGeometry(QtCore.QRect(600, 50, 341, 21))
        self.tab5_win1lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.tab5_win1lineEdit_4.setReadOnly(True)
        self.tab5_win1lineEdit_4.setObjectName("tab5_win1lineEdit_4")
        self.tab5_win1label = QtWidgets.QLabel(self.tab5_newWindow1)
        self.tab5_win1label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.tab5_win1label.setAutoFillBackground(True)
        self.tab5_win1label.setText("")
        self.tab5_win1label.setObjectName("tab5_win1label")
        self.tab5_win1comboBox_2 = QtWidgets.QComboBox(self.tab5_newWindow1)
        self.tab5_win1comboBox_2.setEnabled(True)
        self.tab5_win1comboBox_2.setGeometry(QtCore.QRect(1139, 27, 41, 22))
        self.tab5_win1comboBox_2.setEditable(False)
        self.tab5_win1comboBox_2.setCurrentText("")
        self.tab5_win1comboBox_2.setObjectName("tab5_win1comboBox_2")
        self.tab5_win1pushButton_2 = QtWidgets.QPushButton(self.tab5_newWindow1)
        self.tab5_win1pushButton_2.setGeometry(QtCore.QRect(1050, 0, 71, 21))
        self.tab5_win1pushButton_2.setObjectName("tab5_win1pushButton_2")
        self.tab5_win1lineEdit_2.raise_()
        self.tab5_win1tableWidget.raise_()
        self.tab5_win1label_5.raise_()
        self.tab5_win1label_4.raise_()
        self.tab5_win1dateEdit.raise_()
        self.tab5_win1comboBox.raise_()
        self.tab5_win1label_3.raise_()
        self.tab5_win1pushButton.raise_()
        self.tab5_win1label_2.raise_()
        self.tab5_win1lineEdit.raise_()
        self.tab5_win1lineEdit_3.raise_()
        self.tab5_win1lineEdit_4.raise_()
        self.tab5_win1label.raise_()
        self.tab5_win1comboBox_2.raise_()
        self.tab5_win1pushButton_2.raise_()
        MainWindow.setCentralWidget(self.tab5_newWindow1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tab5_win1tableWidget.setSortingEnabled(False)
        self.tab5_win1label_5.setText(_translate("MainWindow", "단위"))
        self.tab5_win1label_4.setText(_translate("MainWindow", "기준일"))
        self.tab5_win1label_3.setText(_translate("MainWindow", "고객"))
        self.tab5_win1pushButton.setText(_translate("MainWindow", "조회"))
        self.tab5_win1label_2.setText(_translate("MainWindow", "고객그룹"))
        self.tab5_win1lineEdit_3.setText(_translate("MainWindow", "순자산 증감"))
        self.tab5_win1lineEdit_4.setText(_translate("MainWindow", "수탁고 설정액"))
        self.tab5_win1pushButton_2.setText(_translate("MainWindow", "엑셀 변환"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())