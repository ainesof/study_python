# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import decimal
import math, os.path, sys, traceback
import cx_Oracle
import matplotlib.pyplot as plt
import pandas as pd
import requests, bs4
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


class Ui_MainWindow(object):
    def __init__(self):
        self.fig = plt.Figure()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1256, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1261, 801))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.label_7 = QtWidgets.QLabel(self.tab1)
        self.label_7.setGeometry(QtCore.QRect(250, 750, 181, 20))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.tab1)
        self.tableWidget.setGeometry(QtCore.QRect(180, 30, 1051, 701))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.tab1)
        self.label_2.setGeometry(QtCore.QRect(470, 730, 221, 21))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.tab1)
        self.label_5.setGeometry(QtCore.QRect(250, 730, 181, 21))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab1)
        self.label_6.setGeometry(QtCore.QRect(180, 750, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(430, 730, 41, 21))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2.setGeometry(QtCore.QRect(1150, 0, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.tab1)
        self.label_4.setGeometry(QtCore.QRect(180, 730, 71, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.tab1)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(100, 0, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab1)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 260, 171, 71))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.listWidget = QtWidgets.QListWidget(self.tab1)
        self.listWidget.setGeometry(QtCore.QRect(0, 30, 171, 192))
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(self.tab1)
        self.label_3.setGeometry(QtCore.QRect(0, 2, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 230, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 0, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_8 = QtWidgets.QLabel(self.tab1)
        self.label_8.setGeometry(QtCore.QRect(430, 750, 41, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab1)
        self.label_9.setGeometry(QtCore.QRect(470, 750, 51, 21))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab1)
        self.label_10.setGeometry(QtCore.QRect(530, 750, 41, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab1)
        self.label_11.setGeometry(QtCore.QRect(570, 750, 141, 21))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab1)
        self.label_12.setGeometry(QtCore.QRect(90, 230, 31, 21))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.checkBox = QtWidgets.QCheckBox(self.tab1)
        self.checkBox.setGeometry(QtCore.QRect(130, 230, 21, 21))
        self.checkBox.setText("")
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tab2_pushbutton = QtWidgets.QPushButton(self.tab2)
        self.tab2_pushbutton.setGeometry(QtCore.QRect(100, 0, 71, 23))
        self.tab2_pushbutton.setObjectName("tab2_pushbutton")
        self.tab2_tablewidget = QtWidgets.QTableWidget(self.tab2)
        self.tab2_tablewidget.setGeometry(QtCore.QRect(180, 30, 1051, 701))
        self.tab2_tablewidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab2_tablewidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab2_tablewidget.setAlternatingRowColors(True)
        self.tab2_tablewidget.setObjectName("tab2_tablewidget")
        self.tab2_tablewidget.setColumnCount(0)
        self.tab2_tablewidget.setRowCount(0)
        self.tab2_comboBox = QtWidgets.QComboBox(self.tab2)
        self.tab2_comboBox.setGeometry(QtCore.QRect(20, 0, 61, 22))
        self.tab2_comboBox.setObjectName("tab2_comboBox")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.tab3_pushButton = QtWidgets.QPushButton(self.tab3)
        self.tab3_pushButton.setGeometry(QtCore.QRect(1130, 0, 93, 28))
        self.tab3_pushButton.setObjectName("tab3_pushButton")
        self.tab3_tablewidget = QtWidgets.QTableWidget(self.tab3)
        self.tab3_tablewidget.setGeometry(QtCore.QRect(0, 140, 1241, 631))
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
        self.tab3_label_8.setGeometry(QtCore.QRect(10, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(10)
        self.tab3_label_8.setFont(font)
        self.tab3_label_8.setObjectName("tab3_label_8")
        self.tab3_label_9 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_9.setGeometry(QtCore.QRect(460, 80, 121, 21))
        self.tab3_label_9.setObjectName("tab3_label_9")
        self.tab3_label_10 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_10.setGeometry(QtCore.QRect(630, 80, 91, 21))
        self.tab3_label_10.setObjectName("tab3_label_10")
        self.tab3_label_11 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_11.setGeometry(QtCore.QRect(760, 80, 161, 21))
        self.tab3_label_11.setObjectName("tab3_label_11")
        self.tab3_label_12 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_12.setGeometry(QtCore.QRect(960, 80, 121, 21))
        self.tab3_label_12.setObjectName("tab3_label_12")
        self.tab3_comboBox = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox.setGeometry(QtCore.QRect(610, 10, 81, 22))
        self.tab3_comboBox.setObjectName("tab3_comboBox")
        self.tab3_comboBox_2 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_2.setGeometry(QtCore.QRect(800, 10, 76, 22))
        self.tab3_comboBox_2.setObjectName("tab3_comboBox_2")
        self.tab3_comboBox_3 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_3.setGeometry(QtCore.QRect(70, 40, 321, 22))
        self.tab3_comboBox_3.setObjectName("tab3_comboBox_3")
        self.tab3_comboBox_4 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_4.setGeometry(QtCore.QRect(610, 40, 81, 22))
        self.tab3_comboBox_4.setObjectName("tab3_comboBox_4")
        self.tab3_comboBox_5 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_5.setGeometry(QtCore.QRect(70, 70, 111, 22))
        self.tab3_comboBox_5.setObjectName("tab3_comboBox_5")
        self.tab3_checkBox = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox.setGeometry(QtCore.QRect(740, 40, 21, 21))
        self.tab3_checkBox.setText("")
        self.tab3_checkBox.setObjectName("tab3_checkBox")
        self.tab3_checkBox_2 = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox_2.setGeometry(QtCore.QRect(440, 80, 21, 21))
        self.tab3_checkBox_2.setText("")
        self.tab3_checkBox_2.setObjectName("tab3_checkBox_2")
        self.tab3_checkBox_3 = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox_3.setGeometry(QtCore.QRect(610, 80, 21, 21))
        self.tab3_checkBox_3.setText("")
        self.tab3_checkBox_3.setObjectName("tab3_checkBox_3")
        self.tab3_checkBox_4 = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox_4.setGeometry(QtCore.QRect(740, 80, 21, 21))
        self.tab3_checkBox_4.setText("")
        self.tab3_checkBox_4.setObjectName("tab3_checkBox_4")
        self.tab3_checkBox_5 = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox_5.setGeometry(QtCore.QRect(940, 80, 21, 21))
        self.tab3_checkBox_5.setText("")
        self.tab3_checkBox_5.setObjectName("tab3_checkBox_5")
        self.tab3_dateEdit = QtWidgets.QDateEdit(self.tab3)
        self.tab3_dateEdit.setGeometry(QtCore.QRect(70, 10, 91, 22))
        self.tab3_dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab3_dateEdit.setObjectName("tab3_dateEdit")
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(True)
        self.label_6.setText(_translate("MainWindow", "조회데이터:"))
        self.label.setText(_translate("MainWindow", "값:"))
        self.pushButton_2.setText(_translate("MainWindow", "엑셀 변환"))
        self.label_4.setText(_translate("MainWindow", "검색테이블: "))
        self.pushButton.setText(_translate("MainWindow", "조회"))
        self.label_3.setText(_translate("MainWindow", "DB리스트"))
        self.pushButton_3.setText(_translate("MainWindow", "조건검색"))
        self.pushButton_4.setText(_translate("MainWindow", "그래프"))
        self.label_8.setText(_translate("MainWindow", "갯수:"))
        self.label_10.setText(_translate("MainWindow", "합계:"))
        self.label_12.setText(_translate("MainWindow", "사용"))
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
        self.tab3_label_11.setText(_translate("MainWindow", "펀드결제수수료면제/유예펀드"))
        self.tab3_label_12.setText(_translate("MainWindow", "채권평가보수유예펀드"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "펀드상세내역 조회"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.menudevelop.setTitle(_translate("MainWindow", "develop"))
        self.menuetc.setTitle(_translate("MainWindow", "etc"))
        self.actioninfo_site.setText(_translate("MainWindow", "info site"))
        self.actionset.setText(_translate("MainWindow", "set"))

        # 클래스 변수
        Ui_MainWindow.selectedTable = ""  # DB리스트 선택값
        Ui_MainWindow.dfRow = 0  # 검색된 자료 row
        Ui_MainWindow.mainWindow_df = ""  # 메인 자료값 df
        Ui_MainWindow.sqlQuery1 = ""  # 추가 조건
        Ui_MainWindow.maxSearch = 1000  # 최대 조회가능 숫자

        # Qt디자이너 외 구현
        self.setListWidget()  # DB리스트 생성
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 내용수정 금지
        self.tab1_newWindow1 = QDialog()  # 검색조건 팝업창
        self.tab1_newWindow2 = QDialog()  # 그래픽부분 팝업창
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.tab2_comboBox.addItem('xml')
        self.tab2_comboBox.addItem('json')
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)  # 헤더 중앙정렬
        self.settab3_comboBox_3() # 추가할 펀드명이 너무 많아서 뒤에 작성


        # 이벤트
        # self.menuetc.triggered.connect() # 툴바 메뉴선택
        self.pushButton.clicked.connect(self.createTable)  # 조회
        self.pushButton_2.clicked.connect(self.toExcel)  # 엑셀변환 버튼
        self.tableWidget.cellClicked.connect(self.cellClickEvent)  # 표 클릭시
        self.tableWidget.currentCellChanged.connect(self.cellClickEvent)  # 표 클릭시
        self.listWidget.currentItemChanged.connect(self.clickListWidget)  # DB리스트 클릭시
        self.listWidget.doubleClicked.connect(self.createTable)  # DB리스트 더블클릭시
        self.listWidget.itemActivated.connect(self.createTable) # DB리스트에서 엔터키 입력시
        self.pushButton_3.clicked.connect(self.windowQuery)  # 검색조건 팝업 버튼
        self.pushButton_4.clicked.connect(self.windowGraphic)  # 그래픽 팝업 버튼
        self.checkBox.stateChanged.connect(self.chkBox)  # 체크 변경시
        self.tab2_pushbutton.clicked.connect(self.connectAPI)  # API 자료조회
        self.tab3_pushButton.clicked.connect(self.tab3_createTable)
        # -----------------------------------windowGraphic

    def windowGraphic(self):
        """그래프 차트 창 """

        self.tab1_newWindow2.setObjectName("tab1_newWindow2")
        self.tab1_win2label = QtWidgets.QLabel(self.tab1_newWindow2)
        self.tab1_win2label.setGeometry(QtCore.QRect(10, 10, 56, 21))
        self.tab1_win2label.setObjectName("tab1_win2label")
        self.tab1_win2comboBox = QtWidgets.QComboBox(self.tab1_newWindow2)
        self.tab1_win2comboBox.setGeometry(QtCore.QRect(240, 10, 171, 22))
        self.tab1_win2comboBox.setObjectName("tab1_win2comboBox")
        self.tab1_win2comboBox_2 = QtWidgets.QComboBox(self.tab1_newWindow2)
        self.tab1_win2comboBox_2.setGeometry(QtCore.QRect(70, 10, 111, 22))
        self.tab1_win2comboBox_2.setObjectName("tab1_win2comboBox_2")
        self.tab1_win2textEdit = QtWidgets.QTextEdit(self.tab1_newWindow2)
        self.tab1_win2textEdit.setGeometry(QtCore.QRect(10, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(9)
        self.tab1_win2textEdit.setFont(font)
        self.tab1_win2textEdit.setObjectName("tab1_win2textEdit")
        self.tab1_win2widget = QtWidgets.QWidget(self.tab1_newWindow2)
        self.tab1_win2widget.setGeometry(QtCore.QRect(90, 40, 731, 581))
        self.tab1_win2widget.setObjectName("tab1_win2widget")
        self.tab1_win2pushButton = QtWidgets.QPushButton(self.tab1_newWindow2)
        self.tab1_win2pushButton.setGeometry(QtCore.QRect(420, 10, 51, 21))
        self.tab1_win2pushButton.setObjectName("tab1_win2pushButton")
        self.tab1_win2label_2 = QtWidgets.QLabel(self.tab1_newWindow2)
        self.tab1_win2label_2.setGeometry(QtCore.QRect(190, 10, 56, 21))
        self.tab1_win2label_2.setObjectName("tab1_win2label_2")

        _translate = QtCore.QCoreApplication.translate
        self.tab1_win2label.setText(_translate("t1Window2", "선택 항목"))
        self.tab1_win2pushButton.setText(_translate("t1Window2", "조회"))

        # Qt디자이너 외 구현
        chart = ["원형차트", "선차트", "막대차트", "산포도"]

        try:
            for i in Ui_MainWindow.mainWindow_df.columns.values.tolist():
                self.tab1_win2comboBox.addItem(i)
            for i in chart:
                self.tab1_win2comboBox_2.addItem(i)

            plt.ion()
            self.fig = plt.Figure()
            self.canvas = FigureCanvas(self.fig)
            layout = QVBoxLayout(self.tab1_win2widget)
            layout.addWidget(self.canvas)

            # self.tab1_win2widget.addToolBar(NavigationToolbar(self.canvas, self.tab1_win2widget)) # 툴바 추가가 안됨
            self.tab1_newWindow2.setWindowModality(QtCore.Qt.ApplicationModal)  # 하위창 컨트롤 금지
            self.tab1_newWindow2.show()
            plt.close(self.fig)  # 종료시 차트 지움

            # 이벤트
            self.tab1_win2pushButton.clicked.connect(lambda: self.selectGraphic(chart))  # 그래픽 팝업 버튼

        except:
            traceback.print_exc()

    def selectGraphic(self, chart):
        """ 차트 선택"""
        if self.tab1_win2comboBox_2.currentText() == chart[0]:
            self.set_GraphicPie()
        elif self.tab1_win2comboBox_2.currentText() == chart[1]:
            self.set_GraphLine()
        elif self.tab1_win2comboBox_2.currentText() == chart[2]:
            self.set_GraphBar()
        elif self.tab1_win2comboBox_2.currentText() == chart[3]:
            self.set_GraphScatter()
        else:
            traceback.print_exc()

    def chartValue(self):
        """ 차트에 쓸 인덱스, 값 계산해서 리턴"""
        val = []  # 값
        idx = []  # 라벨

        groupd = Ui_MainWindow.mainWindow_df.groupby([self.tab1_win2comboBox.currentText()]).count()
        groupd2 = groupd.iloc[:, 0]
        idx = groupd2.index
        for i in groupd2:
            val.append(i)
        return idx, val

    def set_GraphicPie(self):
        """내부쿼리 운용회사펀드그룹코드-펀드코드 조회시에는 에러 MatplotlibDeprecationWarning: normalize=None does not normalize if the sum is less than 1 but this behavior is deprecated since 3.3 until two minor releases later."""
        # explode = (0.1, 0, 0, 0)  # 차트의 간격 부분으로 0끼리는 붙어있음 컬럼수와 맞아야함

        idx, val = self.chartValue()
        self.canvas.figure.clear()  # 차트 다시 그림
        self.tab1_win2widget.chart = self.canvas.figure.subplots()
        self.tab1_win2widget.chart.pie(val, labels=idx, autopct="%1.1f%%", shadow=True, startangle=90)
        self.tab1_win2widget.chart.axis("equal")
        self.canvas.draw()

    def set_GraphLine(self):
        """선 차트"""
        idx, val = self.chartValue()
        self.canvas.figure.clear()  # 차트 다시 그림
        self.tab1_win2widget.chart = self.canvas.figure.subplots()
        self.tab1_win2widget.chart.plot(idx, val)
        self.canvas.draw()

    def set_GraphBar(self):
        """막대 차트"""
        idx, val = self.chartValue()
        self.canvas.figure.clear()  # 차트 다시 그림
        self.tab1_win2widget.chart = self.canvas.figure.subplots()
        self.tab1_win2widget.chart.bar(idx, val)
        self.canvas.draw()

    def set_GraphScatter(self):
        """막대 차트"""
        idx, val = self.chartValue()
        self.canvas.figure.clear()  # 차트 다시 그림
        self.tab1_win2widget.chart = self.canvas.figure.subplots()
        self.tab1_win2widget.chart.scatter(idx, val)
        self.canvas.draw()

    # --------------------------------------------windowQuery
    def windowQuery(self):
        """ 검색조건 추가 창 """
        self.tab1_win1label = QtWidgets.QLabel(self.tab1_newWindow1)
        self.tab1_win1label.setGeometry(QtCore.QRect(0, 40, 51, 21))
        self.tab1_win1label.setObjectName("tab1_win1label")
        self.tab1_win1comboBox = QtWidgets.QComboBox(self.tab1_newWindow1)
        self.tab1_win1comboBox.setGeometry(QtCore.QRect(40, 70, 151, 22))
        self.tab1_win1comboBox.setObjectName("tab1_win1comboBox")
        self.tab1_win1label_2 = QtWidgets.QLabel(self.tab1_newWindow1)
        self.tab1_win1label_2.setGeometry(QtCore.QRect(90, 40, 51, 21))
        self.tab1_win1label_2.setObjectName("tab1_win1label_2")
        self.tab1_win1comboBox_3 = QtWidgets.QComboBox(self.tab1_newWindow1)
        self.tab1_win1comboBox_3.setGeometry(QtCore.QRect(200, 70, 71, 22))
        self.tab1_win1comboBox_3.setObjectName("tab1_win1comboBox_3")
        self.tab1_win1lineEdit = QtWidgets.QLineEdit(self.tab1_newWindow1)
        self.tab1_win1lineEdit.setGeometry(QtCore.QRect(280, 70, 121, 21))
        self.tab1_win1lineEdit.setObjectName("tab1_win1lineEdit")
        self.tab1_win1pushButton = QtWidgets.QPushButton(self.tab1_newWindow1)
        self.tab1_win1pushButton.setGeometry(QtCore.QRect(340, 10, 75, 23))
        self.tab1_win1pushButton.setObjectName("tab1_win1pushButton")
        self.tab1_win1checkBox = QtWidgets.QCheckBox(self.tab1_newWindow1)
        self.tab1_win1checkBox.setEnabled(True)
        self.tab1_win1checkBox.setGeometry(QtCore.QRect(20, 70, 21, 20))
        self.tab1_win1checkBox.setText("")
        self.tab1_win1checkBox.setChecked(True)
        self.tab1_win1checkBox.setObjectName("tab1_win1checkBox")
        self.tab1_win1lineEdit_2 = QtWidgets.QLineEdit(self.tab1_newWindow1)
        self.tab1_win1lineEdit_2.setEnabled(False)
        self.tab1_win1lineEdit_2.setGeometry(QtCore.QRect(280, 100, 121, 21))
        self.tab1_win1lineEdit_2.setReadOnly(False)
        self.tab1_win1lineEdit_2.setObjectName("tab1_win1lineEdit_2")
        self.tab1_win1comboBox_4 = QtWidgets.QComboBox(self.tab1_newWindow1)
        self.tab1_win1comboBox_4.setGeometry(QtCore.QRect(200, 100, 71, 22))
        self.tab1_win1comboBox_4.setObjectName("tab1_win1comboBox_4")
        self.tab1_win1checkBox_2 = QtWidgets.QCheckBox(self.tab1_newWindow1)
        self.tab1_win1checkBox_2.setEnabled(True)
        self.tab1_win1checkBox_2.setGeometry(QtCore.QRect(20, 100, 21, 20))
        self.tab1_win1checkBox_2.setText("")
        self.tab1_win1checkBox_2.setObjectName("tab1_win1checkBox_2")
        self.tab1_win1comboBox_2 = QtWidgets.QComboBox(self.tab1_newWindow1)
        self.tab1_win1comboBox_2.setGeometry(QtCore.QRect(40, 100, 151, 22))
        self.tab1_win1comboBox_2.setObjectName("tab1_win1comboBox_2")
        self.tab1_win1label_3 = QtWidgets.QLabel(self.tab1_newWindow1)
        self.tab1_win1label_3.setGeometry(QtCore.QRect(210, 40, 51, 21))
        self.tab1_win1label_3.setObjectName("tab1_win1label_3")
        self.tab1_win1label_4 = QtWidgets.QLabel(self.tab1_newWindow1)
        self.tab1_win1label_4.setGeometry(QtCore.QRect(330, 40, 51, 21))
        self.tab1_win1label_4.setObjectName("tab1_win1label_4")

        _translate = QtCore.QCoreApplication.translate
        self.tab1_win1label.setText(_translate("MainWindow", "사용여부"))
        self.tab1_win1label_2.setText(_translate("MainWindow", "검색 항목"))
        self.tab1_win1pushButton.setText(_translate("MainWindow", "확인"))
        self.tab1_win1label_3.setText(_translate("MainWindow", "검색 조건"))
        self.tab1_win1label_4.setText(_translate("MainWindow", "값"))

        # QT디자이너 외 구현
        self.tab1_newWindow1.sqlQuery = ""
        self.tab1_newWindow1.setWindowTitle("조건검색창")
        self.tab1_newWindow1.setWindowModality(QtCore.Qt.ApplicationModal)  # 하위창 컨트롤 금지
        self.tab1_newWindow1.resize(426, 298)
        self.tab1_win1pushButton.setDisabled(False)  # 쿼리추가 버튼 비활성화
        self.setCombobox()
        self.tab1_newWindow1.show()

        # 이벤트
        self.tab1_win1pushButton.clicked.connect(self.submitQuery)  # 확인버튼 누를시
        self.tab1_win1checkBox.stateChanged.connect(self.ableQuery1)  # 체크박스 변화시
        self.tab1_win1checkBox_2.stateChanged.connect(self.ableQuery2)

    def ableQuery1(self):
        """ 체크시 옆에 텍스트박스 활성화, 해제시 비활성화+값 지움"""
        if self.tab1_win1checkBox.isChecked():
            self.tab1_win1lineEdit.setEnabled(True)  # 입력문 활성화
            self.tab1_win1pushButton.setDisabled(False)
        else:
            self.tab1_win1lineEdit.setEnabled(False)
            self.tab1_win1lineEdit.setText("")

    def ableQuery2(self):
        if self.tab1_win1checkBox_2.isChecked():
            self.tab1_win1lineEdit_2.setEnabled(True)  # 입력문 활성화
            self.tab1_win1pushButton.setDisabled(False)
        else:
            self.tab1_win1lineEdit_2.setEnabled(False)
            self.tab1_win1lineEdit_2.setText("")

    def submitQuery(self):
        """ 추가검색조건 SQL에 추가"""
        sql1 = ""
        sql2 = ""
        if self.tab1_win1lineEdit.text() == "":
            self.tab1_win1lineEdit.setEnabled(False)
            self.tab1_win1checkBox.setChecked(False)
        else:
            sql1 = self.setQuery(self.tab1_win1comboBox.currentText(), self.tab1_win1comboBox_3.currentIndex(),
                                 self.tab1_win1lineEdit.text())
        if self.tab1_win1lineEdit_2.text() == "":
            self.tab1_win1lineEdit_2.setEnabled(False)
            self.tab1_win1checkBox_2.setChecked(False)
        else:
            sql2 = self.setQuery(self.tab1_win1comboBox_2.currentText(), self.tab1_win1comboBox_4.currentIndex(),
                                 self.tab1_win1lineEdit_2.text())
        Ui_MainWindow.sqlQuery1 = sql1 + sql2
        self.plainTextEdit.setPlainText(Ui_MainWindow.sqlQuery1.replace("and ", "", 1))
        self.checkBox.setChecked(True)
        self.plainTextEdit.setEnabled(True)
        self.createTable()
        self.tab1_newWindow1.close()

    def setQuery(self, columnText, i, lineEditText):
        """ 조건을 설정해 SQL에 추가 """
        str1 = [" like '%", " = '", " != '", " <= '", " >= '"]
        str2 = ["%'", "'"]
        sql = " and " + columnText + str1[i] + lineEditText + str2[math.trunc((i + 9) / 10)]
        return sql

    def setCombobox(self):
        """ 콤보박스값들 설정 """
        comboList = ["부분일치", "일치", "제외", "이상", "이하"]
        for i in comboList:
            self.tab1_win1comboBox_3.addItem(i)
            self.tab1_win1comboBox_4.addItem(i)
        for i in Ui_MainWindow.mainWindow_df.columns.values.tolist():
            self.tab1_win1comboBox.addItem(i)
            self.tab1_win1comboBox_2.addItem(i)

    # -----------------------------------------------tab1

    def actpopup(self):
        """ 특정 테이블만 팝업 사용가능"""
        # accessGraphic=["FUND_COMPANY"]
        # if Ui_MainWindow.selectedTable in actGraphic:
        #     self.pushButton_4.setDisabled(False)
        # else:
        #     self.pushButton_4.setDisabled(True)
        self.pushButton_4.setDisabled(False)

    def chkBox(self):
        """조건 비활성화 유무 표시"""
        self.createTable()
        if self.checkBox.isChecked():
            self.plainTextEdit.setEnabled(True)
        else:
            self.plainTextEdit.setEnabled(False)

    def setListWidget(self):
        """ 왼쪽 리스트에 DB리스트 생성. 리스트는 하드코딩 약 8만건 기준 조회시간 30초 """
        dbList = ["공통코드","운용역코드","펀드_결산기준가격", "펀드_기준가격", "펀드_기준가격회계", "펀드_마스터", "펀드_민감도내역",
                  "펀드_보수계산정보", "펀드_보수율", "펀드_보수일별집계", "펀드_설정해지결제", "펀드_설정해지내역", "펀드_설정해지보수",
                  "펀드_설정해지예정내역", "펀드_설정해지원장", "펀드_수익자정보", "펀드_운용회사변경내역", "펀드_위탁사별구조관계총괄", "펀드_위탁사별펀드정보",
                  "펀드_전체해지이체거래", "펀드_총계정원장", "펀드_판매사별보수내역", "펀드_판매사별실적",
                  "펀드_환율적용방법", "정보_거래그룹", "정보_거래유형", "정보_계정과목", "정보_국가", "정보_매매처", "정보_발행기관",
                  "정보_발행기관예외", "정보_부실보증기관", "정보_사무수탁사", "정보_수익자", "정보_신용등급", "정보_업종", "정보_운용역담당펀드",
                  "정보_자산분류", "정보_증권거래소", "정보_증권거래소회사업종", "정보_채권기준종류", "정보_코스콤채권종류", "정보_팀",
                  "정보_팀별운용역", "정보_판매회사펀드", "정보_펀드자체유형", "정보_펀드협회분류코드", "정보_펀드회계유형", "정보_평가회사채권분류",
                  "정보_회사", "정보_회사그룹", "평가_벤치마크지수", "평가_펀드기여손익", "평가_펀드목표수익",
                  "평가_펀드부문손익", "평가_펀드부문손익률", "평가_펀드성과평가","국가별공휴일"
                    ,"기타_공휴일","기타_관심펀드","기타_달력일자","기타_시스템체크","기타_일자"

                  ]
        self.listWidget.addItems(dbList)

    def clickListWidget(self):
        """ DB리스트 클릭시 클래스 변수에 값을 저장 """
        Ui_MainWindow.selectedTable = self.listWidget.currentItem().text()
        Ui_MainWindow.sqlQuery1 = ""
        self.plainTextEdit.setPlainText(Ui_MainWindow.sqlQuery1)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)

    def cellClickEvent(self, row, col):
        """ 셀 클릭시 계산값을 보여줌"""
        try:
            clickCellText = self.tableWidget.item(row, col).text()
            self.label_2.setText(clickCellText)
            selected = self.tableWidget.selectedRanges()
            cnt = 0
            tot = []

            for idx, val in enumerate(
                    selected):  # val.columnCount(), val.topRow(), val.leftColumn(), val.bottomRow(), val.rightColumn()
                for i in range(int(val.topRow()), int(val.bottomRow()) + 1):
                    for k in range(int(val.leftColumn()), int(val.rightColumn()) + 1):
                        cnt = cnt + 1
                        value=self.isFloat(self.tableWidget.item(i, k).text())
                        if value:
                            tot.append(value)

            self.label_9.setText(str(cnt))  # 선택 수량
            self.label_11.setText(str(sum(tot)))  # 합계
        except:
            # self.createTable()
            traceback.print_exc()

    def isFloat(self,str):
        """정수, 소수만 소수타입으로 변환해 리턴"""
        basischk=0
        numeric=False
        returnvalue=0
        value=list(str)

        for idx,val in enumerate(value):
            if idx==0:
                if val=='-' or val.isdigit()==True:
                 continue
                else:
                 break
            elif idx==len(value)-1:
                numeric=True
            else:
                if val.isdigit()==True:
                    continue
                elif val=="." and basischk==0:
                    basischk=+1
                    continue
                else:
                    break

        if numeric==True:
            returnvalue=decimal.Decimal(str) # 부동소수점 문제 해결
        return returnvalue

    def createTable(self):
        """ 테이블 컬럼, 로우 수, 컬럼명 설정을 함"""
        try:
            sqlValue = self.searchValue()
            if Ui_MainWindow.selectedTable:
                if sqlValue:
                    header = self.searchColumn()
                    df = pd.DataFrame(sqlValue)
                    df.columns = header
                    df.head()
                    Ui_MainWindow.dfRow = len(df.index)
                    self.tableWidget.setColumnCount(len(df.columns))
                    self.tableWidget.setRowCount(len(df.index))
                    self.tableWidget.setHorizontalHeaderLabels(header)
                    self.setTableData(df)
                    Ui_MainWindow.mainWindow_df = df
                    self.label_2.setText("")
                    self.label_5.setText(Ui_MainWindow.selectedTable)
                    self.label_7.setText(str(Ui_MainWindow.dfRow) + " / 전체:" + self.tableCount())
                    self.label_9.setText("")
                    self.label_11.setText("")
                    self.tableWidget.resizeColumnsToContents()  # 셀 크기를 내용길이와 같게
                    self.pushButton_3.setDisabled(False)
                    self.actpopup()

                else:
                    self.tableWidget.clear()
                    self.tableWidget.setRowCount(0)
                    self.label_2.setText("")
                    self.label_5.setText(Ui_MainWindow.selectedTable)
                    self.label_7.setText("0 / 전체:0")
                    self.label_9.setText("")
                    self.label_11.setText("")
            else:
                self.label_5.setText("없음")
            self.label_2.setText("")
        except:
            traceback.print_exc()

    def tableCount(self):
        """테이블 자료수 조회"""
        sql = "select count(*) from " + Ui_MainWindow.selectedTable
        cur.execute(sql)
        cnt = cur.fetchall()
        a = list(cnt[0])[0]
        return str(a)

    def searchColumn(self):
        """ 테이블 컬럼을 가지고와서 List로 변환해 반환"""
        if Ui_MainWindow.selectedTable:
            str1 = []

            sql = "select column_name from cols where table_name = '" + Ui_MainWindow.selectedTable + "' order by COLUMN_ID ASC"
            cur.execute(sql)
            idx = cur.fetchall()
            for i in range(len(idx)):
                str1.append(''.join(idx[i]))

            return str1

    def searchValue(self):
        """ SQL 값 리턴. 어떤 테이블은 로우수가 1200만개가 넘는 것도 있어서 5만건으로 제한 200만건 넘어가면 에러나면서 컴퓨터 꺼짐 10만건에 1분가량 소요"""
        try:
            row = ""
            subSql = ""
            if self.checkBox.isChecked():
                subSql = Ui_MainWindow.sqlQuery1
            else:
                subSql = ""
            if Ui_MainWindow.selectedTable:  # 값 있는 경우
                sql = "select * from " + Ui_MainWindow.selectedTable + " where 1=1" + subSql
                print("sql:" + sql)
                cur.execute(sql)
                row = cur.fetchmany(Ui_MainWindow.maxSearch)
            else:  # 값 없는 경우
                sql = ""
            return row
        except:
            a = QMessageBox()
            a.setText("데이터 조회 중 오류가 발생했습니다.")
            a.setStandardButtons(QMessageBox.Ok)
            a.exec_()
            traceback.print_exc()

    def setTableData(self, df):
        """for로 돌리면서 표에 값을 입력, Null값 따로 변환안함"""
        try:
            for i in range(len(df.index)):
                for j in range(len(df.columns)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))
        except:
            traceback.print_exc()
    def menuInfo(self):
        """찾기 귀찮아서"""
        os.system('explorer https://codetorial.net/pyqt5/index.html')

    def toExcel(self):
        """엑셀 변환 저장"""
        a = QMessageBox()

        try:
            if Ui_MainWindow.dfRow:
                excelfolder = QFileDialog.getExistingDirectory(self.tab1, '폴더 지정', 'C:\\')
                # excelfolder = QFileDialog.getSaveFileName(self.tab1, "저장","C:\\'", "excel File(*.xlsx)") 파일명 지정은 나중에 구현
                filename = datetime.today().strftime("%Y%m%d%H%M%S")
                excelTitle = (excelfolder + filename + ".xlsx")
                if excelfolder:
                    Ui_MainWindow.mainWindow_df.to_excel(excelTitle) # 엑셀 생성
                    if os.path.exists(excelTitle):
                        a.setText("경로: " + excelTitle + "\n\n엑셀파일 생성 완료")

                    else:
                        a.setText("파일이 생성되지 않았습니다")
                    a.setStandardButtons(QMessageBox.Ok)
                    a.exec_()
            else:
                a.setText("변환할 자료가 없습니다")
                a.setStandardButtons(QMessageBox.Ok)
                a.exec_()
        except:
            a.setText("파일 생성 중 에러가 발생했습니다.")
            a.setStandardButtons(QMessageBox.Ok)
            a.exec_()
            traceback.print_exc()

    # --------------------------------------tab2
    def connectAPI(self):
        """API 받아와서 표에 넣음 key값에 {}는 제거"""

        encodingkey = "3RhwH1vBpJD8wjdiy%2FMMSldNw3i7S4kaVOoZVc7JxOLv30V5WzU0CezVivAIkd0iPHTmYgQc3DcQ76et3Dqsig%3D%3D"
        decodingkey = "3RhwH1vBpJD8wjdiy/MMSldNw3i7S4kaVOoZVc7JxOLv30V5WzU0CezVivAIkd0iPHTmYgQc3DcQ76et3Dqsig=="

        # request 인증키와 항목
        endpoint_service = "http://apis.data.go.kr/B190017/service/GetInsuredProductService202008"
        service = "getProductList202008"  # 서비스명
        pageNo = 1  # 페이지번호
        numOfRows = 800  # 페이지결과 수
        resultType = self.tab2_comboBox.currentText()  # 결과형식 xml/json
        regnNm = ""  # 금융권역
        fncIstNm = ""  # 금융회사명
        prdNm = ""  # 금융상품명

        url = f"{endpoint_service}/{service}?serviceKey={encodingkey}&pageNo={pageNo}&numOfRows={numOfRows}&resultType={resultType}"

        # 사이트, api 전문
        # https://www.data.go.kr/
        # http://apis.data.go.kr/B190017/service/GetInsuredProductService202008/getProductList202008?serviceKey=3RhwH1vBpJD8wjdiy%2FMMSldNw3i7S4kaVOoZVc7JxOLv30V5WzU0CezVivAIkd0iPHTmYgQc3DcQ76et3Dqsig%3D%3D&numOfRows=500&resultType=json
        if resultType == 'xml':
            self.xmlParse(url)
        elif resultType == 'json':
            self.jsonParse(url)
        else:
            traceback.print_exc()

    def xmlParse(self, url):
        """xml 파싱"""
        dict1 = {'회사': [], '상품': [], '등록일': []}
        fncistnm = []
        prdnm = []
        regdate = []

        req = requests.get(url)
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        col1 = soup.findAll("fncistnm")
        col2 = soup.findAll("prdnm")
        col3 = soup.findAll("regdate")
        for i in col1:
            fncistnm.append(i.string)
        for i in col2:
            prdnm.append(i.string)
        for i in col3:
            regdate.append(i.string)
        dict1['회사'] = fncistnm
        dict1['상품'] = prdnm
        dict1['등록일'] = regdate

        df2 = pd.DataFrame(dict1)
        self.tab2_createTable(df2)

    def jsonParse(self, url):
        """ json 파싱 파일 지저분한건 jsonviewer로 보기"""
        dict1 = {'회사': [], '상품': [], '등록일': []}
        fncistnm = []
        prdnm = []
        regdate = []

        response = requests.get(url).json()
        df3 = pd.DataFrame()
        asd = response['getProductList']['item']
        for i in asd:
            fncistnm.append(list(i.values())[2])
            prdnm.append(list(i.values())[4])
            regdate.append(list(i.values())[3])
        dict1['회사'] = fncistnm
        dict1['상품'] = prdnm
        dict1['등록일'] = regdate
        df2 = pd.DataFrame(dict1)
        self.tab2_createTable(df2)

    def tab2_createTable(self, df2):
        """탭2 테이블 제작"""
        self.tab2_tablewidget.setColumnCount(len(df2.columns))
        self.tab2_tablewidget.setRowCount(len(df2.index))
        self.tab2_tablewidget.setHorizontalHeaderLabels(df2.columns)
        for i in range(len(df2.index)):
            for j in range(len(df2.columns)):
                self.tab2_tablewidget.setItem(i, j, QTableWidgetItem(str(df2.iloc[i, j])))
        self.tab2_tablewidget.resizeColumnsToContents()  # 컬럼 크기 조정

    # ---------------------------------------tab3


    def tab3_createTable(self):
        try:
            header = ['기준일','펀드코드','펀드명','수익자','펀드종류구분','펀드유형','공모사모구분','모자구분','종류형구분','펑드구분','적용법률','자통법적용일','최초설정일','다음결산일','상환일','다음보수인출일',
                      '판매보수','운용보수','사무관리보수','수탁보수','펀드평가보수','자산관리보수','상품관리보수','성과보수','성과보수여부','Total','설정액','전일설정좌수','전일총자산','전일순자산','전일기준가','펀드약명',
                      '영문명','운용역','운용사','수탁사','사무관리사','펀드평가사','판매사갯수','판매사','협회표준코드','금감원코드','예탁원펀드코드','예탁원종목코드','상품분류코드','상품분류2차','집합투자기구분류',
                        '펀드결제수수료여부','분배방식','당기결산방식','시가평가여부','장단기구분','국외세액환급여부','이관일','이수일','부사무관리사','해외전용과표가격대상여부','해외전용과표가격적용일',
                      '설정대금확정일1','설정일1','환매대금확정일1','환매일1','환매대금확정일2','환매일','위탁사자체유형','펀드결제수수료면제시작일','펀드결제수수료면제종료일','펀드결제수수료유예시작일',
                      '펀드결제수수료유예종료일','채권평가사보수유예시작일','채권평가사보수유예종료일','수탁사코드','배당기준운용사','신주인수권증서평가기준(폐지일)','공모청약수수료기준','단위형구분','수익차등여부','사모분류',
                      '일반투자자포함여부']
            sqlValue = self.tab3_searchValue()
            df3 = pd.DataFrame(sqlValue)
            df3.columns = header
            df3.head()
            self.tab3_tablewidget.setColumnCount(len(df3.columns))
            self.tab3_tablewidget.setRowCount(len(df3.index))
            self.tab3_tablewidget.setHorizontalHeaderLabels(header)
            self.tab3_setTableData(df3)
            self.tab3_tablewidget.resizeColumnsToContents()  # 컬럼 크기 조정
        except:
            traceback.print_exc()

    def tab3_setTableData(self, df3):
        """for로 돌리면서 표에 값을 입력, Null값 따로 변환안함"""
        try:
            for i in range(len(df3.index)):
                for j in range(len(df3.columns)):
                    self.tab3_tablewidget.setItem(i, j, QTableWidgetItem(str(df3.iloc[i, j])))
        except:
            traceback.print_exc()

    def tab3_searchValue(self):
        """ SQL 값 리턴 값 같은게 여러개 나오는건 정보_운용역담당펀드의 운용역구분코드 컬럼 때문인데 이게 어디와 매칭되는지 몰라서 join 못하고 distinct로 중복처리"""
        try:
            sql = "select distinct b.기준일자 , a.펀드코드, d.위탁사펀드명, "+\
                  "(select listagg(수익자명, ',') as aa from (select 수익자명 from 정보_수익자 f, 펀드_수익자정보 e "+\
                    "where a.펀드코드=e.펀드코드(+) and e.수익자코드=f.수익자코드 group by 수익자명)) as 수익자명"+\
                  ", i.펀드회계유형명, "+\
                  "(select 공통코드값명 from 공통코드 where a.집합투자기구2차분류코드=공통코드값 and 공통코드ID='000418')as 펀드유형,"+ \
                "(select 공통코드값명 from 공통코드 where a.공모사모코드=공통코드값 and 공통코드ID='000222') as 공모사모구분"+\
                ", ''모자구분,"+\
                "'*'종류별구분,"+\
                "''펀드구분, "+\
                 "(select 공통코드값명 from 공통코드 where a.적용법령구분코드=공통코드값 and 공통코드ID='000436') as 적용법률,"+\
                 "자본시장통합법적용일자 as 자통법적용일, 최초설정일자, 다음결산일자, 상환예정일자,다음보수인출일자,c.판매회사보수율,"+\
                 "c.운용회사보수율,사무수탁사보수율,수탁사보수율,펀드평가회사보수율,''자산관리보수,''상품관리보수,성과보수율,성과보수여부,"+\
                 "round(c.판매회사보수율+c.운용회사보수율+사무수탁사보수율+수탁사보수율+펀드평가회사보수율,2),"+\
                 "설정금액,''전일설정좌수,''전일총자산,''전일순자산,''전일기준가,d.위탁사펀드약어명,d.위탁사펀드영문명,"+\
                 "(select listagg(운용역명,', ')"+\
                "   from(select h.운용역명 from 정보_운용역담당펀드 m, 운용역코드 h"+\
                "    where a.펀드코드=b.펀드코드 and m.펀드코드=a.펀드코드 and m.운용역코드=h.운용역코드"+\
                "    group by 운용역명)) as 운용역명,"+\
                " a.운용회사코드 as 운용사, " \
                "a.수탁사코드 as 수탁사" \
                ",g.사무수탁사명 as 사무관리사,''펀드평가사,"+\
                "(select count(*) from 펀드_판매사별실적 where a.펀드코드=펀드코드 and b.기준일자=기준일자) as 판매사갯수,"+\
                "(select listagg(매매처명,', ')  as aa"+\
                "   from("+\
                "    select 펀드판매회사코드,매매처명 from 펀드_판매사별실적 c, 정보_매매처 d"+\
                "    where a.펀드코드=c.펀드코드 and b.기준일자=c.기준일자 and c.펀드판매회사코드=매매처코드"+\
                "    group by 펀드판매회사코드, 매매처명"+\
                "    )) as 판매사"+\
                ",금융투자협회종목코드 as 협회표준코드,금융감독원코드 as 금감원코드,증권예탁원펀드코드 as 예탁원펀드코드,증권예탁원종목코드 as 예탁원종목코드,상품분류코드,"+\
                "''상품분류2차,"+\
                "집합투자기구1차분류코드||집합투자기구2차분류코드||집합투자기구3차분류코드||집합투자기구4차분류코드||집합투자기구5차분류코드||집합투자기구6차분류코드||집합투자기구7차분류코드||"+\
                "집합투자기구8차분류코드||집합투자기구9차분류코드||집합투자기구10차분류코드||"+\
                "집합투자기구11차분류코드||집합투자기구12차분류코드||집합투자기구13차분류코드||집합투자기구14차분류코드||'?' as 집합투자기구분류"+\
                ",펀드결제수수료계상여부,"+\
                " (select 공통코드값명 from 공통코드 where a.분배방법구분코드=공통코드값 and 공통코드ID='000221') as 분배방식,"+\
                " ''당기결산방식,a.시가평가여부,''장단기부분,a.국외세액환급여부,''이관일,''이수일,''부사무관리사,a.해외주식비과표대상여부,a.해외주식비과표적용일자,''설정대금확정일1,''설정일,"+\
                "''환매대금확정일1,''환매일1,''환매대금확정일2,''환매일2,''위탁사자체유형,''펀드결제수수료면제시작일,''펀드결제수수료종료일,''펀드결제수수료유예시작일,''펀드결제수수료유예종료일,"+\
                "''채권평가사보수유예시작일,''채권평가사보수유예종료일,"+\
                "수탁사코드,''배당기준운용사,"+\
                "''신주인수권증서평가기준_폐지일,"+\
                "''공모청약수수료기준,"+\
                "''단위형구분,''수익차등여부,"+\
                "(select 공통코드값명 from 공통코드 where a.사모구분코드=공통코드값 and 공통코드ID='001015') as 사모분류,"+\
                "''일반투자자포함여부 "+\
                "from 펀드_마스터 a ,펀드_기준가격 b, 펀드_보수율 c, 펀드_위탁사별펀드정보 d, 정보_사무수탁사 g,"+\
                " 정보_펀드회계유형 i,"+\
                " 정보_운용역담당펀드 m,"+\
                " 운용역코드 h "+\
                "where a.펀드코드=b.펀드코드 "+\
                "and a.펀드코드=c.펀드코드 "+\
                "and a.펀드코드=d.펀드코드 "+\
                "and a.사무수탁사코드=g.사무수탁사코드 "+\
                "and a.펀드회계유형코드=i.펀드회계유형코드 "+\
                "and m.운용역코드=h.운용역코드 "+\
                "and a.펀드코드=m.펀드코드 "+\
                "and b.기준일자='{}' ".format(self.tab3_dateEdit.text().replace('-', '/'))
            sql+="and c.유효시작일자 <= '{}'".format(self.tab3_dateEdit.text().replace('-', '/'))
            sql+="and c.유효종료일자 >= '{}'".format(self.tab3_dateEdit.text().replace('-', '/'))

            if self.tab3_comboBox_3.currentText()!='전체':
                sql+="and a.펀드코드='{}'".format(self.tab3_comboBox_3.currentText()[:4])
            print("sql:" + sql)
            cur.execute(sql)
            row = cur.fetchmany(Ui_MainWindow.maxSearch)

            return row
        except:
            a = QMessageBox()
            a.setText("데이터 조회 중 오류가 발생했습니다.")
            a.setStandardButtons(QMessageBox.Ok)
            a.exec_()
            traceback.print_exc()


    def settab3_comboBox_3(self):
        """펀드코드 세팅"""
        fundList=("1944","ER11","1033","1275")
        self.tab3_comboBox_3.addItem('전체')
        sql = "select 위탁사펀드코드, 위탁사펀드명 from 펀드_위탁사별펀드정보 where 위탁사펀드코드 in "+ str(fundList)
        cur.execute(sql)
        cnt = cur.fetchall()
        for val1,val2 in cnt:
            self.tab3_comboBox_3.addItem(val1+"::"+val2)


# 메인
if __name__ == '__main__':
    conn = cx_Oracle.connect("system", "1234", "localhost:1521/xe")
    cur = conn.cursor()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# conn = cx_Oracle.connect("HKCL", "hkcl", "11.10.5.11:1521/hkfund")
# excelTitle = (r"C:\Users\User\Desktop/" + fileName + ".xlsx")
# pyuic5 -x mainFrame.ui -o mainFrame.py
# pyuic5 -x windowGraphic.ui -o windowGraphic.py
# pyuic5 -x windowQuery.ui -o windowQuery.py
# ModuleNotFoundError: No module named 'requests': 파이참에 깔아도 위치가 다른게 딸려서 인식 못 하는거니 파이썬/scripts에 가서 pip로 requests 설치
# 파이썬창에서 import requests를 치면 반응이 없고 그냥 requests를 쳤을 때 에러가 아니고 다른게 나오면 설치된거. 다른것도 마찬가지
