# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import math, decimal, os.path, sys, traceback
import cx_Oracle, query
import time
import matplotlib.pyplot as plt
import pandas as pd
import requests, bs4
import multiprocessing as mp
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import date, timedelta
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 리소스 상대경로로 변환용
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class process(mp.Process):
    """멀티프로세싱 테스트"""
    def __init__(self,id):
        super(process, self).__init__()
        self.id=id

    def run(self):
        print('...//?')

class Ui_MainWindow(object):
    def __init__(self):
        self.fig = plt.Figure()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 751, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")
        self.tab5_tableWidget = QtWidgets.QTableWidget(self.tab5)
        self.tab5_tableWidget.setGeometry(QtCore.QRect(0, 80, 741, 381))
        self.tab5_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab5_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab5_tableWidget.setAlternatingRowColors(True)
        self.tab5_tableWidget.setObjectName("tab5_tableWidget")
        self.tab5_tableWidget.setColumnCount(0)
        self.tab5_tableWidget.setRowCount(0)
        self.tab5_dateEdit = QtWidgets.QDateEdit(self.tab5)
        self.tab5_dateEdit.setGeometry(QtCore.QRect(50, 10, 91, 22))
        self.tab5_dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab5_dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.tab5_dateEdit.setCalendarPopup(True)
        self.tab5_dateEdit.setObjectName("tab5_dateEdit")
        self.tab5_label = QtWidgets.QLabel(self.tab5)
        self.tab5_label.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.tab5_label.setObjectName("tab5_label")
        self.tab5_label_2 = QtWidgets.QLabel(self.tab5)
        self.tab5_label_2.setGeometry(QtCore.QRect(687, 60, 61, 21))
        self.tab5_label_2.setObjectName("tab5_label_2")
        self.tab5_label_3 = QtWidgets.QLabel(self.tab5)
        self.tab5_label_3.setGeometry(QtCore.QRect(650, 540, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab5_label_3.setFont(font)
        self.tab5_label_3.setText("")
        self.tab5_label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab5_label_3.setObjectName("tab5_label_3")
        self.tab5_pushButton = QtWidgets.QPushButton(self.tab5)
        self.tab5_pushButton.setGeometry(QtCore.QRect(690, 0, 51, 21))
        self.tab5_pushButton.setObjectName("tab5_pushButton")
        self.tab5_label_4 = QtWidgets.QLabel(self.tab5)
        self.tab5_label_4.setGeometry(QtCore.QRect(190, 50, 91, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(11)
        self.tab5_label_4.setFont(font)
        self.tab5_label_4.setObjectName("tab5_label_4")
        self.tab5_label_5 = QtWidgets.QLabel(self.tab5)
        self.tab5_label_5.setGeometry(QtCore.QRect(520, 50, 91, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(11)
        self.tab5_label_5.setFont(font)
        self.tab5_label_5.setObjectName("tab5_label_5")
        self.tabWidget.addTab(self.tab5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setEnabled(True)
        self.tab1.setObjectName("tab1")
        self.tab1_label_7 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_7.setGeometry(QtCore.QRect(250, 430, 181, 20))
        self.tab1_label_7.setText("")
        self.tab1_label_7.setObjectName("tab1_label_7")
        self.tab1_tableWidget = QtWidgets.QTableWidget(self.tab1)
        self.tab1_tableWidget.setGeometry(QtCore.QRect(180, 30, 561, 381))
        self.tab1_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab1_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab1_tableWidget.setAlternatingRowColors(True)
        self.tab1_tableWidget.setObjectName("tab1_tableWidget")
        self.tab1_tableWidget.setColumnCount(0)
        self.tab1_tableWidget.setRowCount(0)
        self.tab1_label_2 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_2.setGeometry(QtCore.QRect(450, 410, 171, 21))
        self.tab1_label_2.setText("")
        self.tab1_label_2.setObjectName("tab1_label_2")
        self.tab1_label_5 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_5.setGeometry(QtCore.QRect(250, 410, 181, 21))
        self.tab1_label_5.setText("")
        self.tab1_label_5.setObjectName("tab1_label_5")
        self.tab1_label_6 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_6.setGeometry(QtCore.QRect(180, 430, 71, 21))
        self.tab1_label_6.setObjectName("tab1_label_6")
        self.tab1_label = QtWidgets.QLabel(self.tab1)
        self.tab1_label.setGeometry(QtCore.QRect(430, 410, 21, 21))
        self.tab1_label.setObjectName("tab1_label")
        self.tab1_pushButton_2 = QtWidgets.QPushButton(self.tab1)
        self.tab1_pushButton_2.setGeometry(QtCore.QRect(666, 4, 75, 23))
        self.tab1_pushButton_2.setObjectName("tab1_pushButton_2")
        self.tab1_label_4 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_4.setGeometry(QtCore.QRect(180, 410, 71, 21))
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
        self.tab1_label_8.setGeometry(QtCore.QRect(430, 430, 31, 21))
        self.tab1_label_8.setObjectName("tab1_label_8")
        self.tab1_label_9 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_9.setGeometry(QtCore.QRect(470, 430, 51, 21))
        self.tab1_label_9.setText("")
        self.tab1_label_9.setObjectName("tab1_label_9")
        self.tab1_label_10 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_10.setGeometry(QtCore.QRect(530, 430, 41, 21))
        self.tab1_label_10.setObjectName("tab1_label_10")
        self.tab1_label_11 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_11.setGeometry(QtCore.QRect(570, 430, 141, 21))
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
        self.tab1_label_13.setGeometry(QtCore.QRect(671, 410, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab1_label_13.setFont(font)
        self.tab1_label_13.setText("")
        self.tab1_label_13.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab1_label_13.setObjectName("tab1_label_13")
        self.tab1_pushButton_5 = QtWidgets.QPushButton(self.tab1)
        self.tab1_pushButton_5.setGeometry(QtCore.QRect(261, 2, 61, 21))
        self.tab1_pushButton_5.setText("")
        self.tab1_pushButton_5.setObjectName("tab1_pushButton_5")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tab2_pushbutton = QtWidgets.QPushButton(self.tab2)
        self.tab2_pushbutton.setGeometry(QtCore.QRect(690, 5, 51, 23))
        self.tab2_pushbutton.setObjectName("tab2_pushbutton")
        self.tab2_tableWidget = QtWidgets.QTableWidget(self.tab2)
        self.tab2_tableWidget.setGeometry(QtCore.QRect(0, 30, 741, 411))
        self.tab2_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab2_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab2_tableWidget.setAlternatingRowColors(True)
        self.tab2_tableWidget.setObjectName("tab2_tableWidget")
        self.tab2_tableWidget.setColumnCount(0)
        self.tab2_tableWidget.setRowCount(0)
        self.tab2_comboBox = QtWidgets.QComboBox(self.tab2)
        self.tab2_comboBox.setGeometry(QtCore.QRect(20, 0, 61, 22))
        self.tab2_comboBox.setObjectName("tab2_comboBox")
        self.tab2_label = QtWidgets.QLabel(self.tab2)
        self.tab2_label.setGeometry(QtCore.QRect(670, 470, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab2_label.setFont(font)
        self.tab2_label.setText("")
        self.tab2_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab2_label.setObjectName("tab2_label")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.tab3_pushButton = QtWidgets.QPushButton(self.tab3)
        self.tab3_pushButton.setGeometry(QtCore.QRect(690, 90, 51, 21))
        self.tab3_pushButton.setObjectName("tab3_pushButton")
        self.tab3_tableWidget = QtWidgets.QTableWidget(self.tab3)
        self.tab3_tableWidget.setGeometry(QtCore.QRect(0, 120, 741, 321))
        self.tab3_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab3_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab3_tableWidget.setAlternatingRowColors(True)
        self.tab3_tableWidget.setObjectName("tab3_tableWidget")
        self.tab3_tableWidget.setColumnCount(0)
        self.tab3_tableWidget.setRowCount(0)
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
        self.tab3_label_4.setGeometry(QtCore.QRect(300, 10, 151, 21))
        self.tab3_label_4.setObjectName("tab3_label_4")
        self.tab3_label_5 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_5.setGeometry(QtCore.QRect(590, 10, 51, 21))
        self.tab3_label_5.setObjectName("tab3_label_5")
        self.tab3_label_6 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_6.setGeometry(QtCore.QRect(300, 40, 121, 21))
        self.tab3_label_6.setObjectName("tab3_label_6")
        self.tab3_label_7 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_7.setEnabled(False)
        self.tab3_label_7.setGeometry(QtCore.QRect(610, 40, 101, 21))
        self.tab3_label_7.setObjectName("tab3_label_7")
        self.tab3_label_8 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_8.setGeometry(QtCore.QRect(0, 100, 111, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(10)
        self.tab3_label_8.setFont(font)
        self.tab3_label_8.setObjectName("tab3_label_8")
        self.tab3_label_9 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_9.setGeometry(QtCore.QRect(310, 70, 121, 21))
        self.tab3_label_9.setObjectName("tab3_label_9")
        self.tab3_label_10 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_10.setGeometry(QtCore.QRect(480, 70, 91, 21))
        self.tab3_label_10.setObjectName("tab3_label_10")
        self.tab3_label_11 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_11.setEnabled(False)
        self.tab3_label_11.setGeometry(QtCore.QRect(610, 70, 161, 21))
        self.tab3_label_11.setObjectName("tab3_label_11")
        self.tab3_comboBox = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox.setGeometry(QtCore.QRect(460, 10, 81, 22))
        self.tab3_comboBox.setObjectName("tab3_comboBox")
        self.tab3_comboBox_2 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_2.setGeometry(QtCore.QRect(650, 10, 76, 22))
        self.tab3_comboBox_2.setObjectName("tab3_comboBox_2")
        self.tab3_comboBox_4 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_4.setGeometry(QtCore.QRect(460, 40, 81, 22))
        self.tab3_comboBox_4.setObjectName("tab3_comboBox_4")
        self.tab3_comboBox_5 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_5.setGeometry(QtCore.QRect(70, 70, 161, 22))
        self.tab3_comboBox_5.setObjectName("tab3_comboBox_5")
        self.tab3_checkBox = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox.setGeometry(QtCore.QRect(590, 40, 21, 21))
        self.tab3_checkBox.setText("")
        self.tab3_checkBox.setCheckable(False)
        self.tab3_checkBox.setObjectName("tab3_checkBox")
        self.tab3_checkBox_2 = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox_2.setGeometry(QtCore.QRect(290, 70, 21, 21))
        self.tab3_checkBox_2.setText("")
        self.tab3_checkBox_2.setObjectName("tab3_checkBox_2")
        self.tab3_checkBox_3 = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox_3.setGeometry(QtCore.QRect(460, 70, 21, 21))
        self.tab3_checkBox_3.setText("")
        self.tab3_checkBox_3.setObjectName("tab3_checkBox_3")
        self.tab3_checkBox_4 = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox_4.setGeometry(QtCore.QRect(590, 70, 21, 21))
        self.tab3_checkBox_4.setText("")
        self.tab3_checkBox_4.setCheckable(False)
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
        self.tab3_lineEdit = QtWidgets.QLineEdit(self.tab3)
        self.tab3_lineEdit.setGeometry(QtCore.QRect(70, 40, 91, 21))
        self.tab3_lineEdit.setObjectName("tab3_lineEdit")
        self.tab3_label_13 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_13.setGeometry(QtCore.QRect(670, 439, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab3_label_13.setFont(font)
        self.tab3_label_13.setText("")
        self.tab3_label_13.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab3_label_13.setObjectName("tab3_label_13")
        self.tab3_label_14 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_14.setGeometry(QtCore.QRect(1100, 620, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab3_label_14.setFont(font)
        self.tab3_label_14.setText("")
        self.tab3_label_14.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab3_label_14.setObjectName("tab3_label_14")
        self.tab3_label_15 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_15.setGeometry(QtCore.QRect(0, 440, 41, 21))
        self.tab3_label_15.setObjectName("tab3_label_15")
        self.tab3_label_16 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_16.setGeometry(QtCore.QRect(50, 440, 41, 21))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(9)
        self.tab3_label_16.setFont(font)
        self.tab3_label_16.setAutoFillBackground(False)
        self.tab3_label_16.setText("")
        self.tab3_label_16.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tab3_label_16.setObjectName("tab3_label_16")
        self.tab3_toolButton = QtWidgets.QToolButton(self.tab3)
        self.tab3_toolButton.setGeometry(QtCore.QRect(160, 39, 31, 23))
        self.tab3_toolButton.setArrowType(QtCore.Qt.NoArrow)
        self.tab3_toolButton.setObjectName("tab3_toolButton")
        self.tab3_label_17 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_17.setGeometry(QtCore.QRect(530, 90, 71, 21))
        self.tab3_label_17.setText("")
        self.tab3_label_17.setObjectName("tab3_label_17")
        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.tab4_tableWidget = QtWidgets.QTableWidget(self.tab4)
        self.tab4_tableWidget.setGeometry(QtCore.QRect(0, 70, 741, 371))
        self.tab4_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab4_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab4_tableWidget.setAlternatingRowColors(True)
        self.tab4_tableWidget.setObjectName("tab4_tableWidget")
        self.tab4_tableWidget.setColumnCount(0)
        self.tab4_tableWidget.setRowCount(0)
        self.tab4_pushButton = QtWidgets.QPushButton(self.tab4)
        self.tab4_pushButton.setGeometry(QtCore.QRect(690, 40, 51, 21))
        self.tab4_pushButton.setObjectName("tab4_pushButton")
        self.tab4_dateEdit = QtWidgets.QDateEdit(self.tab4)
        self.tab4_dateEdit.setGeometry(QtCore.QRect(63, 10, 91, 22))
        self.tab4_dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab4_dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.tab4_dateEdit.setCalendarPopup(True)
        self.tab4_dateEdit.setObjectName("tab4_dateEdit")
        self.tab4_label = QtWidgets.QLabel(self.tab4)
        self.tab4_label.setGeometry(QtCore.QRect(163, 10, 16, 21))
        self.tab4_label.setObjectName("tab4_label")
        self.tab4_label_2 = QtWidgets.QLabel(self.tab4)
        self.tab4_label_2.setGeometry(QtCore.QRect(3, 10, 51, 21))
        self.tab4_label_2.setObjectName("tab4_label_2")
        self.tab4_dateEdit_2 = QtWidgets.QDateEdit(self.tab4)
        self.tab4_dateEdit_2.setGeometry(QtCore.QRect(183, 10, 91, 22))
        self.tab4_dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab4_dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.tab4_dateEdit_2.setCalendarPopup(True)
        self.tab4_dateEdit_2.setObjectName("tab4_dateEdit_2")
        self.tab4_label_3 = QtWidgets.QLabel(self.tab4)
        self.tab4_label_3.setGeometry(QtCore.QRect(2, 38, 61, 21))
        self.tab4_label_3.setObjectName("tab4_label_3")
        self.tab4_lineEdit = QtWidgets.QLineEdit(self.tab4)
        self.tab4_lineEdit.setGeometry(QtCore.QRect(62, 38, 91, 21))
        self.tab4_lineEdit.setObjectName("tab4_lineEdit")
        self.tab4_label_4 = QtWidgets.QLabel(self.tab4)
        self.tab4_label_4.setGeometry(QtCore.QRect(670, 440, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab4_label_4.setFont(font)
        self.tab4_label_4.setText("")
        self.tab4_label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab4_label_4.setObjectName("tab4_label_4")
        self.tab4_label_5 = QtWidgets.QLabel(self.tab4)
        self.tab4_label_5.setGeometry(QtCore.QRect(0, 440, 41, 21))
        self.tab4_label_5.setObjectName("tab4_label_5")
        self.tab4_label_6 = QtWidgets.QLabel(self.tab4)
        self.tab4_label_6.setGeometry(QtCore.QRect(50, 440, 41, 21))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(9)
        self.tab4_label_6.setFont(font)
        self.tab4_label_6.setAutoFillBackground(False)
        self.tab4_label_6.setText("")
        self.tab4_label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tab4_label_6.setObjectName("tab4_label_6")
        self.tabWidget.addTab(self.tab4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
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
        self.tab5_tableWidget.setSortingEnabled(False)
        self.tab5_label.setText(_translate("MainWindow", "기준일"))
        self.tab5_label_2.setText(_translate("MainWindow", "(단위: 억)"))
        self.tab5_pushButton.setText(_translate("MainWindow", "조회"))
        self.tab5_label_4.setText(_translate("MainWindow", "홀세일 1본부"))
        self.tab5_label_5.setText(_translate("MainWindow", "홀세일 2본부"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), _translate("MainWindow", "수탁고 현황"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow",
                                                                               "                                                                                                                                                            "))
        self.tab1_tableWidget.setSortingEnabled(False)
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
        self.tab2_tableWidget.setSortingEnabled(False)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "API 조회"))
        self.tab3_pushButton.setText(_translate("MainWindow", "조회"))
        self.tab3_tableWidget.setSortingEnabled(False)
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
        self.tab3_toolButton.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "펀드상세내역 조회"))
        self.tab4_tableWidget.setSortingEnabled(False)
        self.tab4_pushButton.setText(_translate("MainWindow", "조회"))
        self.tab4_label.setText(_translate("MainWindow", "~"))
        self.tab4_label_2.setText(_translate("MainWindow", "기준일"))
        self.tab4_label_3.setText(_translate("MainWindow", "펀드코드"))
        self.tab4_label_5.setText(_translate("MainWindow", "조회수:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), _translate("MainWindow", "수익자 정보"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.menudevelop.setTitle(_translate("MainWindow", "develop"))
        self.menuetc.setTitle(_translate("MainWindow", "etc"))
        self.actioninfo_site.setText(_translate("MainWindow", "info site"))
        self.actionset.setText(_translate("MainWindow", "version"))

        # 클래스 변수
        Ui_MainWindow.updateDate="2021/11/30" # 최신 업데이트

        Ui_MainWindow.selectedTable = ""  # DB리스트 선택값
        Ui_MainWindow.mainWindow_df1_0 = ""  # 메인 자료값
        Ui_MainWindow.mainWindow_df3_1 = ""  # 탭3 팝업 자료값
        Ui_MainWindow.mainWindow_df3_1Re = ""  # 탭3 팝업 가공값
        Ui_MainWindow.mainWindow_df3_2 = ""  # 탭3 펀드조회 자료값
        Ui_MainWindow.mainWindow_df3_2Re = ""  # 탭3 펀드조회 가공값
        Ui_MainWindow.mainWindow_df3_3 = ""  # 탭3 수익자정보 자료값
        Ui_MainWindow.mainWindow_df3_3Re = ""  # 탭3 수익자정보 가공값
        Ui_MainWindow.mainWindow_df4_0 = ""  # 탭4 수익자현황 자료값
        Ui_MainWindow.mainWindow_df5_0 = ""  # 탭5 수탁고현황 자료값
        Ui_MainWindow.mainWindow_df5_1 = "" # 수익자 그룹현황 자료값
        Ui_MainWindow.sqlQuery = ""  # 추가 쿼리
        Ui_MainWindow.maxSearch = 10000  # 최대 조회가능 숫자
        Ui_MainWindow.commaLength = 5  # 최소 콤마찍는 자리 수
        Ui_MainWindow.tab3Code = ""  # 탭3 클릭값 펀드코드
        Ui_MainWindow.tab3Name = ""  # 탭3 클릭값 펀드명
        Ui_MainWindow.tab3Col = ""  # 탭3 클릭 확인값
        Ui_MainWindow.tab3Value = ""  # 탭3 클릭 확인값
        Ui_MainWindow.tab3SelectCode = ""  # 탭3 펀드검색 검색명
        Ui_MainWindow.tab5group = "" # 탭5 고객그룹
        Ui_MainWindow.tab5team = "" # 탭5 홀세일본부구분
        Ui_MainWindow.version  # 현재 접속DB 구분
        Ui_MainWindow.color = QtGui.QColor(255, 225, 225)  # 음수표시 색상 RGB

        # Qt디자이너 외 구현
        self.setListWidget()  # DB리스트 생성
        self.tab1_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 내용수정 금지
        self.tab1_newWindow1 = QDialog()  # 세부검색조건 팝업창
        self.tab1_newWindow2 = QDialog()  # 그래픽부분 팝업창
        self.tab3_newWindow1 = QDialog()  # 탭3 팝업창
        self.tab3_newWindow2 = QDialog()  # 탭3 펀드검색 팝업창
        self.tab3_newWindow3 = QDialog()  # 탭3 수익자 팝업창
        self.tab5_newWindow1 = QDialog() # 탭5 수탁고 팝업창
        self.popup_version = QDialog()  # 탭3 수익자 팝업창
        self.tab1_pushButton_3.setDisabled(True)
        self.tab1_pushButton_4.setDisabled(True)
        self.tab2_comboBox.addItem('json')
        self.tab2_comboBox.addItem('xml')
        self.tab1_tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)  # 헤더 중앙정렬
        self.tab3_comboBox.addItems(('전체', '운용중', '운용개시', '결산', '상환'))
        self.tab3_comboBox_2.addItems(('전체', '유', '무'))
        self.tab3_comboBox_4.addItems(('전체', '판매펀드', '운용펀드'))
        self.tab3_comboBox_5.addItems(('전체', '224 흥국자산운용', '207 교보악사자산운용', '216 DB자산운용', '363 트러스톤자산운용', '368 하이자산운용'))
        if Ui_MainWindow.version != "xe": # xe 계정만 날짜 다르게
            self.tab3_dateEdit.setDate(date.today() - timedelta(4))
            self.tab4_dateEdit.setDate(date.today() - timedelta(4))
            self.tab5_dateEdit.setDate(date.today() - timedelta(4))
        self.tab3_dateEdit_2.setDate(date.today() - timedelta(1))  # 자료는 전일자꺼 까지만 있음
        self.tab4_dateEdit_2.setDate(date.today() - timedelta(1))  # 자료는 전일자꺼 까지만 있음
        self.newcreateTable(5,0,'','','','','') # 임시로 시작시 설정
        self.tab3_toolButton.setIcon(QIcon(resource_path('find.png'))) # 돋보기 아이콘
        # self.tab3_label_17.setText('////')
        # processes= process(0),process(1),process(2),process(3)
        # [p.start() for p in processes]

        # 이벤트
        try:
            self.menuetc.triggered.connect(lambda: self.popup1(Ui_MainWindow.updateDate)) # 툴바:업데이트쪽
            self.tab1_pushButton.clicked.connect(lambda: self.newcreateTable(1,0,'','','','',''))  # 탭1 조회
            self.tab1_pushButton_2.clicked.connect(lambda: self.toExcel("1", "0", self.tab1_label_5.text()))  # 엑셀변환 버튼
            self.tab1_tableWidget.cellClicked.connect(self.cellClickEvent)  # 표 클릭시
            self.tab1_tableWidget.currentCellChanged.connect(self.cellClickEvent)  # 표 클릭시 이벤트 둘 다 있어야 재대로 나옴
            self.tab1_listWidget.currentItemChanged.connect(self.clearPlaintext)  # DB리스트 클릭시
            self.tab1_pushButton_3.clicked.connect(self.windowQuery)  # 검색조건 팝업 버튼
            self.tab1_pushButton_4.clicked.connect(lambda: self.windowGraphic("1", "0"))  # 그래픽 팝업 버튼
            self.tab1_checkBox.stateChanged.connect(self.chkBox)  # 체크 변경시
            self.tab2_comboBox.currentIndexChanged.connect(self.connectAPI)  # API 자료조회
            self.tab2_pushbutton.clicked.connect(self.connectAPI)  # API 자료조회
            self.tab3_pushButton.clicked.connect(lambda: self.newcreateTable(3,0,'','','','','')) # 탭3 테이블 조회
            self.tab3_tableWidget.cellClicked.connect(self.tab3_returnCode)  # 탭3 표 클릭시
            self.tab3_toolButton.clicked.connect(self.windowCode)  # 탭3 펀드검색
            self.tab3_tableWidget.doubleClicked.connect(lambda: self.tab3_selectWindow(Ui_MainWindow.tab3Col,
                  Ui_MainWindow.tab3Value,Ui_MainWindow.tab3Code,Ui_MainWindow.tab3Name))  # 탭3 표 더블블릭시
            self.tab4_pushButton.clicked.connect(lambda: self.newcreateTable(4,0,'','','','','')) #탭4 조회
            self.tab5_pushButton.clicked.connect(lambda: self.newcreateTable(5,0,'','','','',''))  # 탭5 조회
            self.tab5_dateEdit.dateChanged.connect(lambda: self.newcreateTable(5,0,'','','','',''))  # 탭5 조회
            self.tab5_tableWidget.cellClicked.connect(self.tab5_returnCode)  # 탭5 표 클릭시
            self.tab5_tableWidget.doubleClicked.connect(self.tab5_win1SearchValue)  # 탭5 펀드검색
            self.tab1_pushButton_5.clicked.connect(self.test)  # 테스트용
        except:
            traceback.print_exc()

        # -----------------------------------windowGraphic

    def windowGraphic(self, tab, win):
        """그래프 차트 창 """

        self.tab1_win2label = QtWidgets.QLabel(self.tab1_newWindow2)
        self.tab1_win2label.setGeometry(QtCore.QRect(10, 10, 56, 21))
        self.tab1_win2label.setObjectName("tab1_win2label")
        self.tab1_win2comboBox = QtWidgets.QComboBox(self.tab1_newWindow2)
        self.tab1_win2comboBox.setGeometry(QtCore.QRect(190, 11, 171, 22))
        self.tab1_win2comboBox.setObjectName("tab1_win2comboBox")
        self.tab1_win2comboBox_2 = QtWidgets.QComboBox(self.tab1_newWindow2)
        self.tab1_win2comboBox_2.setGeometry(QtCore.QRect(70, 10, 81, 22))
        self.tab1_win2comboBox_2.setObjectName("tab1_win2comboBox_2")
        self.tab1_win2Widget = QtWidgets.QWidget(self.tab1_newWindow2)
        self.tab1_win2Widget.setGeometry(QtCore.QRect(10, 40, 901, 591))
        self.tab1_win2Widget.setObjectName("tab1_win2Widget")
        self.tab1_win2pushButton = QtWidgets.QPushButton(self.tab1_newWindow2)
        self.tab1_win2pushButton.setGeometry(QtCore.QRect(850, 10, 61, 21))
        self.tab1_win2pushButton.setObjectName("tab1_win2pushButton")
        self.tab1_win2label_2 = QtWidgets.QLabel(self.tab1_newWindow2)
        self.tab1_win2label_2.setGeometry(QtCore.QRect(158, 10, 31, 21))
        self.tab1_win2label_2.setAutoFillBackground(True)
        self.tab1_win2label_2.setObjectName("tab1_win2label_2")
        self.tab1_win2label_3 = QtWidgets.QLabel(self.tab1_newWindow2)
        self.tab1_win2label_3.setGeometry(QtCore.QRect(370, 9, 31, 21))
        self.tab1_win2label_3.setAutoFillBackground(True)
        self.tab1_win2label_3.setObjectName("tab1_win2label_3")
        self.tab1_win2comboBox_3 = QtWidgets.QComboBox(self.tab1_newWindow2)
        self.tab1_win2comboBox_3.setGeometry(QtCore.QRect(400, 10, 171, 22))
        self.tab1_win2comboBox_3.setObjectName("tab1_win2comboBox_3")

        _translate = QtCore.QCoreApplication.translate

        self.tab1_win2label.setText(_translate("t1Window2", "차트종류"))
        self.tab1_win2pushButton.setText(_translate("t1Window2", "조회"))
        self.tab1_win2label_2.setText(_translate("t1Window2", "x축"))
        self.tab1_win2label_3.setText(_translate("t1Window2", "y축"))

        # 이벤트
        self.tab1_win2pushButton.clicked.connect(lambda: self.selectGraphic(chart, tab, win))  # 차트 제작
        self.tab1_win2comboBox_2.currentIndexChanged.connect(
            lambda: self.setGraphicComboBox(chart, tab, win))  # 콤보박스 재설정

        # Qt디자이너 외 구현
        chart = ["원형차트", "선차트", "막대차트", "산포도", "스템 플롯"]

        try:
            self.tab1_win2comboBox_2.addItems(chart)
            if tab == "1" and win == "0":
                for i in Ui_MainWindow.mainWindow_df1_0.columns.values.tolist():
                    self.tab1_win2comboBox.addItem(i)
                    self.tab1_win2comboBox_3.addItem(i)
            elif tab == "3" and win == "1":
                for i in Ui_MainWindow.mainWindow_df3_1Re.columns.values.tolist():
                    self.tab1_win2comboBox.addItem(i)
                    self.tab1_win2comboBox_3.addItem(i)
            elif tab == "3" and win == "3":
                for i in Ui_MainWindow.mainWindow_df3_3Re.columns.values.tolist():
                    self.tab1_win2comboBox.addItem(i)
                    self.tab1_win2comboBox_3.addItem(i)
            plt.ion()
            self.fig = plt.Figure()
            self.canvas = FigureCanvas(self.fig)
            layout = QVBoxLayout(self.tab1_win2Widget)
            layout.addWidget(self.canvas)

            self.tab1_newWindow2.setWindowModality(QtCore.Qt.ApplicationModal)  # 하위창 컨트롤 금지
            self.tab1_newWindow2.show()
            plt.close(self.fig)  # 종료시 차트 지움

        except:
            traceback.print_exc()

    def selectGraphic(self, chart, tab, win):
        """ 차트 선택"""
        if self.tab1_win2comboBox_2.currentText() == chart[0]:  # 원형 차트
            self.set_GraphicPie(tab, win)
        else:
            self.set_GraphLine(tab, win, chart)

    def setGraphicComboBox(self, chart, tab, win):
        """차트마다 쓸 항목 설정"""
        try:
            if self.tab1_win2comboBox_2.currentText() == chart[0]:
                self.tab1_win2label_2.setText("항목")
                self.tab1_win2label_3.setText("")
                self.tab1_win2comboBox_3.setDisabled(True)
            elif self.tab1_win2comboBox_2.currentText() == chart[1]:
                self.tab1_win2label_2.setText("x축")
                self.tab1_win2label_3.setText("y축")
                self.tab1_win2comboBox_3.setDisabled(False)
            elif self.tab1_win2comboBox_2.currentText() == chart[2]:
                self.tab1_win2label_2.setText("x축")
                self.tab1_win2label_3.setText("y축")
                self.tab1_win2comboBox_3.setDisabled(False)
            elif self.tab1_win2comboBox_2.currentText() == chart[3]:
                self.tab1_win2label_2.setText("x축")
                self.tab1_win2label_3.setText("y축")
                self.tab1_win2comboBox_3.setDisabled(False)
            else:
                traceback.print_exc()
        except:
            traceback.print_exc()

    def set_GraphicPie(self, tab, win):
        """내부쿼리 운용회사펀드그룹코드-펀드코드 조회시에는 에러 MatplotlibDeprecationWarning: normalize=None does not normalize if the sum is less than 1 but this behavior is deprecated since 3.3 until two minor releases later."""
        try:
            val = []  # 수량
            idx = []  # 항목
            if tab == "1" and win == "0":
                groupd = Ui_MainWindow.mainWindow_df1_0.groupby([self.tab1_win2comboBox.currentText()]).count()
            elif tab == "3" and win == "1":
                groupd = Ui_MainWindow.mainWindow_df3_1Re.groupby([self.tab1_win2comboBox.currentText()]).count()
            elif tab == "3" and win == "3":
                groupd = Ui_MainWindow.mainWindow_df3_3Re.groupby([self.tab1_win2comboBox.currentText()]).count()
            groupd2 = groupd.iloc[:, 0]
            idx = groupd2.index
            [val.append(i) for i in groupd2]

            self.canvas.figure.clear()  # 차트 다시 그림
            chart = self.canvas.figure.subplots()
            # explode = (0.1, 0, 0, 0)  # 차트의 간격 부분으로 0끼리는 붙어있음 컬럼수와 맞아야함
            chart.pie(val, labels=idx, autopct="%1.1f%%", startangle=90)
            chart.axis("equal")
            self.canvas.draw()
        except:
            a = QMessageBox()
            a.setText("차트가 생성되지 않았습니다")
            a.setStandardButtons(QMessageBox.Ok)
            a.exec_()
            traceback.print_exc()

    def set_GraphLine(self, tab, win, chart):
        """선차트,막대차트,산포도,스템 플롯차트"""
        try:

            if tab == "1" and win == "0":
                df = Ui_MainWindow.mainWindow_df1_0
            if tab == "3" and win == "1":
                df = Ui_MainWindow.mainWindow_df3_1Re  # .sort_values(by=['기준일자'], ascending=False)
            if tab == "3" and win == "3":
                df = Ui_MainWindow.mainWindow_df3_3Re  # .sort_values(by=['기준일자'], ascending=False)
            xval = df[self.tab1_win2comboBox.currentText()]
            yval = df[self.tab1_win2comboBox_3.currentText()]
            #
            # if self.isFloat(df[self.tab1_win2comboBox_3.currentText()][0])!=0: # 첫 값보고 타입 확인
            #     yscale=[]
            #     maxVal=math.ceil(df[self.tab1_win2comboBox_3.currentText()].max())
            #     minVal=math.floor(df[self.tab1_win2comboBox_3.currentText()].min())
            #     ytick=maxVal-minVal
            #     yscale.append(decimal.Decimal(math.floor(minVal)))
            #     for i in range(1,8):
            #         yscale.append(decimal.Decimal(math.floor(minVal+(ytick/10*i))))
            #     yscale.append(decimal.Decimal(math.ceil(maxVal)))
            #     print(yscale)
            self.canvas.figure.clear()  # 차트 다시 그림
            ax = self.canvas.figure.subplots(1, 1)
            # ax.set_yticks(yscale)
            if self.tab1_win2comboBox_2.currentText() == chart[1]:  # 선 차트
                ax.plot(xval, yval, marker=".", linestyle="-", color="g")
            elif self.tab1_win2comboBox_2.currentText() == chart[2]:  # 막대 차트
                ax.bar(xval, yval, alpha=0.4, width=0.3)
            elif self.tab1_win2comboBox_2.currentText() == chart[3]:  # 산포도
                ax.scatter(xval, yval)
            elif self.tab1_win2comboBox_2.currentText() == chart[4]:  # 산포도
                ax.stem(xval, yval)  # 스템 플롯

            ax.set_xlabel(self.tab1_win2comboBox.currentText())
            ax.set_ylabel(self.tab1_win2comboBox_3.currentText())
            # ax.legend(['asd']) 선 이름
            self.canvas.draw()
        except:
            a = QMessageBox()
            a.setText("차트를 생성할 수 없는 항목입니다")
            a.setStandardButtons(QMessageBox.Ok)
            a.exec_()
            traceback.print_exc()

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
        self.tab1_win1comboBox_3.addItems(["부분일치", "일치", "제외", "이상", "이하"])
        self.tab1_win1comboBox_4.addItems(["부분일치", "일치", "제외", "이상", "이하"])
        self.setCombobox()
        self.tab1_newWindow1.show()

        # 이벤트
        try:
            self.tab1_win1pushButton.clicked.connect(self.submitQuery)  # 확인버튼 누를시
            self.tab1_win1checkBox.stateChanged.connect(self.ableQuery1) #추가조건 활성/비활성화
            self.tab1_win1checkBox_2.stateChanged.connect(self.ableQuery2) #추가조건 활성/비활성화
        except:
            traceback.print_exc()

    def ableQuery1(self):
        """ 체크시 옆에 텍스트박스 활성화, 해제시 비활성화+값 지움"""
        if self.tab1_win1checkBox.isChecked():
            self.tab1_win1lineEdit.setEnabled(True)  # 입력문 활성화
            self.tab1_win1pushButton.setDisabled(False)
        else:
            self.tab1_win1lineEdit.setEnabled(False)
            self.tab1_win1lineEdit.setText("")

    def ableQuery2(self):
        """ 체크시 옆에 텍스트박스 활성화, 해제시 비활성화+값 지움"""
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
        Ui_MainWindow.sqlQuery = sql1 + sql2
        self.tab1_plainTextEdit.setPlainText(Ui_MainWindow.sqlQuery.replace("TO_CHAR", "", 1))
        self.tab1_checkBox.setChecked(True)
        self.tab1_plainTextEdit.setEnabled(True)
        Ui_MainWindow.mainWindow_df1_0 = ""
        self.newcreateTable(1, 0, '', '', '','','')
        self.tab1_plainTextEdit.setPlainText(Ui_MainWindow.sqlQuery)
        self.tab1_newWindow1.close()

    def setQuery(self, columnText, i, lineEditText):
        """ 조건을 설정해 SQL에 추가 """
        str1 = [" like '%", " = '", " != '", " <= '", " >= '"]
        str2 = ["%'", "'"]
        sql = " and TO_CHAR(" + columnText + ") " + str1[i] + lineEditText + str2[math.trunc((i + 9) / 10)]  # %만 2번
        return sql

    def setCombobox(self):
        """ 콤보박스값들 설정 """
        for i in Ui_MainWindow.mainWindow_df1_0.columns.values.tolist():
            self.tab1_win1comboBox.addItem(i)
            self.tab1_win1comboBox_2.addItem(i)

    # -----------------------------------------------tab1

    def chkBox(self):
        """조건 비활성화 유무 표시"""
        self.newcreateTable(1, 0, '', '', '','','')
        if self.tab1_checkBox.isChecked():
            self.tab1_plainTextEdit.setEnabled(True)
        else:
            self.tab1_plainTextEdit.setEnabled(False)

    def setListWidget(self):
        """ 왼쪽 리스트에 DB리스트 생성. 리스트는 하드코딩 약 8만건 기준 조회시간 30초 """
        dbList = ["정보_회사","SUIKJA_INFO", "SUIKJA_COM", "FUND_BASIC", "FUND_COMPANY", "FUND_INTEGRATE", "FUND_OPERATE", "FUND_RETAIL",
                  "FUND_RETAIL_SELLER",
                  "공통코드", "운용역코드", "펀드_결산기준가격", "펀드_기준가격", "펀드_기준가격회계", "펀드_마스터", "펀드_민감도내역",
                  "펀드_보수계산정보", "펀드_보수율", "펀드_보수일별집계", "펀드_설정해지결제", "펀드_설정해지내역", "펀드_설정해지보수",
                  "펀드_설정해지예정내역", "펀드_설정해지원장", "펀드_수익자정보", "펀드_운용회사변경내역", "펀드_위탁사별구조관계총괄", "펀드_위탁사별펀드정보",
                  "펀드_전체해지이체거래", "펀드_총계정원장", "펀드_판매사별보수내역", "펀드_판매사별실적",
                  "펀드_환율적용방법", "정보_거래그룹", "정보_거래유형", "정보_계정과목", "정보_국가", "정보_매매처", "정보_발행기관",
                  "정보_발행기관예외", "정보_부실보증기관", "정보_사무수탁사", "정보_수익자", "정보_신용등급", "정보_업종", "정보_운용역담당펀드",
                  "정보_자산분류", "정보_증권거래소", "정보_증권거래소회사업종", "정보_채권기준종류", "정보_코스콤채권종류", "정보_팀",
                  "정보_팀별운용역", "정보_판매회사펀드", "정보_펀드자체유형", "정보_펀드협회분류코드", "정보_펀드회계유형", "정보_평가회사채권분류",
                  "정보_회사", "정보_회사그룹", "평가_벤치마크지수", "평가_펀드기여손익", "평가_펀드목표수익",
                  "평가_펀드부문손익", "평가_펀드부문손익률", "평가_펀드성과평가", "국가별공휴일",
                  "기타_공휴일", "기타_관심펀드", "기타_달력일자", "기타_시스템체크", "기타_일자", "----------", "SELL_COMPANY",
                  "HKCL.FUND_PANCOM_VIEW", "hkcl.FUND_REPORT_VIEW", "hkcl.FUND_RETAIL_VIEW", "hkcl.FUND_SUIK_VIEW",
                  "hkcl.FUND_SUTAK_VIEW"
                  ]
        self.tab1_listWidget.addItems(dbList)

    def cellClickEvent(self, row, col):
        """ 셀 클릭시 계산값을 보여줌"""
        try:
            if row != -1 and col != -1:  # 표를 클릭하고 다른걸 클릭하면 좌표값이 -1이 찍힘
                if self.tab1_tableWidget.item(row, col).text():
                    clickCellText = self.tab1_tableWidget.item(row, col).text()
                    self.tab1_label_2.setText(clickCellText)
                    selected = self.tab1_tableWidget.selectedRanges()
                    cnt = 0
                    tot = []

                    for idx, val in enumerate(
                            selected):  # val.columnCount(), val.topRow(), val.leftColumn(), val.bottomRow(), val.rightColumn()
                        for i in range(int(val.topRow()), int(val.bottomRow()) + 1):
                            for k in range(int(val.leftColumn()), int(val.rightColumn()) + 1):
                                cnt = cnt + 1
                                str1 = self.tab1_tableWidget.item(i, k).text()
                                str1 = self.delComma(str1)
                                value = self.isFloat(str1)
                                if value:
                                    tot.append(value)

                    self.tab1_label_9.setText(str(cnt))  # 수
                    total = str(sum(tot))
                    self.tab1_label_11.setText(self.setComma(total))  # 합계
        except:
            traceback.print_exc()

    def clearPlaintext(self):
        """조건검색 내용 지우고 검색"""
        self.tab1_plainTextEdit.setPlainText("")
        Ui_MainWindow.sqlQuery = ""
        self.newcreateTable(1, 0, '', '', '','','')

    def tableCount(self):
        """테이블 자료수 조회"""
        try:
            sql = query.returnSQL('tableCount').format(Ui_MainWindow.selectedTable)
            cur.execute(sql)
            cnt = cur.fetchall()
            a = list(cnt[0])[0]
        except:
            traceback.print_exc()
        return str(a)

    def searchColumn(self):
        """ 테이블 컬럼을 가지고와서 DB리스트에 입력"""
        str1 = []
        try:
            if Ui_MainWindow.selectedTable:
                sql = query.returnSQL('searchColumn').format(Ui_MainWindow.selectedTable)
                cur.execute(sql)
                idx = cur.fetchall()
                [str1.append(''.join(idx[i])) for i in range(len(idx))]
        except:
            traceback.print_exc()
        return str1

    def searchValue(self):
        """ SQL 값 리턴"""
        try:
            row = ""
            subSql = ""
            if self.tab1_checkBox.isChecked():
                subSql = Ui_MainWindow.sqlQuery
            else:
                subSql = ""
            if Ui_MainWindow.selectedTable:  # 값 있는 경우
                sql = query.returnSQL('searchValue').format(Ui_MainWindow.selectedTable) + subSql
                print(sql)
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

    def menuInfo(self):
        """찾기 귀찮아서"""
        os.system('explorer https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableWidget.html')

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
        try:
            dict1 = {'회사': [], '상품': [], '등록일': []}
            fncistnm = []
            prdnm = []
            regdate = []

            req = requests.get(url)
            soup = bs4.BeautifulSoup(req.text, "html.parser")
            col1 = soup.findAll("fncistnm")
            col2 = soup.findAll("prdnm")
            col3 = soup.findAll("regdate")
            [fncistnm.append(i.string) for i in col1]
            [prdnm.append(i.string) for i in col2]
            [regdate.append(i.string) for i in col3]

            dict1['회사'] = fncistnm
            dict1['상품'] = prdnm
            dict1['등록일'] = regdate

            df2 = pd.DataFrame(dict1)
            self.newcreateTable(2, 0, '', df2, '', '','')
            # self.tab2_createTable(df2)
        except:
            traceback.print_exc()

    def jsonParse(self, url):
        """ json 파싱, 파일내용 지저분한건 jsonviewer로 보기"""
        try:
            dict1 = {'회사': [], '상품': [], '등록일': []}
            fncistnm = []
            prdnm = []
            regdate = []

            response = requests.get(url).json()
            asd = response['getProductList']['item']
            for i in asd:
                fncistnm.append(list(i.values())[2])
                prdnm.append(list(i.values())[4])
                regdate.append(list(i.values())[3])
            dict1['회사'] = fncistnm
            dict1['상품'] = prdnm
            dict1['등록일'] = regdate
            df2 = pd.DataFrame(dict1)
            self.newcreateTable(2,0, '', df2, '', '','')
        except:
            traceback.print_exc()

    # ---------------------------------------tab3

    def tab3_searchValue(self):
        """ SQL 값 리턴 Hints 22502 화면이고 상황끝난펀드 부분은 더 구현 안 함."""
        try:
            sql = ""
            sql += query.returnSQL('tab3_SearchQuery')
            sql += "and b.tr_ymd >= '{}'".format(self.tab3_dateEdit.text().replace('-', '/'))
            sql += "and b.tr_ymd <= '{}'".format(self.tab3_dateEdit_2.text().replace('-', '/'))

            if self.tab3_lineEdit.text():  # 펀드코드
                self.tab3_lineEdit.setText(self.tab3_lineEdit.text().upper())
                sql += "and a.펀드코드='{}'".format(self.tab3_lineEdit.text())

            if self.tab3_comboBox.currentText() == '운용중':  # 운용중: 기준일이 상환일보다 이전
                sql += " and a.상환예정일자 >= '{}'".format(self.tab3_dateEdit_2.text().replace('-', '/'))
            elif self.tab3_comboBox.currentText() == '운용개시':  # 운용개시: 기준일 내에 운용개시일이 있는 경우
                sql += " and (select min(tr_ymd) from FUND_INTEGRATE where a.펀드코드=FUND_CD) >= '{}'".format(
                    self.tab3_dateEdit.text().replace('-', '/'))
                sql += " and (select min(tr_ymd) from FUND_INTEGRATE where a.펀드코드=FUND_CD) <= '{}'".format(
                    self.tab3_dateEdit_2.text().replace('-', '/'))
            elif self.tab3_comboBox.currentText() == '결산':  # 결산: 기준일 내에 다음결산일이 있는 경우
                sql += " and a.다음결산일자 >= '{}'".format(self.tab3_dateEdit.text().replace('-', '/'))
                sql += " and a.다음결산일자 <= '{}'".format(self.tab3_dateEdit_2.text().replace('-', '/'))
            elif self.tab3_comboBox.currentText() == '상환':  # 상환: 현재 조건이 안 맞음
                sql += " and a.펀드종료일자 >= '{}'".format(self.tab3_dateEdit.text().replace('-', '/'))
                sql += " and a.펀드종료일자 <= '{}'".format(self.tab3_dateEdit_2.text().replace('-', '/'))

            if self.tab3_comboBox_5.currentText() != '전체':  # 운용사코드
                sql += " and a.운용회사코드 = '{}'".format(self.tab3_comboBox_5.currentText()[:3])

            if self.tab3_comboBox_2.currentText() == '유':  # 잔고
                sql += " and b.FUND_TOT_JASAN >0"
            elif self.tab3_comboBox_2.currentText() == '무':
                sql += " and b.FUND_TOT_JASAN =0"

            if self.tab3_checkBox_2.isChecked():  # 국외세액환급대상펀드 체크
                sql += " and b.FUND_FOREIGN_TAX='비대상'"

            if self.tab3_checkBox_3.isChecked():  # 멀티커런시 체크
                sql += " and a.멀티통화여부='Y'"
            #   판매펀드: 판매사 1이상
            print(sql)
            cur.execute(sql)
            row = cur.fetchall()
            if len(row) == 0:
                row = [("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "","", "", "", "", "", "", "", "", "")]
            return row
        except:
            a = QMessageBox()
            a.setText("데이터 조회 중 오류가 발생했습니다.")
            a.setStandardButtons(QMessageBox.Ok)
            a.exec_()
            traceback.print_exc()

    def tab3_returnCode(self, row, col):
        """ 팝업으로 넘길 펀드명,번호. 더블클릭 이벤트에는 클릭값 받는 인자가 없음"""
        self.tab3_newWindow1.update()
        Ui_MainWindow.tab3Code = self.tab3_tableWidget.item(row, 1).text()
        Ui_MainWindow.tab3Name = self.tab3_tableWidget.item(row, 2).text()
        Ui_MainWindow.tab3Value = self.tab3_tableWidget.item(row, 4).text()
        Ui_MainWindow.tab3Col = col

    # -----------------------------------------------탭3 팝업창
    def windowList(self, fundCode, fundName):
        """ 탭3 팝업창"""
        self.tab3_win1tableWidget = QtWidgets.QTableWidget(self.tab3_newWindow1)
        self.tab3_win1tableWidget.setGeometry(QtCore.QRect(0, 30, 1171, 501))
        self.tab3_win1tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab3_win1tableWidget.setAlternatingRowColors(True)
        self.tab3_win1tableWidget.setObjectName("tab3_win1tableWidget")
        self.tab3_win1tableWidget.setColumnCount(0)
        self.tab3_win1tableWidget.setRowCount(0)
        self.tab3_win1label = QtWidgets.QLabel(self.tab3_newWindow1)
        self.tab3_win1label.setGeometry(QtCore.QRect(0, 6, 41, 20))
        self.tab3_win1label.setObjectName("tab3_win1label")
        self.tab3_win1label_2 = QtWidgets.QLabel(self.tab3_newWindow1)
        self.tab3_win1label_2.setGeometry(QtCore.QRect(40, 6, 401, 20))
        self.tab3_win1label_2.setAutoFillBackground(True)
        self.tab3_win1label_2.setText("")
        self.tab3_win1label_2.setObjectName("tab3_win1label_2")
        self.tab3_win1pushButton = QtWidgets.QPushButton(self.tab3_newWindow1)
        self.tab3_win1pushButton.setGeometry(QtCore.QRect(1090, 5, 75, 21))
        self.tab3_win1pushButton.setObjectName("tab3_win1pushButton")
        self.tab3_win1label_4 = QtWidgets.QLabel(self.tab3_newWindow1)
        self.tab3_win1label_4.setGeometry(QtCore.QRect(120, 531, 131, 21))
        self.tab3_win1label_4.setAutoFillBackground(True)
        self.tab3_win1label_4.setText("")
        self.tab3_win1label_4.setObjectName("tab3_win1label_4")
        self.tab3_win1label_6 = QtWidgets.QLabel(self.tab3_newWindow1)
        self.tab3_win1label_6.setGeometry(QtCore.QRect(290, 531, 51, 21))
        self.tab3_win1label_6.setAutoFillBackground(True)
        self.tab3_win1label_6.setText("")
        self.tab3_win1label_6.setObjectName("tab3_win1label_6")
        self.tab3_win1label_3 = QtWidgets.QLabel(self.tab3_newWindow1)
        self.tab3_win1label_3.setGeometry(QtCore.QRect(100, 531, 21, 21))
        self.tab3_win1label_3.setObjectName("tab3_win1label_3")
        self.tab3_win1label_7 = QtWidgets.QLabel(self.tab3_newWindow1)
        self.tab3_win1label_7.setGeometry(QtCore.QRect(350, 531, 31, 21))
        self.tab3_win1label_7.setObjectName("tab3_win1label_7")
        self.tab3_win1label_8 = QtWidgets.QLabel(self.tab3_newWindow1)
        self.tab3_win1label_8.setGeometry(QtCore.QRect(380, 531, 141, 21))
        self.tab3_win1label_8.setAutoFillBackground(True)
        self.tab3_win1label_8.setText("")
        self.tab3_win1label_8.setObjectName("tab3_win1label_8")
        self.tab3_win1label_5 = QtWidgets.QLabel(self.tab3_newWindow1)
        self.tab3_win1label_5.setGeometry(QtCore.QRect(260, 531, 31, 21))
        self.tab3_win1label_5.setObjectName("tab3_win1label_5")
        self.tab3_win1label_9 = QtWidgets.QLabel(self.tab3_newWindow1)
        self.tab3_win1label_9.setGeometry(QtCore.QRect(1095, 532, 71, 20))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab3_win1label_9.setFont(font)
        self.tab3_win1label_9.setAutoFillBackground(True)
        self.tab3_win1label_9.setText("")
        self.tab3_win1label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab3_win1label_9.setObjectName("tab3_win1label_9")
        self.tab3_win1pushButton_2 = QtWidgets.QPushButton(self.tab3_newWindow1)
        self.tab3_win1pushButton_2.setGeometry(QtCore.QRect(1010, 5, 75, 21))
        self.tab3_win1pushButton_2.setObjectName("tab3_win1pushButton_2")
        self.tab3_win1label_10 = QtWidgets.QLabel(self.tab3_newWindow1)
        self.tab3_win1label_10.setGeometry(QtCore.QRect(50, 531, 41, 21))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(9)
        self.tab3_win1label_10.setFont(font)
        self.tab3_win1label_10.setAutoFillBackground(True)
        self.tab3_win1label_10.setText("")
        self.tab3_win1label_10.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tab3_win1label_10.setObjectName("tab3_win1label_10")
        self.tab3_win1label_11 = QtWidgets.QLabel(self.tab3_newWindow1)
        self.tab3_win1label_11.setGeometry(QtCore.QRect(0, 531, 41, 21))
        self.tab3_win1label_11.setObjectName("tab3_win1label_11")
        self.tab3_win1checkBox_2 = QtWidgets.QCheckBox(self.tab3_newWindow1)
        self.tab3_win1checkBox_2.setGeometry(QtCore.QRect(813, 5, 16, 21))
        self.tab3_win1checkBox_2.setText("")
        self.tab3_win1checkBox_2.setChecked(True)
        self.tab3_win1checkBox_2.setObjectName("tab3_win1checkBox_2")
        self.tab3_win1checkBox = QtWidgets.QCheckBox(self.tab3_newWindow1)
        self.tab3_win1checkBox.setGeometry(QtCore.QRect(663, 5, 16, 21))
        self.tab3_win1checkBox.setText("")
        self.tab3_win1checkBox.setChecked(True)
        self.tab3_win1checkBox.setObjectName("tab3_win1checkBox")
        self.tab3_win1dateEdit_2 = QtWidgets.QDateEdit(self.tab3_newWindow1)
        self.tab3_win1dateEdit_2.setEnabled(True)
        self.tab3_win1dateEdit_2.setGeometry(QtCore.QRect(833, 5, 91, 21))
        self.tab3_win1dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab3_win1dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.tab3_win1dateEdit_2.setCalendarPopup(True)
        self.tab3_win1dateEdit_2.setObjectName("tab3_win1dateEdit_2")
        self.tab3_win1dateEdit = QtWidgets.QDateEdit(self.tab3_newWindow1)
        self.tab3_win1dateEdit.setEnabled(True)
        self.tab3_win1dateEdit.setGeometry(QtCore.QRect(683, 5, 91, 21))
        self.tab3_win1dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab3_win1dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.tab3_win1dateEdit.setCalendarPopup(True)
        self.tab3_win1dateEdit.setObjectName("tab3_win1dateEdit")
        self.tab3_win1label_12 = QtWidgets.QLabel(self.tab3_newWindow1)
        self.tab3_win1label_12.setGeometry(QtCore.QRect(793, 5, 16, 21))
        self.tab3_win1label_12.setObjectName("tab3_win1label_12")
        self.tab3_win1pushButton_3 = QtWidgets.QPushButton(self.tab3_newWindow1)
        self.tab3_win1pushButton_3.setGeometry(QtCore.QRect(930, 5, 75, 21))
        self.tab3_win1pushButton_3.setObjectName("tab3_win1pushButton_3")

        _translate = QtCore.QCoreApplication.translate

        self.tab3_win1tableWidget.setSortingEnabled(False)
        self.tab3_win1label.setText(_translate("tab3_win1Main", "펀드명:"))
        self.tab3_win1pushButton.setText(_translate("tab3_win1Main", "엑셀 변환"))
        self.tab3_win1label_3.setText(_translate("tab3_win1Main", "값:"))
        self.tab3_win1label_7.setText(_translate("tab3_win1Main", "합계:"))
        self.tab3_win1label_5.setText(_translate("tab3_win1Main", "갯수:"))
        self.tab3_win1pushButton_2.setText(_translate("tab3_win1Main", "그래프"))
        self.tab3_win1label_11.setText(_translate("tab3_win1Main", "조회수:"))
        self.tab3_win1label_12.setText(_translate("tab3_win1Main", "~"))
        self.tab3_win1pushButton_3.setText(_translate("tab3_win1Main", "조회"))

        # QT디자이너 외 구현
        self.tab3_newWindow1.destroy()
        self.tab3_newWindow1.setWindowTitle("새창")
        self.tab3_newWindow1.setWindowModality(QtCore.Qt.ApplicationModal)  # 하위창 컨트롤 금지
        self.tab3_newWindow1.resize(1169, 558)
        self.tab3_win1label_2.setText(fundName)
        self.newcreateTable(3, 1, '', '', '','', fundCode)
        if Ui_MainWindow.version != "xe" and len(Ui_MainWindow.mainWindow_df3_1) > 0:
            self.tab3_win1dateEdit.setDate(Ui_MainWindow.mainWindow_df3_1['기준일자'].min())
        else:
            self.tab3_win1dateEdit.setDate(date.today() - timedelta(1))
        self.tab3_win1dateEdit_2.setDate(date.today() - timedelta(1))
        self.tab3_newWindow1.show()

        # 이벤트
        try:
            self.tab3_win1tableWidget.cellClicked.connect(self.tab3_cellClickEvent)  # 표 클릭시
            self.tab3_win1tableWidget.currentCellChanged.connect(self.tab3_cellClickEvent)  # 표 클릭시
            self.tab3_win1pushButton.clicked.connect(
                lambda: self.toExcel("3", "1", self.tab3_win1label_2.text()))  # 엑셀변환 버튼
            self.tab3_win1pushButton_2.clicked.connect(lambda: self.windowGraphic("3", "1"))  # 탭3 새창 그래픽 팝업 버튼
            self.tab3_win1checkBox.stateChanged.connect(lambda: self.ckeckedTab3_Win1checkBox(1))  # 날짜로 검색
            self.tab3_win1checkBox_2.stateChanged.connect(lambda: self.ckeckedTab3_Win1checkBox(2))  # 날짜로 검색
            self.tab3_win1pushButton_3.clicked.connect(lambda: self.newcreateTable(3, 1, "re", '', '', '',''))  # 조회
        except:
            traceback.print_exc()

    def ckeckedTab3_Win1checkBox(self, val):
        """일별검색 활성화"""
        if val == 1:
            if self.tab3_win1checkBox.isChecked():
                self.tab3_win1dateEdit.setEnabled(True)
            else:
                self.tab3_win1dateEdit.setEnabled(False)
        elif val == 2:
            if self.tab3_win1checkBox_2.isChecked():
                self.tab3_win1dateEdit_2.setEnabled(True)
            else:
                self.tab3_win1dateEdit_2.setEnabled(False)

    def tab3_cellClickEvent(self, row, col):
        """ 셀 클릭시 계산값을 보여줌 클릭한 전 페이지를 구분하는 방법을 못 찾아 따로 구현"""
        try:
            if row > 0 and col > 0:  # 표를 클릭하고 다른걸 클릭하면 좌표값이 -1이 찍힘
                if self.tab3_win1tableWidget.item(row, col).text():
                    clickCellText = self.tab3_win1tableWidget.item(row, col).text()
                    self.tab3_win1label_4.setText(clickCellText)
                    selected = self.tab3_win1tableWidget.selectedRanges()
                    cnt = 0
                    tot = []

                    for idx, val in enumerate(
                            selected):  # val.columnCount(), val.topRow(), val.leftColumn(), val.bottomRow(), val.rightColumn()
                        for i in range(int(val.topRow()), int(val.bottomRow()) + 1):
                            for k in range(int(val.leftColumn()), int(val.rightColumn()) + 1):
                                cnt = cnt + 1
                                str1 = self.tab3_win1tableWidget.item(i, k).text()
                                str1 = self.delComma(str1)
                                value = self.isFloat(str1)
                                if value:
                                    tot.append(value)

                    self.tab3_win1label_6.setText(str(cnt))  # 수
                    total = str(sum(tot))
                    self.tab3_win1label_8.setText(self.setComma(total))  # 합계
        except:
            traceback.print_exc()

    def test(self):
        try:
            print("~~")
            pp = [('1', '2', '3', '4'),
                  ('5', '6', '7', '8'),
                  ('9', '10', '11', '12')]
            df11 = pd.DataFrame(pp)
            self.asd(df11)
            self.asd2(df11)
            # self.asd3(df11)
            print("끝")

        except:
            traceback.print_exc()

    def asd(self, df11):
        try:
            for i in range(len(df11.index)):
                for j in range(len(df11.columns)):
                    print(i, j)

        except:
            traceback.print_exc()

    def asd2(self, df11):
        try:
            print('---------------')
            np2 = df11.to_numpy()
            for i, val in enumerate(np2):
                for j, val2 in enumerate(val):
                    print(j,val2)
        except:
            traceback.print_exc()
    # def asd3(self,df11):
    #     print('---------------')
    #     try:
    #         np2 = df11.to_numpy()
    #         v,y=[val2 for i, val in enumerate(np2) for j, val2 in enumerate(val)]
    #             # for j, val2 in enumerate(val):
    #         print(v,y)
    #     except:
    #         traceback.print_exc()
        # ---------------------------------------- windowCode

    def windowCode(self):
        self.tab3_win2tableWidget = QtWidgets.QTableWidget(self.tab3_newWindow2)
        self.tab3_win2tableWidget.setGeometry(QtCore.QRect(0, 40, 571, 441))
        self.tab3_win2tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab3_win2tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab3_win2tableWidget.setAlternatingRowColors(True)
        self.tab3_win2tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tab3_win2tableWidget.setObjectName("tab3_win2tableWidget")
        self.tab3_win2tableWidget.setColumnCount(0)
        self.tab3_win2tableWidget.setRowCount(0)
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

        _translate = QtCore.QCoreApplication.translate

        self.tab3_win2tableWidget.setSortingEnabled(False)
        self.tab3_win2label.setText(_translate("MainWindow", "펀드검색"))
        self.tab3_win2pushButton.setText(_translate("MainWindow", "조회"))

        # QT디자이너 외 구현
        self.tab3_newWindow2.setWindowModality(QtCore.Qt.ApplicationModal)  # 하위창 컨트롤 금지
        self.tab3_newWindow2.resize(574, 482)
        self.newcreateTable(3, 2, '', '', '', '','')
        Ui_MainWindow.tab3SelectCode = ""
        self.tab3_lineEdit.setText("")
        self.tab3_newWindow2.show()

        # 이벤트
        self.tab3_win2lineEdit.textEdited.connect(lambda: self.newcreateTable(3, 2, "re", 1, '', '','')) # 펀드코드 검색
        self.tab3_win2lineEdit_2.textEdited.connect(lambda: self.newcreateTable(3, 2, "re", 2, '', '','')) # 펀드명 검색
        self.tab3_win2tableWidget.cellClicked.connect(self.tab3_win2SelectValue) #값 선택
        self.tab3_win2tableWidget.cellDoubleClicked.connect(lambda: self.tab3_win2Close(Ui_MainWindow.tab3SelectCode)) #값 넘김
        self.tab3_win2pushButton.clicked.connect(lambda: self.tab3_win2Close(Ui_MainWindow.tab3SelectCode)) #조회 버튼

    def tab3_win2SelectValue(self, row, col):
        """더블클릭 이벤트에 컬럼 좌표 입력이 별도로 없음"""
        Ui_MainWindow.tab3SelectCode = self.tab3_win2tableWidget.item(row, 0).text()

    def tab3_win2Close(self,fundCode):
        """창 종료"""
        self.tab3_lineEdit.setText(fundCode)
        self.newcreateTable(3, 0, '', '', '', '','')
        self.tab3_newWindow2.close()

    # ----------------------------------windowEarn

    def tab3_selectWindow(self,col,val,fundCode,fundName):
        """클릭 위치에 따라 다른 팝업"""
        try:
            if col == 4 and val != "None":  # null 필터링 하면 여기도 변경 필요
                sql = query.returnSQL('tab3_win3SearchQuery').format(fundCode)
                sql += "and rownum=1"
                cur.execute(sql)
                row = cur.fetchall()
                if row:
                    self.windowEarn(fundCode, fundName)

                else:
                    a = QMessageBox()
                    a.setText("자료가 없습니다.")
                    a.setStandardButtons(QMessageBox.Ok)
                    a.exec_()
            else:
                self.windowList(fundCode, fundName)
        except:
            traceback.print_exc()

    def windowEarn(self, fundCode, fundName):
        """수익자 팝업"""
        self.tab3_win3tableWidget = QtWidgets.QTableWidget(self.tab3_newWindow3)
        self.tab3_win3tableWidget.setGeometry(QtCore.QRect(0, 60, 901, 501))
        self.tab3_win3tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab3_win3tableWidget.setAlternatingRowColors(True)
        self.tab3_win3tableWidget.setObjectName("tab3_win3tableWidget")
        self.tab3_win3tableWidget.setColumnCount(0)
        self.tab3_win3tableWidget.setRowCount(0)
        self.tab3_win3label = QtWidgets.QLabel(self.tab3_newWindow3)
        self.tab3_win3label.setGeometry(QtCore.QRect(5, 10, 41, 20))
        self.tab3_win3label.setObjectName("tab3_win3label")
        self.tab3_win3label_2 = QtWidgets.QLabel(self.tab3_newWindow3)
        self.tab3_win3label_2.setGeometry(QtCore.QRect(53, 10, 271, 20))
        self.tab3_win3label_2.setAutoFillBackground(True)
        self.tab3_win3label_2.setText("")
        self.tab3_win3label_2.setObjectName("tab3_win3label_2")
        self.tab3_win3label_3 = QtWidgets.QLabel(self.tab3_newWindow3)
        self.tab3_win3label_3.setGeometry(QtCore.QRect(5, 32, 51, 20))
        self.tab3_win3label_3.setObjectName("tab3_win3label_3")
        self.tab3_win3comboBox = QtWidgets.QComboBox(self.tab3_newWindow3)
        self.tab3_win3comboBox.setGeometry(QtCore.QRect(56, 31, 121, 22))
        self.tab3_win3comboBox.setObjectName("tab3_win3comboBox")
        self.tab3_win3pushButton_2 = QtWidgets.QPushButton(self.tab3_newWindow3)
        self.tab3_win3pushButton_2.setGeometry(QtCore.QRect(740, 34, 51, 21))
        self.tab3_win3pushButton_2.setObjectName("tab3_win3pushButton_2")
        self.tab3_win3pushButton = QtWidgets.QPushButton(self.tab3_newWindow3)
        self.tab3_win3pushButton.setGeometry(QtCore.QRect(794, 34, 61, 21))
        self.tab3_win3pushButton.setObjectName("tab3_win3pushButton")
        self.tab3_win3dateEdit_2 = QtWidgets.QDateEdit(self.tab3_newWindow3)
        self.tab3_win3dateEdit_2.setEnabled(True)
        self.tab3_win3dateEdit_2.setGeometry(QtCore.QRect(460, 32, 91, 21))
        self.tab3_win3dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab3_win3dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.tab3_win3dateEdit_2.setCalendarPopup(True)
        self.tab3_win3dateEdit_2.setObjectName("tab3_win3dateEdit_2")
        self.tab3_win3checkBox_2 = QtWidgets.QCheckBox(self.tab3_newWindow3)
        self.tab3_win3checkBox_2.setGeometry(QtCore.QRect(440, 32, 16, 21))
        self.tab3_win3checkBox_2.setText("")
        self.tab3_win3checkBox_2.setChecked(True)
        self.tab3_win3checkBox_2.setObjectName("tab3_win3checkBox_2")
        self.tab3_win3dateEdit = QtWidgets.QDateEdit(self.tab3_newWindow3)
        self.tab3_win3dateEdit.setEnabled(True)
        self.tab3_win3dateEdit.setGeometry(QtCore.QRect(310, 32, 91, 21))
        self.tab3_win3dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab3_win3dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.tab3_win3dateEdit.setCalendarPopup(True)
        self.tab3_win3dateEdit.setObjectName("tab3_win3dateEdit")
        self.tab3_win3label_4 = QtWidgets.QLabel(self.tab3_newWindow3)
        self.tab3_win3label_4.setGeometry(QtCore.QRect(415, 32, 16, 21))
        self.tab3_win3label_4.setObjectName("tab3_win3label_4")
        self.tab3_win3checkBox = QtWidgets.QCheckBox(self.tab3_newWindow3)
        self.tab3_win3checkBox.setGeometry(QtCore.QRect(290, 32, 16, 21))
        self.tab3_win3checkBox.setText("")
        self.tab3_win3checkBox.setChecked(True)
        self.tab3_win3checkBox.setObjectName("tab3_win3checkBox")
        self.tab3_win3pushButton_3 = QtWidgets.QPushButton(self.tab3_newWindow3)
        self.tab3_win3pushButton_3.setGeometry(QtCore.QRect(859, 34, 41, 21))
        self.tab3_win3pushButton_3.setObjectName("tab3_win3pushButton_3")
        self.tab3_win3label_5 = QtWidgets.QLabel(self.tab3_newWindow3)
        self.tab3_win3label_5.setGeometry(QtCore.QRect(189, 33, 31, 20))
        self.tab3_win3label_5.setObjectName("tab3_win3label_5")
        self.tab3_win3comboBox_2 = QtWidgets.QComboBox(self.tab3_newWindow3)
        self.tab3_win3comboBox_2.setGeometry(QtCore.QRect(220, 32, 51, 22))
        self.tab3_win3comboBox_2.setObjectName("tab3_win3comboBox_2")

        _translate = QtCore.QCoreApplication.translate

        self.tab3_win3tableWidget.setSortingEnabled(False)
        self.tab3_win3label.setText(_translate("tab3_win3ammain", "펀드명:"))
        self.tab3_win3label_3.setText(_translate("tab3_win3ammain", "수익자"))
        self.tab3_win3pushButton_2.setText(_translate("tab3_win3ammain", "그래프"))
        self.tab3_win3pushButton.setText(_translate("tab3_win3ammain", "엑셀 변환"))
        self.tab3_win3label_4.setText(_translate("tab3_win3ammain", "~"))
        self.tab3_win3pushButton_3.setText(_translate("tab3_win3ammain", "조회"))
        self.tab3_win3label_5.setText(_translate("tab3_win3ammain", "구좌"))

        # QT디자이너 외 구현
        self.tab3_newWindow3.resize(901, 561)
        self.tab3_win3label_2.setText(fundName)
        self.newcreateTable(3, 3, '', '', '','', fundCode)
        self.tab3_newWindow3.setWindowModality(QtCore.Qt.ApplicationModal)  # 하위창 컨트롤 금지
        if Ui_MainWindow.version != "xe" and len(Ui_MainWindow.mainWindow_df3_3) > 0:
            self.tab3_win3dateEdit.setDate(Ui_MainWindow.mainWindow_df3_3['기준일자'].min())
        else:
            self.tab3_win3dateEdit.setDate(date.today() - timedelta(1))
        self.tab3_win3dateEdit_2.setDate(date.today() - timedelta(1))
        self.tab3_newWindow3.show()

        # 이벤트
        self.tab3_win3pushButton_3.clicked.connect(
            lambda: self.newcreateTable(3, 3, "re", self.tab3_win3comboBox.currentText(),
                                        self.tab3_win3comboBox_2.currentText(),'', fundCode)) # 조회 버튼
        self.tab3_win3comboBox.currentTextChanged.connect(lambda: self.tab3_win3ChangeSelectComboBox(fundCode)) # 구좌항목 변경
        self.tab3_win3pushButton_2.clicked.connect(lambda: self.windowGraphic("3", "3"))  # 그래픽 팝업 버튼
        self.tab3_win3pushButton.clicked.connect(
            lambda: self.toExcel("3", "3", self.tab3_win3label_2.text()))  # 엑셀변환 버튼
        self.tab3_win3checkBox.stateChanged.connect(lambda: self.ckeckedTab3_Win3checkBox(1)) # 날짜조회 활성/비활성화
        self.tab3_win3checkBox_2.stateChanged.connect(lambda: self.ckeckedTab3_Win3checkBox(2)) # 날짜조회 활성/비활성화

    def ckeckedTab3_Win3checkBox(self, val):
        """일별검색 활성화"""
        if val == 1:
            if self.tab3_win3checkBox.isChecked():
                self.tab3_win3dateEdit.setEnabled(True)
            else:
                self.tab3_win3dateEdit.setEnabled(False)
        elif val == 2:
            if self.tab3_win3checkBox_2.isChecked():
                self.tab3_win3dateEdit_2.setEnabled(True)
            else:
                self.tab3_win3dateEdit_2.setEnabled(False)

    def tab3_win3ChangeSelectComboBox(self, fundCode):
        """콤보박스 값 동적입력"""
        try:
            self.tab3_win3checkBox.setChecked(False)
            self.tab3_win3checkBox_2.setChecked(False)
            self.tab3_win3dateEdit.setEnabled(False)
            self.tab3_win3dateEdit_2.setEnabled(False)
            if self.tab3_win3comboBox.currentText() != '전체':
                sql = query.returnSQL('tab3_win3ChangeSelectComboBox').format(fundCode, self.tab3_win3comboBox.currentText())
                cur.execute(sql)
                row = cur.fetchmany(Ui_MainWindow.maxSearch)
                df = pd.DataFrame(row)
                self.tab3_win3comboBox_2.clear()
                self.tab3_win3comboBox_2.addItem('전체')
                [self.tab3_win3comboBox_2.addItem(str(j)) for j in df[0]]

            else:
                self.tab3_win3comboBox_2.clear()
        except:
            traceback.print_exc()

    def tab5_win1SearchValue(self):
        """탭5 팝업 생성"""
        if Ui_MainWindow.tab5group!='합계' and Ui_MainWindow.tab5team:
            self.windowGroup(self.tab5_dateEdit.text(),Ui_MainWindow.tab5group,Ui_MainWindow.tab5team)

    def tab5_returnCode(self, row, col):
        """ 팝업으로 넘길 그룹명,팀. 더블클릭 이벤트에는 클릭값 받는 인자가 없음"""
        try:
            if col>=2 and col<=5:
                Ui_MainWindow.tab5team='1본부'
                Ui_MainWindow.tab5group = self.tab5_tableWidget.item(row, 0).text()
            elif col>=7 and col<=10:
                Ui_MainWindow.tab5team='2본부'
                Ui_MainWindow.tab5group=self.tab5_tableWidget.item(row, 0).text()
            else:
                Ui_MainWindow.tab5team=''
                Ui_MainWindow.tab5group=''
        except:
            traceback.print_exc()
    # ----------------------------windowGroup

    def windowGroup(self,date1,group,team):
        self.tab5_win1tableWidget = QtWidgets.QTableWidget(self.tab5_newWindow1)
        self.tab5_win1tableWidget.setGeometry(QtCore.QRect(0, 80, 741, 381))
        self.tab5_win1tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab5_win1tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab5_win1tableWidget.setAlternatingRowColors(True)
        self.tab5_win1tableWidget.setObjectName("tab5_win1tableWidget")
        self.tab5_win1tableWidget.setColumnCount(0)
        self.tab5_win1tableWidget.setRowCount(0)
        self.tab5_win1label_4 = QtWidgets.QLabel(self.tab5_newWindow1)
        self.tab5_win1label_4.setGeometry(QtCore.QRect(190, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(11)
        self.tab5_win1label_4.setFont(font)
        self.tab5_win1label_4.setObjectName("tab5_win1label_4")
        self.tab5_win1label_5 = QtWidgets.QLabel(self.tab5_newWindow1)
        self.tab5_win1label_5.setGeometry(QtCore.QRect(510, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(11)
        self.tab5_win1label_5.setFont(font)
        self.tab5_win1label_5.setObjectName("tab5_win1label_5")
        self.tab5_win1label_2 = QtWidgets.QLabel(self.tab5_newWindow1)
        self.tab5_win1label_2.setGeometry(QtCore.QRect(680, 60, 61, 21))
        self.tab5_win1label_2.setObjectName("tab5_win1label_2")
        self.tab5_win1label = QtWidgets.QLabel(self.tab5_newWindow1)
        self.tab5_win1label.setGeometry(QtCore.QRect(160, 10, 51, 21))
        self.tab5_win1label.setObjectName("tab5_win1label")
        self.tab5_win1dateEdit = QtWidgets.QDateEdit(self.tab5_newWindow1)
        self.tab5_win1dateEdit.setGeometry(QtCore.QRect(200, 10, 91, 22))
        self.tab5_win1dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab5_win1dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.tab5_win1dateEdit.setCalendarPopup(True)
        self.tab5_win1dateEdit.setObjectName("tab5_win1dateEdit")
        self.tab5_win1comboBox = QtWidgets.QComboBox(self.tab5_newWindow1)
        self.tab5_win1comboBox.setGeometry(QtCore.QRect(40, 10, 111, 22))
        self.tab5_win1comboBox.setObjectName("tab5_win1comboBox")
        self.tab5_win1label_3 = QtWidgets.QLabel(self.tab5_newWindow1)
        self.tab5_win1label_3.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.tab5_win1label_3.setObjectName("tab5_win1label_3")
        self.tab5_win1pushButton = QtWidgets.QPushButton(self.tab5_newWindow1)
        self.tab5_win1pushButton.setGeometry(QtCore.QRect(680, 10, 51, 21))
        self.tab5_win1pushButton.setObjectName("tab5_win1pushButton")

        _translate = QtCore.QCoreApplication.translate

        self.tab5_win1tableWidget.setSortingEnabled(False)
        self.tab5_win1label_4.setText(_translate("MainWindow", "홀세일 1본부"))
        self.tab5_win1label_5.setText(_translate("MainWindow", "홀세일 2본부"))
        self.tab5_win1label_2.setText(_translate("MainWindow", "(단위: 억)"))
        self.tab5_win1label.setText(_translate("MainWindow", "기준일"))
        self.tab5_win1label_3.setText(_translate("MainWindow", "고객"))
        self.tab5_win1pushButton.setText(_translate("MainWindow", "조회"))

        # QT디자이너 외 구현
        self.newcreateTable(5, 1, '',date1,group,team,'')
        # self.tab5_win1dateEdit.setDate(datetime.datetime.strptime(date1,'%y-%m-%d'))
        # date,group,team
        # print(datetime.strptime('2021-11-28','%y%m%d'))
        self.tab5_newWindow1.show()

        # 이벤트

    # ----------------------------공통

    def newcreateTable(self, tab, win, re, val1, val2, val3, fundCode):
        """탭순서,새창순서,재조회여부,아무변수,아무변수2,펀드코드가 들어옴"""
        startTime = time.time()
        sql = ""
        a = QMessageBox()
        if tab == 1 and win == 0:
            try:
                if self.tab1_listWidget.currentItem():
                    Ui_MainWindow.selectedTable = self.tab1_listWidget.currentItem().text()
                    sqlValue = self.searchValue()
                    if sqlValue:
                        header = self.searchColumn()
                        df = pd.DataFrame(sqlValue)
                        df.columns = header
                        self.tab1_tableWidget.clear()
                        self.tab1_tableWidget.setColumnCount(len(df.columns))
                        self.tab1_tableWidget.setRowCount(len(df.index))
                        self.tab1_tableWidget.setHorizontalHeaderLabels(header)
                        self.setTableData(df, 1, 0, startTime, '')
                        Ui_MainWindow.mainWindow_df1_0 = df
                        self.tab1_tableWidget.resizeColumnsToContents()  # 셀 크기를 내용길이와 같게
                    else:
                        self.tab1_tableWidget.clear()
                        self.tab1_tableWidget.setRowCount(0)
                        self.tab1_label_2.setText("")
                        self.tab1_label_5.setText(Ui_MainWindow.selectedTable)
                        self.tab1_label_7.setText("0 / 전체:0")
                        self.tab1_label_9.setText("")
                        self.tab1_label_11.setText("")
                        self.tab1_pushButton_3.setDisabled(True)
                        self.tab1_pushButton_4.setDisabled(True)
                else:
                    self.tab1_label_5.setText("없음")
                self.tab1_label_2.setText("")
            except:
                traceback.print_exc()

        elif tab == 2 and win == 0:
            try:
                df2=val1
                self.tab2_tableWidget.setColumnCount(len(df2.columns))
                self.tab2_tableWidget.setRowCount(len(df2.index))
                self.tab2_tableWidget.setHorizontalHeaderLabels(df2.columns)
                self.setTableData(df2, 2, 0, startTime, '')
                self.tab2_tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정
            except:
                traceback.print_exc()

        elif tab == 3 and win == 0:
            try:
                header = ['기준일', '펀드코드', '펀드명', '수익자구분', '수익자', '펀드종류구분', '펀드유형', '일임_자문', '공모사모구분', '국내/해외', '모자구분',
                          '종류형구분', '펀드구분', '적용법률', '자통법적용일', '최초설정일자', '운용개시일',
                          '다음결산일', '상환일', '다음보수인출일',
                          '판매보수', '운용보수', '사무관리보수', '수탁보수', '펀드평가보수', '자산관리보수', '상품관리보수', '성과보수', '성과보수여부', 'Total', '설정액',
                          '설정좌수', '총자산', '순자산', '기준가', '누적수익지수', '펀드약명',
                          '영문명', '운용역', '운용사명', '수탁은행', '수탁사명', '사무수탁사명', '펀드평가사', '판매사갯수', '판매사명', '협회표준코드', '금감원코드',
                          '예탁원펀드코드', '예탁원종목코드', '상품분류코드',
                          '상품분류2차', '집합투자기구분류',
                          '펀드결제수수료여부', '분배방식', '당기결산방식', '시가평가여부', '장단기구분', '국외세액환급여부', '이관일', '이수일', '투자자', '부사무관리사명',
                          '해외전용과표가격대상여부', '해외전용과표가격적용일',
                          '설정대금확정일1', '설정일1', '환매대금확정일1', '환매일1', '환매대금확정일2', '환매일2', 'BM명', 'GIPS펀드유형', '채권평가사보수유예시작일',
                          '채권평가사보수유예종료일', '배당기준운용사',
                          '신주인수권증서평가기준(폐지일)', '공모청약수수료기준', '단위형구분', '수익차등여부', '사모분류', '일반투자자포함여부']
                alignRight = ['20', '21', '22', '23', '24', '25', '26', '27', '29', '30', '31', '32', '33','34']  # 오른쪽 정렬할 컬럼순서들
                sqlValue = self.tab3_searchValue()
                df = pd.DataFrame(sqlValue)
                df.columns = header
                self.tab3_tableWidget.setColumnCount(len(df.columns))
                self.tab3_tableWidget.setRowCount(len(df.index))
                self.tab3_tableWidget.setHorizontalHeaderLabels(header)
                self.setTableData(df, 3, 0, startTime, alignRight)
                self.tab3_tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정
            except:
                traceback.print_exc()

        elif tab == 3 and win == 1:
            header = ['기준일자', '기준가격', '전일대비', '설정금액', '설정좌수', '당일설정좌수', '당일해지좌수', '좌수증감', '총자산', '총자산일간변동', '순자산',
                      '순자산일간변동']
            try:
                if re == "":
                    sql += query.returnSQL('tab3_win1SearchQuery').format(fundCode)
                    print(sql)
                    cur.execute(sql)
                    row = cur.fetchall()
                    df = pd.DataFrame(row)
                elif re == "re":
                    minDate = self.tab3_win1dateEdit.text()
                    maxDate = self.tab3_win1dateEdit_2.text()
                    df = Ui_MainWindow.mainWindow_df3_1
                    if self.tab3_win1checkBox.isChecked():
                        df = df.query('기준일자>=@minDate')
                    if self.tab3_win1checkBox_2.isChecked():
                        df = df.query('기준일자<=@maxDate')
                if row:
                    df.columns = header
                    self.tab3_win1tableWidget.setColumnCount(len(df.columns))
                    self.tab3_win1tableWidget.setRowCount(len(df.index))
                    self.tab3_win1tableWidget.setHorizontalHeaderLabels(header)
                    self.setTableData(df, 3, 1, startTime, '')
                    if re == "":
                        Ui_MainWindow.mainWindow_df3_1 = df
                    Ui_MainWindow.mainWindow_df3_1Re = df
                    self.tab3_win1tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정
                else:
                    a.setText("값이 없습니다")
                    a.setStandardButtons(QMessageBox.Ok)
                    a.exec_()
            except:
                traceback.print_exc()

        elif tab == 3 and win == 2:
            header = ['펀드코드', '펀드명']
            try:
                if re == "":
                    sql += query.returnSQL('tab3_win2SearchQuery')
                    cur.execute(sql)
                    row = cur.fetchall()
                    df = pd.DataFrame(row)
                elif re == "re":
                    if val1 == 1:
                        self.tab3_win2lineEdit_2.setText("")
                        df = Ui_MainWindow.mainWindow_df3_2[
                            Ui_MainWindow.mainWindow_df3_2['펀드코드'].str.contains(self.tab3_win2lineEdit.text())]
                    elif val1 == 2:
                        self.tab3_win2lineEdit.setText("")
                        df = Ui_MainWindow.mainWindow_df3_2[
                            Ui_MainWindow.mainWindow_df3_2['펀드명'].str.contains(self.tab3_win2lineEdit_2.text())]
                df.columns = header
                self.tab3_win2tableWidget.setColumnCount(len(df.columns))
                self.tab3_win2tableWidget.setRowCount(len(df.index))
                self.tab3_win2tableWidget.setHorizontalHeaderLabels(header)
                self.setTableData(df, 3, 2, '', '')
                if re == "":
                    Ui_MainWindow.mainWindow_df3_2 = df
                Ui_MainWindow.mainWindow_df3_2Re = df
                self.tab3_win2tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정

            except:
                traceback.print_exc()

        elif tab == 3 and win == 3:
            alignRight = ['3', '4']  # 오른쪽 정렬할 숫자값들
            header = ['기준일자', '그룹', '수익자명', '구좌', '설정자산', '자산증감', '설정좌수', '좌수증감', '판매사']
            if val1=='전체' and val2=='':
                re=''
            try:
                if re == "":
                    sql += query.returnSQL('tab3_win3SearchQuery').format(fundCode)
                    print(sql)
                    cur.execute(sql)
                    row = cur.fetchall()
                    df = pd.DataFrame(row)
                    df.columns = header
                    self.tab3_win3tableWidget.setColumnCount(len(df.columns))
                    self.tab3_win3tableWidget.setRowCount(len(df.index))
                    self.tab3_win3tableWidget.setHorizontalHeaderLabels(header)
                    self.setTableData(df, 3,3, '', alignRight)

                elif re == "re":
                    minDate = self.tab3_win3dateEdit.text()
                    maxDate = self.tab3_win3dateEdit_2.text()
                    if val1 != '전체':
                        df = Ui_MainWindow.mainWindow_df3_3
                        if self.tab3_win3checkBox.isChecked():
                            df = df.query('기준일자>=@minDate')
                        if self.tab3_win3checkBox_2.isChecked():
                            df = df.query('기준일자<=@maxDate')
                        df = df.query('수익자명==@val1')
                        if val2 != '전체':
                            val2 = int(val2)
                            df = df.query('구좌==@val2')
                        df.columns = header
                        self.tab3_win3tableWidget.setColumnCount(len(df.columns))
                        self.tab3_win3tableWidget.setRowCount(len(df.index))
                        self.tab3_win3tableWidget.setHorizontalHeaderLabels(header)
                        self.setTableData(df, 3, 3, '', alignRight)
                        Ui_MainWindow.mainWindow_df3_3Re = df
                if re == "":
                    self.tab3_win3comboBox.addItem("전체")
                    groupd = df.groupby(['수익자명']).count().iloc[:, 0]
                    [self.tab3_win3comboBox.addItem(str(i)) for i in groupd.index]
                    self.tab3_win3comboBox_2.addItem('전체')
                    Ui_MainWindow.mainWindow_df3_3 = df
                    Ui_MainWindow.mainWindow_df3_3Re = df
                self.tab3_win3tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정
            except:
                if row:
                    a = QMessageBox()
                    a.setText("값이 없습니다.")
                    a.setStandardButtons(QMessageBox.Ok)
                    a.exec_()
                traceback.print_exc()

        elif tab == 4 and win == 0:
            header = ['일자','수익그룹','수익자명','구좌','설정금액','증감','본부','고객그룹','유형']
            try:
                if re == "":
                    sql += query.returnSQL('tab4_searchQuery').format(self.tab4_dateEdit.text().replace('-', '/'),self.tab4_dateEdit_2.text().replace('-', '/'))
                    print(sql)
                    cur.execute(sql)
                    row = cur.fetchall()
                    df = pd.DataFrame(row)
                # elif re == "re":
                #     if val1 == 1:
                #         self.tab3_win2lineEdit_2.setText("")
                #         df = Ui_MainWindow.mainWindow_df3_2[
                #             Ui_MainWindow.mainWindow_df3_2['펀드코드'].str.contains(self.tab3_win2lineEdit.text())]
                #     elif val1 == 2:
                #         self.tab3_win2lineEdit.setText("")
                #         df = Ui_MainWindow.mainWindow_df3_2[
                #             Ui_MainWindow.mainWindow_df3_2['펀드명'].str.contains(self.tab3_win2lineEdit_2.text())]
                if row:
                    df.columns = header
                    self.tab4_tableWidget.setColumnCount(len(df.columns))
                    self.tab4_tableWidget.setRowCount(len(df.index))
                    self.tab4_tableWidget.setHorizontalHeaderLabels(header)
                    self.setTableData(df, 4, 0, startTime, '')
                    if re == "":
                        Ui_MainWindow.mainWindow_df4_0 = df
                    self.tab4_tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정
                else:
                    a.setText("값이 없습니다")
                    a.setStandardButtons(QMessageBox.Ok)
                    a.exec_()
            except:
                traceback.print_exc()

        elif tab == 5 and win == 0:
            header = ['고객그룹','설정액 합','설정액','전월말대비','전분기말대비','전년말대비','','설정액','전월말대비','전분기말대비','전년말대비']
            try:
                if re == "":
                    sql += query.returnSQL('tab5_searchQuery').format(self.tab5_dateEdit.text(),self.tab5_dateEdit.text(),
                                                                      self.tab5_dateEdit.text(),self.tab5_dateEdit.text(),
                                                                      self.tab5_dateEdit.text(),self.tab5_dateEdit.text(),
                                                                      self.tab5_dateEdit.text(),self.tab5_dateEdit.text(),
                                                                      self.tab5_dateEdit.text(),self.tab5_dateEdit.text()
                                                                      )
                    print(sql)
                    cur.execute(sql)
                    row = cur.fetchall()
                    df = pd.DataFrame(row)
                # elif re == "re":
                #     if val1 == 1:
                #         self.tab3_win2lineEdit_2.setText("")
                #         df = Ui_MainWindow.mainWindow_df3_2[
                #             Ui_MainWindow.mainWindow_df3_2['펀드코드'].str.contains(self.tab3_win2lineEdit.text())]
                #     elif val1 == 2:
                #         self.tab3_win2lineEdit.setText("")
                #         df = Ui_MainWindow.mainWindow_df3_2[
                #             Ui_MainWindow.mainWindow_df3_2['펀드명'].str.contains(self.tab3_win2lineEdit_2.text())]
                if row:
                    df.columns = header
                    self.tab5_tableWidget.setColumnCount(len(df.columns))
                    self.tab5_tableWidget.setRowCount(len(df.index))
                    self.tab5_tableWidget.setHorizontalHeaderLabels(header)
                    self.setTableData(df, 5, 0, startTime, '')
                    if re == "":
                        Ui_MainWindow.mainWindow_df5_0 = df
                    self.tab5_tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정
                else:
                    a.setText("값이 없습니다")
                    a.setStandardButtons(QMessageBox.Ok)
                    a.exec_()
            except:
                traceback.print_exc()
        elif tab == 5 and win == 1:
            #val1=date1,val2=group,val3=team
            header = ['유형','설정액','순자산','전월말대비','전분기말대비','전년말대비','전전년말대비','','전월말','전분기말','전년말','전전년말']
            try:
                if re == "":
                    sql += query.returnSQL('tab5_win1searchQuery').format(val1,val2,val3,
                                                                          val1,val2,val3,
                                                                          val1,val1,val2,val3,
                                                                          val1,val2,val3,
                                                                          val1,val2,val3,
                                                                          val1,val2,val3,
                                                                          val1,val2,val3,
                                                                          val1,val1,val2,val3,
                                                                          val1,val2,val3,
                                                                          val1,val2,val3)
                    print(sql)
                    cur.execute(sql)
                    row = cur.fetchall()
                    df = pd.DataFrame(row)
                # elif re == "re":
                #     if val1 == 1:
                #         self.tab3_win2lineEdit_2.setText("")
                #         df = Ui_MainWindow.mainWindow_df3_2[
                #             Ui_MainWindow.mainWindow_df3_2['펀드코드'].str.contains(self.tab3_win2lineEdit.text())]
                #     elif val1 == 2:
                #         self.tab3_win2lineEdit.setText("")
                #         df = Ui_MainWindow.mainWindow_df3_2[
                #             Ui_MainWindow.mainWindow_df3_2['펀드명'].str.contains(self.tab3_win2lineEdit_2.text())]
                if row:
                    df.columns = header
                    self.tab5_win1tableWidget.setColumnCount(len(df.columns))
                    self.tab5_win1tableWidget.setRowCount(len(df.index))
                    self.tab5_win1tableWidget.setHorizontalHeaderLabels(header)
                    self.setTableData(df, 5, 1, startTime, '')
                    if re == "":
                        Ui_MainWindow.mainWindow_df5_1 = df
                    self.tab5_win1tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정
                else:
                    a.setText("값이 없습니다")
                    a.setStandardButtons(QMessageBox.Ok)
                    a.exec_()
            except:
                traceback.print_exc()


    def setTableData(self, df, tab, win, startTime, alignRight):
        """for로 돌리면서 표에 값을 입력, Null값 따로 변환안함"""
        try:
            nArray = df.to_numpy()
            if tab == 1 and win == 0:
                for i, arr in enumerate(nArray):
                    [self.tab1_tableWidget.setItem(i, j, QTableWidgetItem(str(val))) for j, val in enumerate(arr)]
            elif tab == 2 and win == 0:
                for i, arr in enumerate(nArray):
                    [self.tab2_tableWidget.setItem(i, j, QTableWidgetItem(str(val))) for j, val in enumerate(arr)]
            elif tab == 3 and win == 0:
                for i, arr in enumerate(nArray):
                    for j, val in enumerate(arr):
                        self.tab3_tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                        if str(j) in alignRight:
                            self.tab3_tableWidget.item(i, j).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            elif tab == 3 and win == 1:
                for i, arr in enumerate(nArray):
                    for j, val in enumerate(arr):
                        if self.isFloat(val) != 0 or val == 0:
                            self.tab3_win1tableWidget.setItem(i, j, QTableWidgetItem(self.setComma(str(val))))
                            self.tab3_win1tableWidget.item(i, j).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                            if float(val) < 0:
                                self.tab3_win1tableWidget.item(i, j).setBackground(Ui_MainWindow.color)
                        else:
                            self.tab3_win1tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            elif tab == 3 and win == 2:
                for i, arr in enumerate(nArray):
                    [self.tab3_win2tableWidget.setItem(i, j, QTableWidgetItem(str(val))) for j, val in enumerate(arr)]
            elif tab == 3 and win == 3:
                for i, arr in enumerate(nArray):
                    for j, val in enumerate(arr):
                        if self.isFloat(val) != 0 or val == 0:
                            self.tab3_win3tableWidget.setItem(i, j, QTableWidgetItem(self.setComma(str(val))))
                            self.tab3_win3tableWidget.item(i, j).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                            if float(val) < 0:
                                self.tab3_win3tableWidget.item(i, j).setBackground(Ui_MainWindow.color)
                        else:
                            self.tab3_win3tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            elif tab == 4 and win == 0:
                for i, arr in enumerate(nArray):
                    [self.tab4_tableWidget.setItem(i, j, QTableWidgetItem(str(val))) for j, val in enumerate(arr)]
            elif tab == 5 and win == 0:
                for i, arr in enumerate(nArray):
                    for j, val in enumerate(arr):
                        if j!=6:
                            self.tab5_tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                            self.tab5_tableWidget.item(i, j).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            elif tab == 5 and win == 1:
                for i, arr in enumerate(nArray):
                    for j, val in enumerate(arr):
                        if j!=7:
                            self.tab5_win1tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                            self.tab5_win1tableWidget.item(i, j).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)


            if startTime:
                endTime = time.time()
                loadTime = round(endTime - startTime, 3)
            if tab == 1 and win == 0:
                self.tab1_label_13.setText(str(loadTime) + "초")
                self.tab1_label_2.setText("")
                self.tab1_label_5.setText(Ui_MainWindow.selectedTable)
                self.tab1_label_7.setText(str(len(df.index)) + " / 전체:" + self.tableCount())
                self.tab1_label_9.setText("")
                self.tab1_label_11.setText("")
                self.tab1_pushButton_3.setDisabled(False)
                self.tab1_pushButton_4.setDisabled(False)
                self.tab1_pushButton_4.setDisabled(False)
            elif tab == 2 and win == 0:
                self.tab2_label.setText(str(loadTime) + "초")
            elif tab == 3 and win == 0:
                self.tab3_label_13.setText(str(loadTime) + "초")
                self.tab3_label_16.setText(str(self.tab3_tableWidget.rowCount()))
            elif tab == 3 and win == 1:
                self.tab3_win1label_9.setText(str(loadTime) + "초")
                self.tab3_win1label_10.setText(str(self.tab3_win1tableWidget.rowCount()))
            elif tab == 4 and win == 0:
                self.tab4_label_4.setText(str(loadTime) + "초")
                self.tab4_label_6.setText(str(self.tab4_tableWidget.rowCount()))

        except:
            traceback.print_exc()

    def setComma(self, val):
        """1000 단위 콤마 붙여서 리턴"""
        try:
            if len(str(val)) >= Ui_MainWindow.commaLength:
                val = format(float(val), ",")
            return val
        except:
            traceback.print_exc()

    def delComma(self, val):
        """1000 단위 콤마 제거해서 리턴"""
        val = val.replace(',', '')
        return val

    def toExcel(self, tab, win, title):
        """엑셀 변환 저장 tab은 탭, win은 창 번호(메인은 0) 저장시 셀칸 늘리는건 해결 못 함"""
        try:
            a = QMessageBox()
            if tab == "1" and win == "0":
                rowCount = len(Ui_MainWindow.mainWindow_df1_0)
            elif tab == "3" and win == "1":
                rowCount = len(Ui_MainWindow.mainWindow_df3_1Re)
            elif tab == "3" and win == "3":
                rowCount = len(Ui_MainWindow.mainWindow_df3_3Re)
            if rowCount > 0:
                excelfolder = QFileDialog.getExistingDirectory(self.tab1, '폴더 지정', 'C:\\Users\\User\\Desktop')
                # excelfolder = QFileDialog.getSaveFileName(self.tab1, "저장","C:\\'", "excel File(*.xlsx)") 파일명 지정은 나중에 구현
                filename = date.today().strftime("%Y%m%d") + "_" + title
                excelPath = (excelfolder + "/" + filename + ".xlsx")
                if excelfolder:
                    if tab == "1" and win == "0":
                        Ui_MainWindow.mainWindow_df1_0.to_excel(excelPath)  # 엑셀 생성
                    elif tab == "3" and win == "1":
                        Ui_MainWindow.mainWindow_df3_1Re.to_excel(excelPath)
                    elif tab == "3" and win == "3":
                        Ui_MainWindow.mainWindow_df3_3Re.to_excel(excelPath)
                    if os.path.exists(excelPath):
                        a.setText("경로: " + excelPath + "\n\n엑셀파일 생성 완료")
                    else:
                        a.setText("파일이 생성되지 않았습니다")
                    a.setStandardButtons(QMessageBox.Ok)
                    a.exec_()
            else:
                a.setText("변환할 자료가 없습니다")
                a.setStandardButtons(QMessageBox.Ok)
                a.exec_()
        except:
            traceback.print_exc()
            a.setText("파일 생성 중 에러가 발생했습니다. 다른 저장경로로 지정하세요")
            a.setStandardButtons(QMessageBox.Ok)
            a.exec_()

    def isFloat(self, par):
        """정수, 소수만 소수타입으로 변환해 부동소수점 문제 해결하고 리턴 그 외에는 0리턴"""
        basischk = 0
        numeric = False
        returnvalue = 0
        value = list(str(par))

        for idx, val in enumerate(value):
            if idx == 0:
                if len(value) == 1 and val.isdigit() == True:
                    numeric = True
                    break
                elif val == '-' or val.isdigit() == True:
                    continue
                else:
                    break
            elif idx == len(value) - 1 and val.isdigit() == True:
                numeric = True
            else:
                if val.isdigit() == True:
                    continue
                elif val == "." and basischk == 0:
                    basischk = +1
                else:
                    break
        if numeric == True:
            returnvalue = decimal.Decimal(par)
        return returnvalue
       # ---------------------------------팝업

    def popup1(self,update):
        self.popup1_label = QtWidgets.QLabel(self.popup_version)
        self.popup1_label.setGeometry(QtCore.QRect(98, 13, 81, 21))
        self.popup1_label.setObjectName("popup1_label")
        self.popup1_label_2 = QtWidgets.QLabel(self.popup_version)
        self.popup1_label_2.setGeometry(QtCore.QRect(180, 14, 81, 21))
        self.popup1_label_2.setText("")
        self.popup1_label_2.setObjectName("popup1_label_2")
        self.popup1_label_3 = QtWidgets.QLabel(self.popup_version)
        self.popup1_label_3.setGeometry(QtCore.QRect(98, 33, 41, 21))
        self.popup1_label_3.setObjectName("popup1_label_3")
        self.popup1_label_4 = QtWidgets.QLabel(self.popup_version)
        self.popup1_label_4.setGeometry(QtCore.QRect(140, 33, 41, 21))
        self.popup1_label_4.setObjectName("popup1_label_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.popup_version)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1, 4, 71, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.popup1_label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.popup1_label_5.setText("")
        self.popup1_label_5.setObjectName("popup1_label_5")
        self.verticalLayout_2.addWidget(self.popup1_label_5)

        _translate = QtCore.QCoreApplication.translate

        self.popup1_label.setText(_translate("MainWindow", "최신 업데이트:"))
        self.popup1_label_3.setText(_translate("MainWindow", "개발자:"))
        self.popup1_label_4.setText(_translate("MainWindow", "송병규"))


        # Qt디자이너 외 구현
        self.popup_version.resize(274, 69)
        self.popup1_label_2.setText(update)
        pixmap = QtGui.QPixmap(resource_path('ci.jpg'))
        pixmap=pixmap.scaledToHeight(int(60))
        self.popup1_label_5.setPixmap(pixmap)

        self.popup_version.show()

    # ---------------------------------------main


if __name__ == '__main__':
    conn = cx_Oracle.connect("system", "1234", "localhost:1521/xe")
    Ui_MainWindow.version = (str(conn)[-3:-1])
    cur = conn.cursor()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# 현재 setcomma에서 length 값 이하는 표시가 안되고 그걸 내리면 더블클릭시 코드값을 잘못 가져감
# 코드값 같은 특정 헤더명으로 콤마를 안 걸게 하는 방법 찾아야함
# conn = cx_Oracle.connect("HKCL", "hkcl", "11.10.5.11:1521/hkfund")
# conn = cx_Oracle.connect("system", "1234", "localhost:1521/xe")
# pyuic5 -x mainFrame.ui -o mainFrame.py
# pyuic5 -x windowGraphic.ui -o windowGraphic.py
# pyuic5 -x windowQuery.ui -o windowQuery.py
# pyuic5 -x windowList.ui -o windowList.py
# pyuic5 -x windowCode.ui -o windowCode.py
# pyuic5 -x windowEarn.ui -o windowEarn.py
# pyuic5 -x popupVersion.ui -o popupVersion.py
# pyuic5 -x windowGroup.ui -o windowGroup.py

# pyuic5 -x suikja_layout.ui -o suikja_layout.py
# gcc -c clang.c
# gcc -o clang.so -shared -f PIC clang.c