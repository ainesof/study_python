# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os.path

import cx_Oracle
import pandas as pd
import sys
from datetime import datetime
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
      MainWindow.setObjectName("MainWindow")
      MainWindow.resize(1379, 847)
      self.centralwidget = QtWidgets.QWidget(MainWindow)
      self.centralwidget.setObjectName("centralwidget")
      self.pushButton = QtWidgets.QPushButton(self.centralwidget)
      self.pushButton.setGeometry(QtCore.QRect(110, 20, 75, 23))
      self.pushButton.setObjectName("pushButton")
      self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
      self.lineEdit.setGeometry(QtCore.QRect(10, 250, 113, 20))
      self.lineEdit.setObjectName("lineEdit")
      self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
      self.pushButton_2.setGeometry(QtCore.QRect(1280, 20, 75, 23))
      self.pushButton_2.setObjectName("pushButton_2")
      self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
      self.tableWidget.setGeometry(QtCore.QRect(290, 50, 1071, 711))
      self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
      self.tableWidget.setObjectName("tableWidget")
      self.tableWidget.setColumnCount(0)
      self.tableWidget.setRowCount(0)
      self.label = QtWidgets.QLabel(self.centralwidget)
      self.label.setGeometry(QtCore.QRect(560, 30, 41, 21))
      self.label.setObjectName("label")
      self.label_2 = QtWidgets.QLabel(self.centralwidget)
      self.label_2.setGeometry(QtCore.QRect(610, 30, 261, 21))
      self.label_2.setText("")
      self.label_2.setObjectName("label_2")
      self.label_3 = QtWidgets.QLabel(self.centralwidget)
      self.label_3.setGeometry(QtCore.QRect(10, 22, 81, 20))
      font = QtGui.QFont()
      font.setFamily("-윤고딕110")
      font.setPointSize(12)
      self.label_3.setFont(font)
      self.label_3.setObjectName("label_3")
      self.listWidget = QtWidgets.QListWidget(self.centralwidget)
      self.listWidget.setGeometry(QtCore.QRect(10, 50, 171, 192))
      self.listWidget.setObjectName("listWidget")
      self.label_4 = QtWidgets.QLabel(self.centralwidget)
      self.label_4.setGeometry(QtCore.QRect(290, 30, 71, 21))
      self.label_4.setObjectName("label_4")
      self.label_5 = QtWidgets.QLabel(self.centralwidget)
      self.label_5.setGeometry(QtCore.QRect(360, 30, 191, 21))
      self.label_5.setText("")
      self.label_5.setObjectName("label_5")
      MainWindow.setCentralWidget(self.centralwidget)
      self.menubar = QtWidgets.QMenuBar(MainWindow)
      self.menubar.setGeometry(QtCore.QRect(0, 0, 1379, 21))
      self.menubar.setObjectName("menubar")
      MainWindow.setCentralWidget(self.centralwidget)
      self.menubar = QtWidgets.QMenuBar(MainWindow)
      self.menubar.setGeometry(QtCore.QRect(0, 0, 1379, 21))
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
      self.pushButton.setText(_translate("MainWindow", "조회"))
      self.pushButton_2.setText(_translate("MainWindow", "엑셀 변환"))
      self.tableWidget.setSortingEnabled(True)
      self.label.setText(_translate("MainWindow", "선택값:"))
      self.label_3.setText(_translate("MainWindow", "DB리스트"))
      self.label_4.setText(_translate("MainWindow", "검색테이블: "))



    # 클래스 변수
      Ui_MainWindow.selectedTable="" # DB리스트 선택값
      Ui_MainWindow.dfRow=0 # 검색된 자료 row
      Ui_MainWindow.mainWindow_df="" # 메인 자료값 df

    # Qt디자이너 외 구현
      self.setListWidget()
      self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) # 내용수정 금지

     # 버튼클릭 이벤트
      self.pushButton.clicked.connect(self.createTable)  # 조회 버튼
      self.pushButton_2.clicked.connect(lambda: self.toExcel())  # 엑셀변환 버튼
      self.tableWidget.cellClicked.connect(self.cellClickEvent) # 표 클릭시 발생 이벤트
      self.listWidget.currentItemChanged.connect(self.clickListWidget) # DB리스트 클릭시 발생 이벤트
      self.listWidget.doubleClicked.connect(self.createTable) # DB리스트 더블클릭시 발생 이벤트

    def setListWidget(self):
      """ 왼쪽 리스트에 DB리스트 생성
      리스트는 하드코딩 약 8만건 기준 조회시간 30초, 약 400만건 기준 조회시간
      """
      dbList=["ASD","TB"]
      self.listWidget.addItems(dbList)

    def clickListWidget(self):
      """ DB리스트 클릭시 클래스 변수에 값을 저장
      """
      Ui_MainWindow.selectedTable=self.listWidget.currentItem().text()

    def cellClickEvent(self,row,col):
      """ 셀 클릭값 받아오기
      """
      clickCellText=self.tableWidget.item(row, col).text()
      self.label_2.setText(clickCellText)

    def createTable(self):
      """ 테이블 설정
      테이블 컬럼, 로우 수, 컬럼명 설정을 함
      :return: Dataframe타입 조회값
      """
      if Ui_MainWindow.selectedTable:
        df = pd.DataFrame(self.searchValue())
        Ui_MainWindow.dfRow=len(df.index)
        self.tableWidget.setColumnCount(len(df.columns))
        self.tableWidget.setRowCount(len(df.index))
        self.tableWidget.setHorizontalHeaderLabels(self.searchColumn())
        self.setTableData(df)
        Ui_MainWindow.mainWindow_df = df
        self.label_5.setText(Ui_MainWindow.selectedTable)
      else:
        self.label_5.setText("없음")

    def searchColumn(self):
      """ SQL 컬럼명 리턴
      테이블 컬럼을 가지고와서 List로 변환
      :return List타입 컬럼명들
      """
      if Ui_MainWindow.selectedTable:
          str1=[]

          sql = "select column_name from user_tab_columns where table_name = '"+Ui_MainWindow.selectedTable+"'"
          cur.execute(sql)
          idx = cur.fetchall()
          for i in range(len(idx)):
           str1.append(''.join(idx[i]))
          return str1

    def searchValue(self):
      """ SQL 값 리턴
      어떤 테이블은 로우수가 1200만개가 넘는 것도 있으니 주의
      :return: Dataframe타입 SQL조회값
      """
      row=""
      if Ui_MainWindow.selectedTable: #값 있는 경우
        sql = "select * from "+Ui_MainWindow.selectedTable
        cur.execute(sql)
        row = cur.fetchall()
      else: #값 없는 경우
        sql = ""

      return row

    def setTableData(self, df):
      """조회값 입력
      for로 돌리면서 값을 입력
      :param df: dataframe타입 SQL조회값
      """
      for i in range(len(df.index)):
        for j in range(len(df.columns)):
         self.tableWidget.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))

    def toExcel(self):
      """엑셀 변환 에러로그 없이 꺼지면 지정된 저장경로 관련 문제
      """
      a = QMessageBox()
      if Ui_MainWindow.dfRow:
          fileName=datetime.today().strftime("%Y%m%d%H%M%S")

          excelTitle=(r"C:\\"+fileName+".xlsx")
          Ui_MainWindow.mainWindow_df.to_excel(excelTitle)

          if os.path.exists(excelTitle):
           a.setText("경로: "+excelTitle+"\n\n엑셀파일 생성 완료")
          else:
           a.setText("엑셀생성 실패")
          a.setStandardButtons(QMessageBox.Ok)
      else:
          a.setText("변환할 자료가 없습니다")
          a.setStandardButtons(QMessageBox.Ok)
      a.exec_()

 # 메인
if __name__ == '__main__':
 # conn = cx_Oracle.connect("HKCL", "hkcl", "11.10.5.11:1521/hkfund")
 dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
 conn = cx_Oracle.connect("system", "1234")
 cur = conn.cursor()
 app=QtWidgets.QApplication(sys.argv)
 MainWindow = QtWidgets.QMainWindow()
 ui = Ui_MainWindow()
 ui.setupUi(MainWindow)
 MainWindow.show()
 sys.exit(app.exec_())


