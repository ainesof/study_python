# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import os.path
import re
import cx_Oracle
import pandas as pd
import sys
import requests
import bs4
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from datetime import datetime
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1256, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1241, 660))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(250, 600, 151, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(180, 30, 1051, 560))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(510, 10, 331, 21))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(260, 10, 191, 21))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(180, 600, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(400, 600, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(500, 600, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(460, 10, 41, 21))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(1150, 0, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(180, 10, 71, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(100, 0, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 260, 171, 71))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(0, 30, 171, 192))
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 2, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 230, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 230, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1256, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(True)
        self.label_6.setText(_translate("MainWindow", "조회 데이터:"))
        self.label.setText(_translate("MainWindow", "선택값:"))
        self.label_8.setText(_translate("MainWindow", "인덱스:"))
        self.label_9.setText(_translate("MainWindow", "합계:"))
        self.pushButton_2.setText(_translate("MainWindow", "엑셀 변환"))
        self.label_4.setText(_translate("MainWindow", "검색테이블: "))
        self.pushButton.setText(_translate("MainWindow", "조회"))
        self.label_3.setText(_translate("MainWindow", "DB리스트"))
        self.pushButton_3.setText(_translate("MainWindow", "조건검색"))
        self.pushButton_4.setText(_translate("MainWindow", "그래프"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "데이터 조회"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "API 조회연습"))

        # 탭2
        self.tab2_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.tab2_pushbutton.setGeometry(QtCore.QRect(100, 5, 71, 23))
        self.tab2_pushbutton.setObjectName("tab2_pushbutton")
        self.tab2_pushbutton.setText(_translate("tab2MainWindow", "조회"))
        self.tab2_tablewidget = QtWidgets.QTableWidget(self.tab_2)
        self.tab2_tablewidget.setGeometry(QtCore.QRect(180, 30, 1051, 560))
        self.tab2_tablewidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab2_tablewidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab2_tablewidget.setAlternatingRowColors(True)
        self.tab2_tablewidget.setObjectName("tab2_tablewidget")
        self.tab2_tablewidget.setColumnCount(0)
        self.tab2_tablewidget.setRowCount(0)
        self.tab2_tablewidget.setSortingEnabled(True)
        self.tab2_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.tab2_lineEdit.setGeometry(QtCore.QRect(0, 75, 60, 21))
        self.tab2_lineEdit.setObjectName("tab2_lineEdit")
        self.tab2_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.tab2_comboBox.setGeometry(QtCore.QRect(0, 5, 50, 21))
        self.tab2_comboBox.setObjectName("tab2_comboBox")
        self.tab2_comboBox.addItem('xml')
        self.tab2_comboBox.addItem('json')

        self.tab2_pushbutton.clicked.connect(self.connectAPI)

        # 클래스 변수
        Ui_MainWindow.selectedTable="" # DB리스트 선택값
        Ui_MainWindow.dfRow=0 # 검색된 자료 row
        Ui_MainWindow.mainWindow_df="" # 메인 자료값 df
        Ui_MainWindow.sqlQuery1="" # 추가 조건
        Ui_MainWindow.maxSearch=100000 # 최대 조회가능 숫자

        # Qt디자이너 외 구현
        self.setListWidget() # DB리스트 생성
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) # 내용수정 금지
        self.tab1_newWindow1 = QDialog() # 검색조건 팝업창
        self.tab1_newWindow2 = QDialog() # 그래픽부분 팝업창
        self.pushButton_3.setDisabled(True)

        # 이벤트
        self.pushButton.clicked.connect(self.createTable)  # 조회 버튼 createTable
        self.pushButton_2.clicked.connect(self.toExcel)  # 엑셀변환 버튼
        self.tableWidget.cellClicked.connect(self.cellClickEvent) # 표 클릭시 발생 이벤트
        self.tableWidget.currentCellChanged.connect(self.cellClickEvent)  # 표 클릭시 발생 이벤트
        self.listWidget.currentItemChanged.connect(self.clickListWidget) # DB리스트 클릭시 발생 이벤트
        self.listWidget.doubleClicked.connect(self.createTable) # DB리스트 더블클릭시 발생 이벤트
        self.pushButton_3.clicked.connect(self.windowQuery) # 검색조건 추가 버튼
        self.pushButton_4.clicked.connect(self.windowGraphic)  # 검색조건 추가 버튼

    def windowGraphic(self):
        """그래프 차트 창 """

        self.tab1_newWindow2.setWindowTitle("그래프")
        self.tab1_newWindow2.setGeometry(100, 200, 600, 400)
        self.tab1_win2verticalLayoutWidget = QtWidgets.QWidget(self.tab1_newWindow2)
        self.tab1_win2verticalLayoutWidget.setGeometry(QtCore.QRect(300, 0, 300, 400))
        self.tab1_win2verticalLayoutWidget.setObjectName("tab1_win2verticalLayoutWidget")

        # 예제
        Players = "SAMSUNG", "LG", "Apple", "HP"  # 차트의 항목 이름
        Score = [45, 30, 15, 10]  # 차트의 퍼센트
        explode = (0.1, 0, 0, 0)  # 차트의 간격 부분으로 0끼리는 붙어있음

        canvas = FigureCanvas(Figure(figsize=(1, 1)))
        vbox = QVBoxLayout(self.tab1_win2verticalLayoutWidget)
        vbox.addWidget(canvas)

        # 툴바 추가가 안됨
        # self.tab1_win2verticalLayoutWidget.addToolBar(NavigationToolbar(canvas, self.tab1_win2verticalLayoutWidget))
        self.tab1_win2verticalLayoutWidget.ax = canvas.figure.subplots()
        self.tab1_win2verticalLayoutWidget.ax.pie(Score, explode=explode, labels=Players, autopct="%1.1f%%", shadow=True, startangle=90)
        self.tab1_win2verticalLayoutWidget.ax.axis("equal")

        self.tab1_newWindow2.setWindowModality(QtCore.Qt.ApplicationModal) # 하위창 컨트롤 금지
        self.tab1_newWindow2.show()




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
        self.tab1_newWindow1.sqlQuery=""
        self.tab1_newWindow1.setWindowTitle("조건검색창")
        self.tab1_newWindow1.setWindowModality(QtCore.Qt.ApplicationModal) # 하위창 컨트롤 금지
        self.tab1_newWindow1.resize(426, 298)
        self.tab1_win1pushButton.setDisabled(False) # 쿼리추가 버튼 비활성화
        self.setCombobox()
        self.tab1_newWindow1.show()


        # 이벤트
        self.tab1_win1pushButton.clicked.connect(self.submitQuery) # 확인버튼 누를시
        self.tab1_win1checkBox.stateChanged.connect(self.ableQuery1) # 체크박스 변화시
        self.tab1_win1checkBox_2.stateChanged.connect(self.ableQuery2)

    #   -------------------------------------------newwindow1

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
        sql1=""
        sql2=""
        if self.tab1_win1lineEdit.text()=="":
            self.tab1_win1lineEdit.setEnabled(False)
            self.tab1_win1checkBox.setChecked(False)
        else:
            sql1=self.setQuery(self.tab1_win1comboBox.currentText(),self.tab1_win1comboBox_3.currentIndex(),self.tab1_win1lineEdit.text())
        if self.tab1_win1lineEdit_2.text()=="":
            self.tab1_win1lineEdit_2.setEnabled(False)
            self.tab1_win1checkBox_2.setChecked(False)
        else:
            sql2=self.setQuery(self.tab1_win1comboBox_2.currentText(),self.tab1_win1comboBox_4.currentIndex(),self.tab1_win1lineEdit_2.text())
        Ui_MainWindow.sqlQuery1=sql1+sql2
        # self.lineEdit.setText(Ui_MainWindow.sqlQuery1.replace("and ","",1))
        self.plainTextEdit.setPlainText(Ui_MainWindow.sqlQuery1.replace("and ","",1))
        self.createTable()
        self.tab1_newWindow1.close()

    def setQuery(self,columnText,i,lineEditText):
        """ 조건을 설정해 SQL에 추가 """
        str1=[ " like '%"," = '", " != '", " <= '", " >= '"]
        str2=["%'","'"]
        sql=" and "+columnText+str1[i]+lineEditText+str2[math.trunc((i+9)/10)]
        return sql

    def setCombobox(self):
        """ 콤보박스값들 설정 """
        comboList=["부분일치","일치","제외","이상","이하"]
        for i in comboList:
            self.tab1_win1comboBox_3.addItem(i)
            self.tab1_win1comboBox_4.addItem(i)
        for i in Ui_MainWindow.mainWindow_df.columns.values.tolist():
            self.tab1_win1comboBox.addItem(i)
            self.tab1_win1comboBox_2.addItem(i)

    #   -------------------------------------------tab1


    def setListWidget(self):
        """ 왼쪽 리스트에 DB리스트 생성. 리스트는 하드코딩 약 8만건 기준 조회시간 30초 """
        dbList = ["TB","ASD","INCOME","증권회사","지급보증","공공기관","공공기관21"]
        self.listWidget.addItems(dbList)

    def clickListWidget(self):
        """ DB리스트 클릭시 클래스 변수에 값을 저장 """
        Ui_MainWindow.selectedTable=self.listWidget.currentItem().text()
        Ui_MainWindow.sqlQuery1 = ""
        self.plainTextEdit.setPlainText(Ui_MainWindow.sqlQuery1)
        # self.lineEdit.setText(Ui_MainWindow.sqlQuery1)
        self.pushButton_3.setDisabled(True)

    def cellClickEvent(self,row,col):
        """ 셀 클릭값 받아오기 문자에 숫자 껴있는건 맨 앞 숫자만 다 가져옴, 음수 소수점 식별 불가"""
        try:
            clickCellText=self.tableWidget.item(row, col).text()
            self.label_2.setText(clickCellText)
            selected=self.tableWidget.selectedRanges()
            cnt=0
            tot=[]

            for idx, val in enumerate(selected): # val.columnCount(), val.topRow(), val.leftColumn(), val.bottomRow(), val.rightColumn()
                for i in range(int(val.topRow()), int(val.bottomRow())+1):
                    for k in range(int(val.leftColumn()), int(val.rightColumn())+1):
                        cnt=cnt+1
                        value=re.findall("\d+",self.tableWidget.item(i, k).text())
                        if value:
                            tot.append(int(value[0]))

            self.label_8.setText(str(cnt)) # 선택 수량
            self.label_9.setText(str(sum(tot))) # 합계
        except:
            self.createTable()
            print("cellClickEvent 에러")

    def createTable(self):
        """ 테이블 컬럼, 로우 수, 컬럼명 설정을 함
        :return: Dataframe타입 조회값 """
        sqlValue=self.searchValue()
        if Ui_MainWindow.selectedTable:
            if sqlValue:
                header=self.searchColumn()
                df = pd.DataFrame(sqlValue)
                df.columns=header
                self.tableCount()
                Ui_MainWindow.dfRow=len(df.index)
                self.tableWidget.setColumnCount(len(df.columns))
                self.tableWidget.setRowCount(len(df.index))
                self.tableWidget.setHorizontalHeaderLabels(header)
                self.setTableData(df)
                Ui_MainWindow.mainWindow_df = df
                self.label_5.setText(Ui_MainWindow.selectedTable)
                self.label_7.setText(str(Ui_MainWindow.dfRow)+" / 전체:"+self.tableCount())
                self.tableWidget.resizeColumnsToContents() # 셀 크기를 내용길이와 같게
                self.pushButton_3.setDisabled(False)
            else:
                self.tableWidget.clear()
                self.tableWidget.setRowCount(0)
                self.label_5.setText("조회값 없음")
        else:
            self.label_5.setText("없음")
        self.label_2.setText("")

    def tableCount(self):
        """테이블 자료수 조회"""
        sql="select count(*) from "+Ui_MainWindow.selectedTable
        cur.execute(sql)
        cnt = cur.fetchall()
        a=list(cnt[0])[0]
        return str(a)

    def searchColumn(self):
        """ 테이블 컬럼을 가지고와서 List로 변환
        :return List타입 컬럼명들
        """
        if Ui_MainWindow.selectedTable:
            str1=[]

            sql = "select column_name from cols where table_name = '"+Ui_MainWindow.selectedTable+"'"
            cur.execute(sql)
            idx = cur.fetchall()
            for i in range(len(idx)):
                str1.append(''.join(idx[i]))
            return str1

    def searchValue(self):
        """ SQL 값 리턴. 어떤 테이블은 로우수가 1200만개가 넘는 것도 있어서 5만건으로 제한 200만건 넘어가면 에러나면서 컴퓨터 꺼짐 10만건에 1분가량 소요
        :return: Dataframe타입 SQL조회값"""
        try:
            row=""
            if Ui_MainWindow.selectedTable: #값 있는 경우
                sql = "select * from "+Ui_MainWindow.selectedTable+" where 1=1"+Ui_MainWindow.sqlQuery1
                print("sql:"+sql)
                cur.execute(sql)
                row = cur.fetchmany(Ui_MainWindow.maxSearch)
            else: #값 없는 경우
                sql = ""
            return row
        except:
            a = QMessageBox()
            a.setText("데이터 조회 중 오류가 발생했습니다.")
            a.setStandardButtons(QMessageBox.Ok)
            a.exec_()
            print("searchValue 에러")
            
    def setTableData(self, df):
        """for로 돌리면서 표에 값을 입력, Null값 따로 처리안함"""
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))

    def toExcel(self):
        """엑셀 변환. 에러로그 없이 꺼지면 지정된 저장경로 관련 문제"""
        a = QMessageBox()
        try:
            if Ui_MainWindow.dfRow:
                fileName=datetime.today().strftime("%Y%m%d%H%M%S")

                excelTitle=(r"C:\Users\User\Desktop/"+fileName+".xlsx")
                Ui_MainWindow.mainWindow_df.to_excel(excelTitle)

                if os.path.exists(excelTitle):
                    a.setText("경로: "+excelTitle+"\n\n엑셀파일 생성 완료")
                else:
                    a.setText("파일이 생성되지 않았습니다")
                a.setStandardButtons(QMessageBox.Ok)
            else:
                a.setText("변환할 자료가 없습니다")
                a.setStandardButtons(QMessageBox.Ok)
            a.exec_()
        except:
            a.setText("파일 생성 중 에러가 발생했습니다.")
            a.setStandardButtons(QMessageBox.Ok)
            a.exec_()
            print("toExcel 에러")
        # --------------------------------------tab2

    def connectAPI(self):
        """API 받아와서 표에 넣음 key값에 {}는 제거"""

        encodingkey="3RhwH1vBpJD8wjdiy%2FMMSldNw3i7S4kaVOoZVc7JxOLv30V5WzU0CezVivAIkd0iPHTmYgQc3DcQ76et3Dqsig%3D%3D"
        decodingkey="3RhwH1vBpJD8wjdiy/MMSldNw3i7S4kaVOoZVc7JxOLv30V5WzU0CezVivAIkd0iPHTmYgQc3DcQ76et3Dqsig=="

        # request 인증키와 항목
        endpoint_service="http://apis.data.go.kr/B190017/service/GetInsuredProductService202008"
        service="getProductList202008" # 서비스명
        pageNo=1 # 페이지번호
        numOfRows=800 # 페이지결과 수
        resultType=self.tab2_comboBox.currentText() # 결과형식 xml/json
        regnNm="" # 금융권역
        fncIstNm="" # 금융회사명
        prdNm="" # 금융상품명

        url=f"{endpoint_service}/{service}?serviceKey={encodingkey}&pageNo={pageNo}&numOfRows={numOfRows}&resultType={resultType}"

        # 사이트, api 전문
        # https://www.data.go.kr/
        # http://apis.data.go.kr/B190017/service/GetInsuredProductService202008/getProductList202008?serviceKey=3RhwH1vBpJD8wjdiy%2FMMSldNw3i7S4kaVOoZVc7JxOLv30V5WzU0CezVivAIkd0iPHTmYgQc3DcQ76et3Dqsig%3D%3D&numOfRows=500&resultType=json
        if resultType=='xml':
            self.xmlParse(url)
        elif resultType=='json':
            self.jsonParse(url)
        else:
            print("??")

    def xmlParse(self,url):
        """xml 파싱"""
        dict1={'회사':[],'상품':[],'등록일':[]}
        fncistnm = []
        prdnm = []
        regdate = []

        req=requests.get(url)
        soup=bs4.BeautifulSoup(req.text, "html.parser")
        col1 = soup.findAll("fncistnm")
        col2 = soup.findAll("prdnm")
        col3 = soup.findAll("regdate")
        for i in col1:
            fncistnm.append(i.string)
        for i in col2:
            prdnm.append(i.string)
        for i in col3:
            regdate.append(i.string)
        dict1['회사']=fncistnm
        dict1['상품'] = prdnm
        dict1['등록일'] = regdate

        df2=pd.DataFrame(dict1)
        self.tab2createTable(df2)

    def jsonParse(self,url):
        """ json 파싱 파일 지저분한건 jsonviewer로 보기"""
        dict1 = {'회사': [], '상품': [], '등록일': []}
        fncistnm = []
        prdnm = []
        regdate = []

        response = requests.get(url).json()
        df3=pd.DataFrame()
        asd=response['getProductList']['item']
        for i in asd:
            fncistnm.append(list(i.values())[2])
            prdnm.append(list(i.values())[4])
            regdate.append(list(i.values())[3])
        dict1['회사']=fncistnm
        dict1['상품'] = prdnm
        dict1['등록일'] = regdate
        df2 = pd.DataFrame(dict1)
        self.tab2createTable(df2)

    def tab2createTable(self,df2):
        """탭2 테이블 제작"""
        self.tab2_tablewidget.setColumnCount(len(df2.columns))
        self.tab2_tablewidget.setRowCount(len(df2.index))
        self.tab2_tablewidget.setHorizontalHeaderLabels(df2.columns)
        print("~~~")
        for i in range(len(df2.index)):
            for j in range(len(df2.columns)):
                self.tab2_tablewidget.setItem(i, j, QTableWidgetItem(str(df2.iloc[i, j])))
        self.tab2_tablewidget.resizeColumnsToContents() # 컬럼 크기 조정

# 메인
if __name__ == '__main__':
    dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
    conn = cx_Oracle.connect("system", "1234")
    cur = conn.cursor()
    app=QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# dbList = ["FS_펀드속성코드정보", "FS_시장지수코드정보", "FS_운용사정보", "공통코드", "FS_매입_환매거래정보", "FS_운용사유형별지표및성과분석"]
#      conn = cx_Oracle.connect("HKCL", "hkcl", "11.10.5.11:1521/hkfund")
# excelTitle = (r"C:\Users\User\Desktop/" + fileName + ".xlsx")
# pyuic5 -x naver.ui -o naver.py
# ModuleNotFoundError: No module named 'requests': 파이참에 깔아도 위치가 다른게 딸려서 인식 못 하는거니 파이썬/scripts에 가서 pip로 requests 설치
# 파이썬창에서 import requests를 치면 반응이 없고 그냥 requests를 쳤을 때 에러가 아니고 다른게 나오면 설치된거. 다른것도 마찬가지