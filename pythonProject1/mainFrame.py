# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1256, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1261, 671))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.tab1_label_7 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_7.setGeometry(QtCore.QRect(250, 620, 181, 20))
        self.tab1_label_7.setText("")
        self.tab1_label_7.setObjectName("tab1_label_7")
        self.tab1_tableWidget = QtWidgets.QTableWidget(self.tab1)
        self.tab1_tableWidget.setGeometry(QtCore.QRect(180, 30, 1071, 571))
        self.tab1_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab1_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab1_tableWidget.setAlternatingRowColors(True)
        self.tab1_tableWidget.setObjectName("tab1_tableWidget")
        self.tab1_tableWidget.setColumnCount(0)
        self.tab1_tableWidget.setRowCount(0)
        self.tab1_label_2 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_2.setGeometry(QtCore.QRect(470, 600, 221, 21))
        self.tab1_label_2.setText("")
        self.tab1_label_2.setObjectName("tab1_label_2")
        self.tab1_label_5 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_5.setGeometry(QtCore.QRect(250, 600, 181, 21))
        self.tab1_label_5.setText("")
        self.tab1_label_5.setObjectName("tab1_label_5")
        self.tab1_label_6 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_6.setGeometry(QtCore.QRect(180, 620, 71, 21))
        self.tab1_label_6.setObjectName("tab1_label_6")
        self.tab1_label = QtWidgets.QLabel(self.tab1)
        self.tab1_label.setGeometry(QtCore.QRect(430, 600, 41, 21))
        self.tab1_label.setObjectName("tab1_label")
        self.tab1_pushButton_2 = QtWidgets.QPushButton(self.tab1)
        self.tab1_pushButton_2.setGeometry(QtCore.QRect(1175, 2, 75, 23))
        self.tab1_pushButton_2.setObjectName("tab1_pushButton_2")
        self.tab1_label_4 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_4.setGeometry(QtCore.QRect(180, 600, 71, 21))
        self.tab1_label_4.setObjectName("tab1_label_4")
        self.tab1_pushButton = QtWidgets.QPushButton(self.tab1)
        self.tab1_pushButton.setEnabled(True)
        self.tab1_pushButton.setGeometry(QtCore.QRect(100, 0, 71, 23))
        self.tab1_pushButton.setObjectName("tab1_pushButton")
        self.tab1_plainTextEdit = QtWidgets.QPlainTextEdit(self.tab1)
        self.tab1_plainTextEdit.setEnabled(True)
        self.tab1_plainTextEdit.setGeometry(QtCore.QRect(0, 260, 171, 71))
        self.tab1_plainTextEdit.setReadOnly(True)
        self.tab1_plainTextEdit.setObjectName("tab1_plainTextEdit")
        self.tab1_listWidget = QtWidgets.QListWidget(self.tab1)
        self.tab1_listWidget.setGeometry(QtCore.QRect(0, 30, 171, 192))
        self.tab1_listWidget.setObjectName("tab1_listWidget")
        self.tab1_label_3 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_3.setGeometry(QtCore.QRect(0, 2, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.tab1_label_3.setFont(font)
        self.tab1_label_3.setObjectName("tab1_label_3")
        self.tab1_pushButton_3 = QtWidgets.QPushButton(self.tab1)
        self.tab1_pushButton_3.setGeometry(QtCore.QRect(0, 230, 75, 23))
        self.tab1_pushButton_3.setObjectName("tab1_pushButton_3")
        self.tab1_pushButton_4 = QtWidgets.QPushButton(self.tab1)
        self.tab1_pushButton_4.setGeometry(QtCore.QRect(180, 0, 75, 23))
        self.tab1_pushButton_4.setObjectName("tab1_pushButton_4")
        self.tab1_label_8 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_8.setGeometry(QtCore.QRect(430, 620, 41, 21))
        self.tab1_label_8.setObjectName("tab1_label_8")
        self.tab1_label_9 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_9.setGeometry(QtCore.QRect(470, 620, 51, 21))
        self.tab1_label_9.setText("")
        self.tab1_label_9.setObjectName("tab1_label_9")
        self.tab1_label_10 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_10.setGeometry(QtCore.QRect(530, 620, 41, 21))
        self.tab1_label_10.setObjectName("tab1_label_10")
        self.tab1_label_11 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_11.setGeometry(QtCore.QRect(570, 620, 141, 21))
        self.tab1_label_11.setText("")
        self.tab1_label_11.setObjectName("tab1_label_11")
        self.tab1_label_12 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_12.setGeometry(QtCore.QRect(90, 230, 31, 21))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(9)
        self.tab1_label_12.setFont(font)
        self.tab1_label_12.setObjectName("tab1_label_12")
        self.tab1_checkBox = QtWidgets.QCheckBox(self.tab1)
        self.tab1_checkBox.setGeometry(QtCore.QRect(130, 230, 21, 21))
        self.tab1_checkBox.setText("")
        self.tab1_checkBox.setChecked(True)
        self.tab1_checkBox.setObjectName("tab1_checkBox")
        self.tab1_label_13 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_13.setGeometry(QtCore.QRect(1180, 600, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab1_label_13.setFont(font)
        self.tab1_label_13.setText("")
        self.tab1_label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tab1_label_13.setObjectName("tab1_label_13")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tab2_pushbutton = QtWidgets.QPushButton(self.tab2)
        self.tab2_pushbutton.setGeometry(QtCore.QRect(1170, 0, 71, 23))
        self.tab2_pushbutton.setObjectName("tab2_pushbutton")
        self.tab2_tablewidget = QtWidgets.QTableWidget(self.tab2)
        self.tab2_tablewidget.setGeometry(QtCore.QRect(180, 30, 1071, 591))
        self.tab2_tablewidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab2_tablewidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab2_tablewidget.setAlternatingRowColors(True)
        self.tab2_tablewidget.setObjectName("tab2_tablewidget")
        self.tab2_tablewidget.setColumnCount(0)
        self.tab2_tablewidget.setRowCount(0)
        self.tab2_comboBox = QtWidgets.QComboBox(self.tab2)
        self.tab2_comboBox.setGeometry(QtCore.QRect(20, 0, 61, 22))
        self.tab2_comboBox.setObjectName("tab2_comboBox")
        self.tab2_label = QtWidgets.QLabel(self.tab2)
        self.tab2_label.setGeometry(QtCore.QRect(1180, 620, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab2_label.setFont(font)
        self.tab2_label.setText("")
        self.tab2_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tab2_label.setObjectName("tab2_label")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.tab3_pushButton = QtWidgets.QPushButton(self.tab3)
        self.tab3_pushButton.setGeometry(QtCore.QRect(1160, 90, 93, 28))
        self.tab3_pushButton.setObjectName("tab3_pushButton")
        self.tab3_tablewidget = QtWidgets.QTableWidget(self.tab3)
        self.tab3_tablewidget.setGeometry(QtCore.QRect(0, 120, 1251, 501))
        self.tab3_tablewidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab3_tablewidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab3_tablewidget.setAlternatingRowColors(True)
        self.tab3_tablewidget.setObjectName("tab3_tablewidget")
        self.tab3_tablewidget.setColumnCount(0)
        self.tab3_tablewidget.setRowCount(0)
        self.tab3_label = QtWidgets.QLabel(self.tab3)
        self.tab3_label.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.tab3_label.setObjectName("tab3_label")
        self.tab3_label_2 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_2.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.tab3_label_2.setObjectName("tab3_label_2")
        self.tab3_label_3 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_3.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.tab3_label_3.setObjectName("tab3_label_3")
        self.tab3_label_4 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_4.setGeometry(QtCore.QRect(450, 10, 151, 21))
        self.tab3_label_4.setObjectName("tab3_label_4")
        self.tab3_label_5 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_5.setGeometry(QtCore.QRect(740, 10, 51, 21))
        self.tab3_label_5.setObjectName("tab3_label_5")
        self.tab3_label_6 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_6.setGeometry(QtCore.QRect(450, 40, 121, 21))
        self.tab3_label_6.setObjectName("tab3_label_6")
        self.tab3_label_7 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_7.setGeometry(QtCore.QRect(760, 40, 101, 21))
        self.tab3_label_7.setObjectName("tab3_label_7")
        self.tab3_label_8 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_8.setGeometry(QtCore.QRect(0, 100, 111, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(10)
        self.tab3_label_8.setFont(font)
        self.tab3_label_8.setObjectName("tab3_label_8")
        self.tab3_label_9 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_9.setGeometry(QtCore.QRect(460, 70, 121, 21))
        self.tab3_label_9.setObjectName("tab3_label_9")
        self.tab3_label_10 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_10.setGeometry(QtCore.QRect(630, 70, 91, 21))
        self.tab3_label_10.setObjectName("tab3_label_10")
        self.tab3_label_11 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_11.setGeometry(QtCore.QRect(760, 70, 161, 21))
        self.tab3_label_11.setObjectName("tab3_label_11")
        self.tab3_comboBox = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox.setGeometry(QtCore.QRect(610, 10, 81, 22))
        self.tab3_comboBox.setObjectName("tab3_comboBox")
        self.tab3_comboBox_2 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_2.setGeometry(QtCore.QRect(800, 10, 76, 22))
        self.tab3_comboBox_2.setObjectName("tab3_comboBox_2")
        self.tab3_comboBox_3 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_3.setGeometry(QtCore.QRect(170, 40, 231, 22))
        self.tab3_comboBox_3.setObjectName("tab3_comboBox_3")
        self.tab3_comboBox_4 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_4.setGeometry(QtCore.QRect(610, 40, 81, 22))
        self.tab3_comboBox_4.setObjectName("tab3_comboBox_4")
        self.tab3_comboBox_5 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_5.setGeometry(QtCore.QRect(70, 70, 161, 22))
        self.tab3_comboBox_5.setObjectName("tab3_comboBox_5")
        self.tab3_checkBox = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox.setGeometry(QtCore.QRect(740, 40, 21, 21))
        self.tab3_checkBox.setText("")
        self.tab3_checkBox.setObjectName("tab3_checkBox")
        self.tab3_checkBox_2 = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox_2.setGeometry(QtCore.QRect(440, 70, 21, 21))
        self.tab3_checkBox_2.setText("")
        self.tab3_checkBox_2.setObjectName("tab3_checkBox_2")
        self.tab3_checkBox_3 = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox_3.setGeometry(QtCore.QRect(610, 70, 21, 21))
        self.tab3_checkBox_3.setText("")
        self.tab3_checkBox_3.setObjectName("tab3_checkBox_3")
        self.tab3_checkBox_4 = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox_4.setGeometry(QtCore.QRect(740, 70, 21, 21))
        self.tab3_checkBox_4.setText("")
        self.tab3_checkBox_4.setObjectName("tab3_checkBox_4")
        self.tab3_dateEdit = QtWidgets.QDateEdit(self.tab3)
        self.tab3_dateEdit.setGeometry(QtCore.QRect(70, 10, 91, 22))
        self.tab3_dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab3_dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.tab3_dateEdit.setCalendarPopup(True)
        self.tab3_dateEdit.setObjectName("tab3_dateEdit")
        self.tab3_dateEdit_2 = QtWidgets.QDateEdit(self.tab3)
        self.tab3_dateEdit_2.setGeometry(QtCore.QRect(190, 10, 91, 22))
        self.tab3_dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab3_dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.tab3_dateEdit_2.setCalendarPopup(True)
        self.tab3_dateEdit_2.setObjectName("tab3_dateEdit_2")
        self.tab3_label_12 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_12.setGeometry(QtCore.QRect(170, 10, 16, 21))
        self.tab3_label_12.setObjectName("tab3_label_12")
        self.tab3_pushButton_2 = QtWidgets.QPushButton(self.tab3)
        self.tab3_pushButton_2.setGeometry(QtCore.QRect(1190, 60, 61, 21))
        self.tab3_pushButton_2.setText("")
        self.tab3_pushButton_2.setObjectName("tab3_pushButton_2")
        self.tab3_lineEdit = QtWidgets.QLineEdit(self.tab3)
        self.tab3_lineEdit.setGeometry(QtCore.QRect(70, 40, 91, 21))
        self.tab3_lineEdit.setObjectName("tab3_lineEdit")
        self.tab3_label_13 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_13.setGeometry(QtCore.QRect(1180, 620, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab3_label_13.setFont(font)
        self.tab3_label_13.setText("")
        self.tab3_label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tab3_label_13.setObjectName("tab3_label_13")
        self.tab3_label_14 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_14.setGeometry(QtCore.QRect(1100, 620, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab3_label_14.setFont(font)
        self.tab3_label_14.setText("")
        self.tab3_label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tab3_label_14.setObjectName("tab3_label_14")
        self.tab3_label_15 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_15.setGeometry(QtCore.QRect(0, 621, 41, 21))
        self.tab3_label_15.setObjectName("tab3_label_15")
        self.tab3_label_16 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_16.setGeometry(QtCore.QRect(50, 621, 41, 21))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(9)
        self.tab3_label_16.setFont(font)
        self.tab3_label_16.setAutoFillBackground(False)
        self.tab3_label_16.setText("")
        self.tab3_label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tab3_label_16.setObjectName("tab3_label_16")
        self.tabWidget.addTab(self.tab3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1256, 21))
        self.menubar.setObjectName("menubar")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        self.menudevelop = QtWidgets.QMenu(self.menuInfo)
        self.menudevelop.setObjectName("menudevelop")
        self.menuetc = QtWidgets.QMenu(self.menubar)
        self.menuetc.setObjectName("menuetc")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actioninfo_site = QtWidgets.QAction(MainWindow)
        self.actioninfo_site.setObjectName("actioninfo_site")
        self.actionset = QtWidgets.QAction(MainWindow)
        self.actionset.setObjectName("actionset")
        self.menudevelop.addAction(self.actioninfo_site)
        self.menuInfo.addAction(self.menudevelop.menuAction())
        self.menuetc.addAction(self.actionset)
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menubar.addAction(self.menuetc.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tab1_tableWidget.setSortingEnabled(True)
        self.tab1_label_6.setText(_translate("MainWindow", "조회데이터:"))
        self.tab1_label.setText(_translate("MainWindow", "값:"))
        self.tab1_pushButton_2.setText(_translate("MainWindow", "엑셀 변환"))
        self.tab1_label_4.setText(_translate("MainWindow", "검색테이블: "))
        self.tab1_pushButton.setText(_translate("MainWindow", "조회"))
        self.tab1_label_3.setText(_translate("MainWindow", "DB리스트"))
        self.tab1_pushButton_3.setText(_translate("MainWindow", "조건검색"))
        self.tab1_pushButton_4.setText(_translate("MainWindow", "그래프"))
        self.tab1_label_8.setText(_translate("MainWindow", "갯수:"))
        self.tab1_label_10.setText(_translate("MainWindow", "합계:"))
        self.tab1_label_12.setText(_translate("MainWindow", "사용"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "데이터 조회"))
        self.tab2_pushbutton.setText(_translate("MainWindow", "조회"))
        self.tab2_tablewidget.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "API 조회"))
        self.tab3_pushButton.setText(_translate("MainWindow", "조회"))
        self.tab3_tablewidget.setSortingEnabled(True)
        self.tab3_label.setText(_translate("MainWindow", "기준일"))
        self.tab3_label_2.setText(_translate("MainWindow", "펀드코드"))
        self.tab3_label_3.setText(_translate("MainWindow", "운용사코드"))
        self.tab3_label_4.setText(_translate("MainWindow", "운용중/운용개시/결산/상환"))
        self.tab3_label_5.setText(_translate("MainWindow", "잔고유무"))
        self.tab3_label_6.setText(_translate("MainWindow", "판매/운용펀드 기준"))
        self.tab3_label_7.setText(_translate("MainWindow", "통합펀드구분여부"))
        self.tab3_label_8.setText(_translate("MainWindow", "펀드정보상세 내역"))
        self.tab3_label_9.setText(_translate("MainWindow", "국외세액환급대상펀드"))
        self.tab3_label_10.setText(_translate("MainWindow", "멀티커런시조회"))
        self.tab3_label_11.setText(_translate("MainWindow", "채권평가보수 유예대상"))
        self.tab3_label_12.setText(_translate("MainWindow", "~"))
        self.tab3_label_15.setText(_translate("MainWindow", "조회수:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "펀드상세내역 조회"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.menudevelop.setTitle(_translate("MainWindow", "develop"))
        self.menuetc.setTitle(_translate("MainWindow", "etc"))
        self.actioninfo_site.setText(_translate("MainWindow", "info site"))
        self.actionset.setText(_translate("MainWindow", "set"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
