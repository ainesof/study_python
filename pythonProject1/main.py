import time, datetime
from datetime import date, timedelta
import math, decimal, os.path, sys, traceback, webbrowser, urllib, atexit, socket
import cx_Oracle, query
import matplotlib.pyplot as plt
import pandas as pd
import requests, bs4
import multiprocessing as mp
from styleframe import StyleFrame, Styler, utils
from dateutil.parser import parse
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon, QPainter, QFont, QPen, QBrush, QPainterPath
from PyQt5.QtWidgets import *
import json
from collections import OrderedDict
import ctypes

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


# @@@
class f(mp.Process):
    """멀티프로세싱 테스트"""

    # def __init__(self, id):
    #     super(f, self).__init__()
    #     self.id = id

    def worker(self):
        try:
            while (True):
                now = datetime.datetime.now()
                print(now.strftime('%H:%M:%S'))
                time.sleep(1)
                return now
        except:
            print('종료')


def sumtest(a, b):
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S'))
    time.sleep(1)
    return a + b


def times():
    while (True):
        now = datetime.datetime.now()
        print(now.strftime('%H:%M:%S'))
        time.sleep(1)


class Ui_MainWindow(object):
    def __init__(self):
        self.fig = plt.Figure()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 581)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1081, 541))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")
        self.tab5_tableWidget = QtWidgets.QTableWidget(self.tab5)
        self.tab5_tableWidget.setGeometry(QtCore.QRect(0, 70, 1071, 441))
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
        self.tab5_label_3 = QtWidgets.QLabel(self.tab5)
        self.tab5_label_3.setGeometry(QtCore.QRect(1000, 520, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab5_label_3.setFont(font)
        self.tab5_label_3.setText("")
        self.tab5_label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab5_label_3.setObjectName("tab5_label_3")
        self.tab5_lineEdit_3 = QtWidgets.QLineEdit(self.tab5)
        self.tab5_lineEdit_3.setGeometry(QtCore.QRect(420, 50, 361, 21))
        self.tab5_lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.tab5_lineEdit_3.setReadOnly(True)
        self.tab5_lineEdit_3.setObjectName("tab5_lineEdit_3")
        self.tab5_lineEdit_2 = QtWidgets.QLineEdit(self.tab5)
        self.tab5_lineEdit_2.setGeometry(QtCore.QRect(170, 50, 251, 21))
        self.tab5_lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.tab5_lineEdit_2.setReadOnly(True)
        self.tab5_lineEdit_2.setObjectName("tab5_lineEdit_2")
        self.tab5_lineEdit = QtWidgets.QLineEdit(self.tab5)
        self.tab5_lineEdit.setGeometry(QtCore.QRect(0, 50, 1071, 21))
        self.tab5_lineEdit.setReadOnly(True)
        self.tab5_lineEdit.setObjectName("tab5_lineEdit")
        self.tab5_comboBox = QtWidgets.QComboBox(self.tab5)
        self.tab5_comboBox.setEnabled(True)
        self.tab5_comboBox.setGeometry(QtCore.QRect(1030, 26, 41, 20))
        self.tab5_comboBox.setEditable(False)
        self.tab5_comboBox.setCurrentText("")
        self.tab5_comboBox.setObjectName("tab5_comboBox")
        self.tab5_label_2 = QtWidgets.QLabel(self.tab5)
        self.tab5_label_2.setGeometry(QtCore.QRect(1000, 27, 31, 21))
        self.tab5_label_2.setObjectName("tab5_label_2")
        self.tab5_pushButton_2 = QtWidgets.QPushButton(self.tab5)
        self.tab5_pushButton_2.setGeometry(QtCore.QRect(1001, 0, 71, 21))
        self.tab5_pushButton_2.setObjectName("tab5_pushButton_2")
        self.tab5_lineEdit.raise_()
        self.tab5_tableWidget.raise_()
        self.tab5_dateEdit.raise_()
        self.tab5_label.raise_()
        self.tab5_label_3.raise_()
        self.tab5_lineEdit_3.raise_()
        self.tab5_lineEdit_2.raise_()
        self.tab5_comboBox.raise_()
        self.tab5_label_2.raise_()
        self.tab5_pushButton_2.raise_()
        self.tabWidget.addTab(self.tab5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setEnabled(True)
        self.tab1.setObjectName("tab1")
        self.tab1_label_7 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_7.setGeometry(QtCore.QRect(250, 490, 181, 20))
        self.tab1_label_7.setText("")
        self.tab1_label_7.setObjectName("tab1_label_7")
        self.tab1_tableWidget = QtWidgets.QTableWidget(self.tab1)
        self.tab1_tableWidget.setGeometry(QtCore.QRect(174, 50, 891, 421))
        self.tab1_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab1_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab1_tableWidget.setAlternatingRowColors(True)
        self.tab1_tableWidget.setObjectName("tab1_tableWidget")
        self.tab1_tableWidget.setColumnCount(0)
        self.tab1_tableWidget.setRowCount(0)
        self.tab1_label_2 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_2.setGeometry(QtCore.QRect(450, 470, 171, 21))
        self.tab1_label_2.setText("")
        self.tab1_label_2.setObjectName("tab1_label_2")
        self.tab1_label_5 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_5.setGeometry(QtCore.QRect(250, 470, 181, 21))
        self.tab1_label_5.setText("")
        self.tab1_label_5.setObjectName("tab1_label_5")
        self.tab1_label_6 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_6.setGeometry(QtCore.QRect(180, 490, 71, 21))
        self.tab1_label_6.setObjectName("tab1_label_6")
        self.tab1_label = QtWidgets.QLabel(self.tab1)
        self.tab1_label.setGeometry(QtCore.QRect(430, 470, 21, 21))
        self.tab1_label.setObjectName("tab1_label")
        self.tab1_pushButton_2 = QtWidgets.QPushButton(self.tab1)
        self.tab1_pushButton_2.setGeometry(QtCore.QRect(890, 25, 61, 23))
        self.tab1_pushButton_2.setObjectName("tab1_pushButton_2")
        self.tab1_label_4 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_4.setGeometry(QtCore.QRect(180, 470, 71, 21))
        self.tab1_label_4.setObjectName("tab1_label_4")
        self.tab1_pushButton = QtWidgets.QPushButton(self.tab1)
        self.tab1_pushButton.setEnabled(True)
        self.tab1_pushButton.setGeometry(QtCore.QRect(1020, 25, 41, 23))
        self.tab1_pushButton.setObjectName("tab1_pushButton")
        self.tab1_plainTextEdit = QtWidgets.QPlainTextEdit(self.tab1)
        self.tab1_plainTextEdit.setEnabled(True)
        self.tab1_plainTextEdit.setGeometry(QtCore.QRect(0, 278, 171, 71))
        self.tab1_plainTextEdit.setReadOnly(True)
        self.tab1_plainTextEdit.setObjectName("tab1_plainTextEdit")
        self.tab1_listWidget = QtWidgets.QListWidget(self.tab1)
        self.tab1_listWidget.setGeometry(QtCore.QRect(0, 50, 171, 192))
        self.tab1_listWidget.setObjectName("tab1_listWidget")
        self.tab1_label_3 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_3.setGeometry(QtCore.QRect(40, 27, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.tab1_label_3.setFont(font)
        self.tab1_label_3.setObjectName("tab1_label_3")
        self.tab1_pushButton_3 = QtWidgets.QPushButton(self.tab1)
        self.tab1_pushButton_3.setGeometry(QtCore.QRect(0, 248, 75, 23))
        self.tab1_pushButton_3.setObjectName("tab1_pushButton_3")
        self.tab1_pushButton_4 = QtWidgets.QPushButton(self.tab1)
        self.tab1_pushButton_4.setGeometry(QtCore.QRect(960, 25, 51, 23))
        self.tab1_pushButton_4.setObjectName("tab1_pushButton_4")
        self.tab1_label_8 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_8.setGeometry(QtCore.QRect(430, 490, 31, 21))
        self.tab1_label_8.setObjectName("tab1_label_8")
        self.tab1_label_9 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_9.setGeometry(QtCore.QRect(470, 490, 51, 21))
        self.tab1_label_9.setText("")
        self.tab1_label_9.setObjectName("tab1_label_9")
        self.tab1_label_10 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_10.setGeometry(QtCore.QRect(530, 490, 41, 21))
        self.tab1_label_10.setObjectName("tab1_label_10")
        self.tab1_label_11 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_11.setGeometry(QtCore.QRect(570, 490, 141, 21))
        self.tab1_label_11.setText("")
        self.tab1_label_11.setObjectName("tab1_label_11")
        self.tab1_label_12 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_12.setGeometry(QtCore.QRect(90, 248, 31, 21))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(9)
        self.tab1_label_12.setFont(font)
        self.tab1_label_12.setObjectName("tab1_label_12")
        self.tab1_checkBox = QtWidgets.QCheckBox(self.tab1)
        self.tab1_checkBox.setGeometry(QtCore.QRect(130, 248, 21, 21))
        self.tab1_checkBox.setText("")
        self.tab1_checkBox.setChecked(True)
        self.tab1_checkBox.setObjectName("tab1_checkBox")
        self.tab1_label_13 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_13.setGeometry(QtCore.QRect(990, 470, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab1_label_13.setFont(font)
        self.tab1_label_13.setText("")
        self.tab1_label_13.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab1_label_13.setObjectName("tab1_label_13")
        self.tab1_pushButton_5 = QtWidgets.QPushButton(self.tab1)
        self.tab1_pushButton_5.setGeometry(QtCore.QRect(830, 25, 51, 21))
        self.tab1_pushButton_5.setText("")
        self.tab1_pushButton_5.setObjectName("tab1_pushButton_5")
        self.tab1_label_14 = QtWidgets.QLabel(self.tab1)
        self.tab1_label_14.setGeometry(QtCore.QRect(990, 0, 71, 21))
        self.tab1_label_14.setText("")
        self.tab1_label_14.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab1_label_14.setObjectName("tab1_label_14")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tab2_pushbutton = QtWidgets.QPushButton(self.tab2)
        self.tab2_pushbutton.setGeometry(QtCore.QRect(1030, 25, 41, 23))
        self.tab2_pushbutton.setObjectName("tab2_pushbutton")
        self.tab2_tableWidget = QtWidgets.QTableWidget(self.tab2)
        self.tab2_tableWidget.setGeometry(QtCore.QRect(0, 50, 1071, 441))
        self.tab2_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab2_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab2_tableWidget.setAlternatingRowColors(True)
        self.tab2_tableWidget.setObjectName("tab2_tableWidget")
        self.tab2_tableWidget.setColumnCount(0)
        self.tab2_tableWidget.setRowCount(0)
        self.tab2_comboBox = QtWidgets.QComboBox(self.tab2)
        self.tab2_comboBox.setGeometry(QtCore.QRect(0, 20, 61, 22))
        self.tab2_comboBox.setObjectName("tab2_comboBox")
        self.tab2_label = QtWidgets.QLabel(self.tab2)
        self.tab2_label.setGeometry(QtCore.QRect(1000, 490, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab2_label.setFont(font)
        self.tab2_label.setText("")
        self.tab2_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab2_label.setObjectName("tab2_label")
        self.tab2_label_2 = QtWidgets.QLabel(self.tab2)
        self.tab2_label_2.setGeometry(QtCore.QRect(1000, 0, 71, 21))
        self.tab2_label_2.setText("")
        self.tab2_label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab2_label_2.setObjectName("tab2_label_2")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.tab3_pushButton = QtWidgets.QPushButton(self.tab3)
        self.tab3_pushButton.setGeometry(QtCore.QRect(1020, 96, 51, 21))
        self.tab3_pushButton.setObjectName("tab3_pushButton")
        self.tab3_tableWidget = QtWidgets.QTableWidget(self.tab3)
        self.tab3_tableWidget.setGeometry(QtCore.QRect(0, 120, 1071, 371))
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
        self.tab3_label_5.setGeometry(QtCore.QRect(570, 10, 51, 21))
        self.tab3_label_5.setObjectName("tab3_label_5")
        self.tab3_label_6 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_6.setGeometry(QtCore.QRect(300, 40, 121, 21))
        self.tab3_label_6.setObjectName("tab3_label_6")
        self.tab3_label_7 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_7.setEnabled(False)
        self.tab3_label_7.setGeometry(QtCore.QRect(590, 40, 101, 21))
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
        self.tab3_label_11.setGeometry(QtCore.QRect(590, 70, 161, 21))
        self.tab3_label_11.setObjectName("tab3_label_11")
        self.tab3_comboBox = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox.setGeometry(QtCore.QRect(460, 10, 81, 22))
        self.tab3_comboBox.setObjectName("tab3_comboBox")
        self.tab3_comboBox_2 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_2.setGeometry(QtCore.QRect(630, 10, 76, 22))
        self.tab3_comboBox_2.setObjectName("tab3_comboBox_2")
        self.tab3_comboBox_4 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_4.setGeometry(QtCore.QRect(460, 40, 81, 22))
        self.tab3_comboBox_4.setObjectName("tab3_comboBox_4")
        self.tab3_comboBox_5 = QtWidgets.QComboBox(self.tab3)
        self.tab3_comboBox_5.setGeometry(QtCore.QRect(71, 70, 161, 22))
        self.tab3_comboBox_5.setObjectName("tab3_comboBox_5")
        self.tab3_checkBox = QtWidgets.QCheckBox(self.tab3)
        self.tab3_checkBox.setGeometry(QtCore.QRect(570, 40, 21, 21))
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
        self.tab3_checkBox_4.setGeometry(QtCore.QRect(570, 70, 21, 21))
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
        self.tab3_label_13.setGeometry(QtCore.QRect(1000, 491, 71, 21))
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
        self.tab3_label_15.setGeometry(QtCore.QRect(0, 492, 41, 21))
        self.tab3_label_15.setObjectName("tab3_label_15")
        self.tab3_label_16 = QtWidgets.QLabel(self.tab3)
        self.tab3_label_16.setGeometry(QtCore.QRect(50, 492, 41, 21))
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
        self.tab3_label_17.setGeometry(QtCore.QRect(1000, 0, 71, 21))
        self.tab3_label_17.setText("")
        self.tab3_label_17.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab3_label_17.setObjectName("tab3_label_17")
        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.tab4_tableWidget = QtWidgets.QTableWidget(self.tab4)
        self.tab4_tableWidget.setGeometry(QtCore.QRect(0, 70, 1071, 421))
        self.tab4_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab4_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab4_tableWidget.setAlternatingRowColors(True)
        self.tab4_tableWidget.setObjectName("tab4_tableWidget")
        self.tab4_tableWidget.setColumnCount(0)
        self.tab4_tableWidget.setRowCount(0)
        self.tab4_pushButton = QtWidgets.QPushButton(self.tab4)
        self.tab4_pushButton.setGeometry(QtCore.QRect(1020, 48, 51, 21))
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
        self.tab4_label_4 = QtWidgets.QLabel(self.tab4)
        self.tab4_label_4.setGeometry(QtCore.QRect(1000, 491, 71, 21))
        font = QtGui.QFont()
        font.setFamily("-윤고딕110")
        font.setPointSize(8)
        self.tab4_label_4.setFont(font)
        self.tab4_label_4.setText("")
        self.tab4_label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab4_label_4.setObjectName("tab4_label_4")
        self.tab4_label_5 = QtWidgets.QLabel(self.tab4)
        self.tab4_label_5.setGeometry(QtCore.QRect(0, 491, 41, 21))
        self.tab4_label_5.setObjectName("tab4_label_5")
        self.tab4_label_6 = QtWidgets.QLabel(self.tab4)
        self.tab4_label_6.setGeometry(QtCore.QRect(50, 491, 41, 21))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(9)
        self.tab4_label_6.setFont(font)
        self.tab4_label_6.setAutoFillBackground(False)
        self.tab4_label_6.setText("")
        self.tab4_label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tab4_label_6.setObjectName("tab4_label_6")
        self.tab4_label_7 = QtWidgets.QLabel(self.tab4)
        self.tab4_label_7.setGeometry(QtCore.QRect(1000, 0, 71, 21))
        self.tab4_label_7.setText("")
        self.tab4_label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tab4_label_7.setObjectName("tab4_label_7")
        self.tab4_comboBox = QtWidgets.QComboBox(self.tab4)
        self.tab4_comboBox.setGeometry(QtCore.QRect(63, 38, 141, 22))
        self.tab4_comboBox.setObjectName("tab4_comboBox")
        self.tabWidget.addTab(self.tab4, "")
        self.tab6 = QtWidgets.QWidget()
        self.tab6.setObjectName("tab6")
        self.label = QtWidgets.QLabel(self.tab6)
        self.label.setGeometry(QtCore.QRect(50, 30, 151, 141))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1077, 21))
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
        self.action_infosite = QtWidgets.QAction(MainWindow)
        self.action_infosite.setObjectName("action_infosite")
        self.action_version = QtWidgets.QAction(MainWindow)
        self.action_version.setObjectName("action_version")
        self.action_wikidocs = QtWidgets.QAction(MainWindow)
        self.action_wikidocs.setObjectName("action_wikidocs")
        self.menudevelop.addAction(self.action_infosite)
        self.menudevelop.addAction(self.action_wikidocs)
        self.menuInfo.addAction(self.menudevelop.menuAction())
        self.menuetc.addAction(self.action_version)
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
        self.tab5_lineEdit_3.setText(_translate("MainWindow", "홀세일 2본부"))
        self.tab5_lineEdit_2.setText(_translate("MainWindow", "홀세일 1본부"))
        self.tab5_label_2.setText(_translate("MainWindow", "단위"))
        self.tab5_pushButton_2.setText(_translate("MainWindow", "엑셀 변환"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), _translate("MainWindow", "수탁고 현황"))
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
        self.tab4_label_3.setText(_translate("MainWindow", "수익자명"))
        self.tab4_label_5.setText(_translate("MainWindow", "조회수:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), _translate("MainWindow", "수익자 정보"))
        self.label.setText(_translate("MainWindow", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab6), _translate("MainWindow", "그리기"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.menudevelop.setTitle(_translate("MainWindow", "develop"))
        self.menuetc.setTitle(_translate("MainWindow", "etc"))
        self.action_infosite.setText(_translate("MainWindow", "info site"))
        self.action_version.setText(_translate("MainWindow", "version"))
        self.action_wikidocs.setText(_translate("MainWindow", "wiki docs"))

        # 클래스 변수
        Ui_MainWindow.updateDate = "2022-01-10"  # 최근 업데이트

        Ui_MainWindow.userinfo= {}
        Ui_MainWindow.col = ""  # 클릭한 표위치
        Ui_MainWindow.row = ""  # 클릭한 표위치
        Ui_MainWindow.maxSearch = 10000  # 최대 테이블 조회가능 제한
        Ui_MainWindow.commaLength = 4  # 최소 콤마찍는 자리 수
        Ui_MainWindow.won= 100000000 # 표시단위(억)
        Ui_MainWindow.minus = QtGui.QColor(255, 225, 225)  # 음수표시 색상 RGB
        Ui_MainWindow.bold = QtGui.QColor(225, 225, 225)  # 강조 색상 RGB
        Ui_MainWindow.selectedTable = ""  # DB리스트 선택값
        Ui_MainWindow.mainWindow_df1_0 = ""  # 메인 자료값
        Ui_MainWindow.mainWindow_df3_1 = ""  # 탭3 팝업 자료값
        Ui_MainWindow.mainWindow_df3_1Re = ""  # 탭3 팝업 가공값
        Ui_MainWindow.mainWindow_df3_2 = ""  # 탭3 펀드조회 자료값
        Ui_MainWindow.mainWindow_df3_2Re = ""  # 탭3 펀드조회 가공값
        Ui_MainWindow.mainWindow_df3_3 = ""  # 탭3 수익자정보 자료값
        Ui_MainWindow.mainWindow_df3_3Re = ""  # 탭3 수익자정보 가공값
        Ui_MainWindow.mainWindow_df4_0 = ""  # 탭4 수익자현황 자료값
        Ui_MainWindow.mainWindow_df5_0 = ""  # 탭5 수탁고현황 최종자료값
        Ui_MainWindow.mainWindow_df5_1 = ""  # 수익자 그룹현황 자료값
        Ui_MainWindow.mainWindow_df5_1Re = ""  # 수익자 그룹현황 가공값
        Ui_MainWindow.mainWindow_df5_1Ex = ""  # 수익자 그룹현황 엑셀값
        Ui_MainWindow.mainWindow_df5_2 = ""  # 수익자 항목현황 자료값
        Ui_MainWindow.mainWindow_df5_2Re = ""  # 수익자 항목현황 가공값
        Ui_MainWindow.mainWindow_df5_2Ex = ""  # 수익자 그룹현황 엑셀값
        Ui_MainWindow.sqlQuery = ""  # 추가 쿼리
        Ui_MainWindow.tab3Code = ""  # 탭3 클릭값 펀드코드
        Ui_MainWindow.tab3Name = ""  # 탭3 클릭값 펀드명
        Ui_MainWindow.tab3Value = ""  # 탭3 클릭 확인값
        Ui_MainWindow.tab3SelectCode = ""  # 탭3 펀드검색 검색명
        Ui_MainWindow.tab5group = ""  # 탭5 고객그룹
        Ui_MainWindow.tab5team = ""  # 탭5 홀세일본부 구분
        Ui_MainWindow.tab5win1Item = ""  # 탭5 창1 항목값
        Ui_MainWindow.tab5win1Item = ""  # 탭5 창1 항목값
        Ui_MainWindow.tab5changeWonFlag= True

        # Qt디자이너 외 구현
        self.setListWidget()  # DB리스트 생성
        self.tab1_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 내용수정 금지
        self.tab1_newWindow1 = QDialog()  # 세부검색조건 팝업창
        self.tab1_newWindow2 = QDialog()  # 그래픽부분 팝업창
        self.popup_version = QDialog()  # 탭3 수익자 팝업창
        self.tab1_pushButton_3.setDisabled(True)
        self.tab1_pushButton_4.setDisabled(True)
        self.tabWidget.setUsesScrollButtons(False)  # 상단 탭스크롤바 막기
        Ui_MainWindow.userinfo=userinfo # 접속정보 입력
        if os.path.exists('hkamudfl.exe'):
            os.remove('hkamudfl.exe') # 시작시 다운로더 제거
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow",
        "                                                                                                                              "
        "                                                                                                                    "))
        self.tab1_tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)  # 헤더 중앙정렬
        if Ui_MainWindow.userinfo['id'] != "HKCL":  # 계정만 날짜 다르게
            day = 1
            if date.today().isoweekday() == 1:  # 월요일만
                day = 3
            self.tab3_dateEdit.setDate(date.today() - timedelta(day))
            self.tab4_dateEdit.setDate(date.today() - timedelta(day))
        self.tab3_dateEdit_2.setDate(date.today() - timedelta(1))  # 자료는 전일자꺼 까지만 있음
        self.tab4_dateEdit_2.setDate(date.today() - timedelta(1))  # 자료는 전일자꺼 까지만 있음
        # print(userinfo)
        self.tab2_layout()  # 탭2 레이아웃
        self.tab3_layout()  # 탭3 레이아웃
        self.tab4_layout()  # 탭4 레이아웃
        self.tab5_layout()  # 탭5 레이아웃
        self.tab6_layout()  # 탭6 레이아웃
        self.timer = QtCore.QTimer()  # 실시간 시계
        self.timer.start(1000)
        atexit.register(self.closeApp)  # 종료시

        self.newcreateTable(5, 0, '', self.tab5_dateEdit.text(), '', '', '')  # 임시

        # 이벤트
        try:
            self.action_infosite.triggered.connect(lambda: self.linkSite(1))  # 툴바1-1
            self.action_wikidocs.triggered.connect(lambda: self.linkSite(2))  # 툴바1-2
            self.action_version.triggered.connect(lambda: self.popup1(Ui_MainWindow.updateDate))  # 툴바2
            self.tab1_pushButton.clicked.connect(lambda: self.newcreateTable(1, 0, '', '', '', '', ''))  # 탭1 조회
            self.tab1_pushButton_2.clicked.connect(lambda: self.toExcel("1", "0", self.tab1_label_5.text()))  # 엑셀변환 버튼
            self.tab1_tableWidget.cellClicked.connect(self.cellClickEvent)  # 표 클릭시
            self.tab1_tableWidget.currentCellChanged.connect(self.cellClickEvent)  # 표 클릭시 이벤트 둘 다 있어야 재대로 나옴
            self.tab1_listWidget.currentItemChanged.connect(self.clearPlaintext)  # DB리스트 클릭시
            self.tab1_pushButton_3.clicked.connect(self.windowQuery)  # 검색조건 팝업 버튼
            self.tab1_pushButton_4.clicked.connect(lambda: self.windowGraphic("1", "0"))  # 그래픽 팝업 버튼
            self.tab1_checkBox.stateChanged.connect(self.chkBox)  # 체크 변경시
            self.timer.timeout.connect(self.clock)  # 실시간 시간값 뿌림
            self.tab1_pushButton_5.clicked.connect(self.test)  # 테스트용

        except:
            traceback.print_exc()

    # -----------------------------------------------tab1

    def chkBox(self):
        """조건 비활성화 유무 표시"""
        self.newcreateTable(1, 0, '', '', '', '', '')
        if self.tab1_checkBox.isChecked():
            self.tab1_plainTextEdit.setEnabled(True)
        else:
            self.tab1_plainTextEdit.setEnabled(False)

    def setListWidget(self):
        """ 왼쪽 리스트에 DB리스트 생성. 리스트는 하드코딩 약 8만건 기준 조회시간 30초 """
        dbList = ["정보_회사", "SUIKJA_INFO", "SUIKJA_COM", "FUND_BASIC", "FUND_COMPANY", "FUND_INTEGRATE", "FUND_OPERATE",
                  "FUND_RETAIL",
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
                                value = self.parseFloat(str1)
                                if value:
                                    tot.append(value)

                    self.tab1_label_9.setText(str(cnt))  # 수
                    total = str(sum(tot))
                    self.tab1_label_11.setText(self.setComma(2,total,False))  # 합계
        except:
            traceback.print_exc()

    def clearPlaintext(self):
        """조건검색 내용 지우고 검색"""
        self.tab1_plainTextEdit.setPlainText("")
        Ui_MainWindow.sqlQuery = ""
        self.newcreateTable(1, 0, '', '', '', '', '')

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
                # print(sql)
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

        # -------------------------------------------- 탭1 창1 windowQuery

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
            self.tab1_win1checkBox.stateChanged.connect(self.ableQuery1)  # 추가조건 활성/비활성화
            self.tab1_win1checkBox_2.stateChanged.connect(self.ableQuery2)  # 추가조건 활성/비활성화
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
        self.newcreateTable(1, 0, '', '', '', '', '')
        self.tab1_plainTextEdit.setPlainText(Ui_MainWindow.sqlQuery)
        self.tab1_newWindow1.close()

    def setQuery(self, columnText, i, lineEditText):
        """ 조건을 설정해 SQL에 추가 """
        str1 = [" like '%", " = '", " != '", " >= '", " <= '"]
        str2 = ["%'", "'"]
        sql = " and TO_CHAR(" + columnText + ") " + str1[i] + lineEditText + str2[math.trunc((i + 9) / 10)]  # %만 2번
        return sql

    def setCombobox(self):
        """ 콤보박스값들 설정 """
        for i in Ui_MainWindow.mainWindow_df1_0.columns.values.tolist():
            self.tab1_win1comboBox.addItem(i)
            self.tab1_win1comboBox_2.addItem(i)

        # ----------------------------------- 탭1 창2 windowGraphic

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
            # if self.parseFloat(df[self.tab1_win2comboBox_3.currentText()][0])!=0: # 첫 값보고 타입 확인
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

    # --------------------------------------tab2

    def tab2_layout(self):
        self.tab2_comboBox.addItem('json')
        self.tab2_comboBox.addItem('xml')

        # 이벤트
        self.tab2_comboBox.currentIndexChanged.connect(self.connectAPI)  # API 자료조회
        self.tab2_pushbutton.clicked.connect(self.connectAPI)  # API 자료조회

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
            self.newcreateTable(2, 0, '', df2, '', '', '')
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
            self.newcreateTable(2, 0, '', df2, '', '', '')
        except:
            traceback.print_exc()

    # ---------------------------------------tab3

    def tab3_layout(self):
        self.tab3_newWindow1 = QDialog()  # 탭3 팝업창
        self.tab3_newWindow2 = QDialog()  # 탭3 펀드검색 팝업창
        self.tab3_newWindow3 = QDialog()  # 탭3 수익자 팝업창
        self.tab3_comboBox.addItems(('전체', '운용중', '운용개시', '결산', '상환'))
        self.tab3_comboBox_2.addItems(('전체', '유', '무'))
        self.tab3_comboBox_4.addItems(('전체', '판매펀드', '운용펀드'))
        self.tab3_comboBox_5.addItems(('전체', '224 흥국자산운용', '207 교보악사자산운용', '216 DB자산운용', '363 트러스톤자산운용', '368 하이자산운용'))
        self.tab3_toolButton.setIcon(QIcon(resource_path('find.png')))  # 돋보기 아이콘

        # 멀티프로세스 연습 @@@

        p = mp.Process(target=times)
        p.daemon = True

        # p.start()

        # 이벤트
        self.tab3_pushButton.clicked.connect(lambda: self.newcreateTable(3, 0, '', '', '', '', ''))  # 탭3 테이블 조회
        self.tab3_tableWidget.cellClicked.connect(self.tab3_returnCode)  # 탭3 표 클릭시
        self.tab3_toolButton.clicked.connect(self.windowCode)  # 탭3 펀드검색
        self.tab3_tableWidget.doubleClicked.connect(lambda: self.tab3_selectWindow(Ui_MainWindow.col,
                                                                                   Ui_MainWindow.tab3Value,
                                                                                   Ui_MainWindow.tab3Code,
                                                                                   Ui_MainWindow.tab3Name))  # 탭3 표 더블블릭시

    def clock(self):
        """실시간 시계"""
        self.tab1_label_14.setText(str(datetime.datetime.now().strftime('%H:%M:%S')))
        self.tab2_label_2.setText(str(datetime.datetime.now().strftime('%H:%M:%S')))
        self.tab3_label_17.setText(str(datetime.datetime.now().strftime('%H:%M:%S')))
        self.tab4_label_7.setText(str(datetime.datetime.now().strftime('%H:%M:%S')))

    def tab3_selectWindow(self, col, val, fundCode, fundName):
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
            # print(sql)
            cur.execute(sql)
            row = cur.fetchall()
            if len(row) == 0:
                row = [("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", "", "", "", "", "", "")]
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
        Ui_MainWindow.col = col

    # ----------------------------------------------- 탭3 창1 팝업창
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
        self.newcreateTable(3, 1, '', self.tab3_win1dateEdit.text(), self.tab3_win1dateEdit_2.text(), '', fundCode)
        if Ui_MainWindow.userinfo['id'] != "HKCL" and len(Ui_MainWindow.mainWindow_df3_1) > 0:
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
            self.tab3_win1pushButton_3.clicked.connect(
                lambda: self.newcreateTable(3, 1, "re", self.tab3_win1dateEdit.text(), self.tab3_win1dateEdit_2.text(),
                                            '', ''))  # 조회
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
                                value = self.parseFloat(str1)
                                if value:
                                    tot.append(value)

                    self.tab3_win1label_6.setText(str(cnt))  # 수
                    total = str(sum(tot))
                    self.tab3_win1label_8.setText(self.setComma(2,total,False))  # 합계
        except:
            traceback.print_exc()

        # ---------------------------------------- 탭3 창2 windowCode

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
        self.newcreateTable(3, 2, '', '', '', '', '')
        Ui_MainWindow.tab3SelectCode = ""
        self.tab3_lineEdit.setText("")
        self.tab3_newWindow2.show()

        # 이벤트
        self.tab3_win2lineEdit.textEdited.connect(lambda: self.newcreateTable(3, 2, "re", 1, '', '', ''))  # 펀드코드 검색
        self.tab3_win2lineEdit_2.textEdited.connect(lambda: self.newcreateTable(3, 2, "re", 2, '', '', ''))  # 펀드명 검색
        self.tab3_win2tableWidget.cellClicked.connect(self.tab3_win2SelectValue)  # 값 선택
        self.tab3_win2tableWidget.cellDoubleClicked.connect(
            lambda: self.tab3_win2Close(Ui_MainWindow.tab3SelectCode))  # 값 넘김
        self.tab3_win2pushButton.clicked.connect(lambda: self.tab3_win2Close(Ui_MainWindow.tab3SelectCode))  # 조회 버튼

    def tab3_win2SelectValue(self, row, col):
        """더블클릭 이벤트에 컬럼 좌표 입력이 별도로 없음"""
        Ui_MainWindow.tab3SelectCode = self.tab3_win2tableWidget.item(row, 0).text()

    def tab3_win2Close(self, fundCode):
        """창 종료"""
        self.tab3_lineEdit.setText(fundCode)
        self.newcreateTable(3, 0, '', '', '', '', '')
        self.tab3_newWindow2.close()

    # ---------------------------------- 탭3 창3 windowEarn

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
        self.newcreateTable(3, 3, '', '', '', fundCode, '')
        self.tab3_newWindow3.setWindowModality(QtCore.Qt.ApplicationModal)  # 하위창 컨트롤 금지
        if Ui_MainWindow.userinfo['id'] != "HKCL" and len(Ui_MainWindow.mainWindow_df3_3) > 0:
            self.tab3_win3dateEdit.setDate(Ui_MainWindow.mainWindow_df3_3['기준일자'].min())
        else:
            self.tab3_win3dateEdit.setDate(date.today() - timedelta(1))
        self.tab3_win3dateEdit_2.setDate(date.today() - timedelta(1))
        self.tab3_newWindow3.show()

        # 이벤트
        self.tab3_win3pushButton_3.clicked.connect(
            lambda: self.newcreateTable(3, 3, "re", self.tab3_win3comboBox.currentText(),
                                        self.tab3_win3comboBox_2.currentText(), fundCode, ''))  # 조회 버튼
        self.tab3_win3comboBox.currentTextChanged.connect(
            lambda: self.tab3_win3ChangeSelectComboBox(fundCode))  # 구좌항목 변경
        self.tab3_win3pushButton_2.clicked.connect(lambda: self.windowGraphic("3", "3"))  # 그래픽 팝업 버튼
        self.tab3_win3pushButton.clicked.connect(
            lambda: self.toExcel("3", "3", self.tab3_win3label_2.text()))  # 엑셀변환 버튼
        self.tab3_win3checkBox.stateChanged.connect(lambda: self.ckeckedTab3_Win3checkBox(1))  # 날짜조회 활성/비활성화
        self.tab3_win3checkBox_2.stateChanged.connect(lambda: self.ckeckedTab3_Win3checkBox(2))  # 날짜조회 활성/비활성화

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
                sql = query.returnSQL('tab3_win3ChangeSelectComboBoxQuery').format(fundCode,
                                                                                   self.tab3_win3comboBox.currentText())
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

    # -------------------------------------tab4

    def tab4_layout(self):
        self.tab4_comboBox.addItem('전체')
        self.tab4_pushButton.clicked.connect(
            lambda: self.newcreateTable(4, 0, '', self.tab4_dateEdit.text(), self.tab4_dateEdit_2.text(),
                                        self.tab4_comboBox.currentText(), ''))  # 탭4 조회

        # 이벤트
        self.tab4_dateEdit.dateChanged.connect(
            lambda: self.newcreateTable(4, 0, '', self.tab4_dateEdit.text(), self.tab4_dateEdit_2.text(),
                                        self.tab4_comboBox.currentText(), ''))  # 탭4 조회
        self.tab4_dateEdit_2.dateChanged.connect(
            lambda: self.newcreateTable(4, 0, '', self.tab4_dateEdit.text(), self.tab4_dateEdit_2.text(),
                                        self.tab4_comboBox.currentText(), ''))  # 탭4 조회

    # ---------------------------------------tab5

    def tab5_layout(self):
        self.tab5_newWindow1 = QDialog()  # 탭5 수탁고 팝업창
        self.tab5_newWindow2 = QDialog()  # 탭5 유형별 팝업창
        self.tab5_dateEdit.setDate(parse(self.tab5_setDate()))
        self.tab5_comboBox.addItems(['억', '원'])
        # self.tab5_readJson()
        # self.tab5_createJson()

        # 이벤트
        self.tab5_dateEdit.dateChanged.connect(
            lambda: self.newcreateTable(5, 0, '', self.tab5_dateEdit.text(), '', '', ''))  # 탭5 조회
        self.tab5_tableWidget.cellClicked.connect(self.tab5_returnCode)  # 탭5 표 클릭시
        self.tab5_tableWidget.doubleClicked.connect(self.tab5_searchValue)  # 탭5 펀드검색
        self.tab5_comboBox.currentTextChanged.connect(
            lambda: self.newcreateTable(5, 0, '', self.tab5_dateEdit.text(), '', '', ''))  # 탭5 조회
        self.tab5_pushButton_2.clicked.connect(lambda: self.toExcel("5", "0", '수탁고 현황'))  # 엑셀변환 버튼
        self.tab5_tableWidget.horizontalHeader().sectionDoubleClicked.connect(self.tab5_headerDbclick) #헤더 더블클릭시 기준날짜 보여줌

    def tab5_createJson(self):
        """JSON파일 생성"""
        asd=Ui_MainWindow.userinfo['ip']+':5000\\static\\file\\setting\\test.json'
        print('~')
        file_data=OrderedDict()
        file_data['ip']=socket.gethostbyname(socket.gethostname())
        file_data['info1']='1'
        file_data['info2']='2'
        with open('userimsi.json','w',encoding="utf-8") as makefile:
            json.dump(file_data,makefile,ensure_ascii=False, indent='\t')

    def tab5_readJson(self):
        """JSON파일 읽기"""
        path = Ui_MainWindow.userinfo['ip'] + f':5000\\static\\file\\setting\\test.json'
        with open('C:\\Users\\User\\Desktop\\asdasd.json','r',encoding='utf-8') as readfile:
            content=json.load(readfile)
            print(content['ip'])

    def tab5_searchValue(self):
        """탭5 팝업 생성"""
        if Ui_MainWindow.tab5group != '합계' and Ui_MainWindow.tab5team:
            self.windowGroup(self.tab5_dateEdit.text(), Ui_MainWindow.tab5group, Ui_MainWindow.tab5team)

    def tab5_returnCode(self, row, col):
        """ 팝업으로 넘길 그룹명,팀. 더블클릭 이벤트에는 클릭값 받는 인자가 없음"""
        try:
            if col >= 2 and col <= 5:
                Ui_MainWindow.tab5team = '1본부'
                Ui_MainWindow.tab5group = self.tab5_tableWidget.item(row, 0).text()
            elif col >= 6 and col <= 9:
                Ui_MainWindow.tab5team = '2본부'
                Ui_MainWindow.tab5group = self.tab5_tableWidget.item(row, 0).text()
            else:
                Ui_MainWindow.tab5team = ''
                Ui_MainWindow.tab5group = ''
        except:
            traceback.print_exc()

    def tab5_setDate(self):
        """가장 최근 자료 날짜로 설정"""
        try:
            sql = query.returnSQL('tab5_setDateQuery')
            cur.execute(sql)
            row = cur.fetchall()
            return row[0][0]
        except:
            traceback.print_exc()

    def tab5_headerDbclick(self,logicalIndex):
        """헤더 더블클릭시 조회 기준날짜 보여줌"""
        try:
            tableheader = ['고객그룹', '설정액 합', '설정액', '전월말대비', '전분기말대비', '전년말대비', '설정액', '전월말대비', '전분기말대비', '전년말대비']
            header=['lastmonth','lastquater','lastyear','last2year']
            date=self.tab5_dateEdit.text()
            month=date[0:7]
            sql = query.returnSQL('tab5_headerDbclick').format(date=date,month=month)
            cur.execute(sql)
            row = cur.fetchall()
            df = pd.DataFrame(row)
            df.columns = header
            if logicalIndex==2 or logicalIndex==6:
                if self.tab5_tableWidget.horizontalHeaderItem(logicalIndex).text() in tableheader:
                    self.tab5_tableWidget.horizontalHeaderItem(logicalIndex).setText(self.tab5_dateEdit.text()[5:10])
                else:
                    self.tab5_tableWidget.horizontalHeaderItem(logicalIndex).setText(tableheader[logicalIndex])
            elif logicalIndex==3 or logicalIndex==7:
                if self.tab5_tableWidget.horizontalHeaderItem(logicalIndex).text() in tableheader:
                    date=(pd.to_datetime(df['lastmonth']).dt.date).values[0]
                    self.tab5_tableWidget.horizontalHeaderItem(logicalIndex).setText(str(date)[2:10])
                else:
                    self.tab5_tableWidget.horizontalHeaderItem(logicalIndex).setText(tableheader[logicalIndex])
            elif logicalIndex==4 or logicalIndex==8:
                if self.tab5_tableWidget.horizontalHeaderItem(logicalIndex).text() in tableheader:
                    date=(pd.to_datetime(df['lastquater']).dt.date).values[0]
                    self.tab5_tableWidget.horizontalHeaderItem(logicalIndex).setText(str(date)[2:10])
                else:
                    self.tab5_tableWidget.horizontalHeaderItem(logicalIndex).setText(tableheader[logicalIndex])
            elif logicalIndex==5 or logicalIndex==9:
                if self.tab5_tableWidget.horizontalHeaderItem(logicalIndex).text() in tableheader:
                    date=(pd.to_datetime(df['lastyear']).dt.date).values[0]
                    self.tab5_tableWidget.horizontalHeaderItem(logicalIndex).setText(str(date)[2:10])
                else:
                    self.tab5_tableWidget.horizontalHeaderItem(logicalIndex).setText(tableheader[logicalIndex])

        except:
            traceback.print_exc()


    # ---------------------------- 탭5 창1 windowGroup

    def windowGroup(self, date1, group, team):
        self.tab5_win1tableWidget = QtWidgets.QTableWidget(self.tab5_newWindow1)
        self.tab5_win1tableWidget.setGeometry(QtCore.QRect(0, 70, 1211, 281))
        self.tab5_win1tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab5_win1tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab5_win1tableWidget.setAlternatingRowColors(True)
        self.tab5_win1tableWidget.setObjectName("tab5_win1tableWidget")
        self.tab5_win1tableWidget.setColumnCount(0)
        self.tab5_win1tableWidget.setRowCount(0)
        self.tab5_win1label_5 = QtWidgets.QLabel(self.tab5_newWindow1)
        self.tab5_win1label_5.setGeometry(QtCore.QRect(1142, 28, 31, 21))
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
        self.tab5_win1label_2 = QtWidgets.QLabel(self.tab5_newWindow1)
        self.tab5_win1label_2.setGeometry(QtCore.QRect(97, 10, 51, 21))
        self.tab5_win1label_2.setObjectName("tab5_win1label_2")
        self.tab5_win1lineEdit = QtWidgets.QLineEdit(self.tab5_newWindow1)
        self.tab5_win1lineEdit.setGeometry(QtCore.QRect(150, 10, 61, 21))
        self.tab5_win1lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.tab5_win1lineEdit.setReadOnly(True)
        self.tab5_win1lineEdit.setObjectName("tab5_win1lineEdit")
        self.tab5_win1lineEdit_2 = QtWidgets.QLineEdit(self.tab5_newWindow1)
        self.tab5_win1lineEdit_2.setGeometry(QtCore.QRect(0, 50, 1211, 21))
        self.tab5_win1lineEdit_2.setReadOnly(True)
        self.tab5_win1lineEdit_2.setObjectName("tab5_win1lineEdit_2")
        self.tab5_win1lineEdit_3 = QtWidgets.QLineEdit(self.tab5_newWindow1)
        self.tab5_win1lineEdit_3.setGeometry(QtCore.QRect(200, 50, 391, 21))
        self.tab5_win1lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.tab5_win1lineEdit_3.setReadOnly(True)
        self.tab5_win1lineEdit_3.setObjectName("tab5_win1lineEdit_3")
        self.tab5_win1lineEdit_4 = QtWidgets.QLineEdit(self.tab5_newWindow1)
        self.tab5_win1lineEdit_4.setGeometry(QtCore.QRect(590, 50, 341, 21))
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
        self.tab5_win1comboBox_2.setGeometry(QtCore.QRect(1170, 27, 41, 22))
        self.tab5_win1comboBox_2.setEditable(False)
        self.tab5_win1comboBox_2.setCurrentText("")
        self.tab5_win1comboBox_2.setObjectName("tab5_win1comboBox_2")
        self.tab5_win1pushButton_2 = QtWidgets.QPushButton(self.tab5_newWindow1)
        self.tab5_win1pushButton_2.setGeometry(QtCore.QRect(1141, 0, 71, 21))
        self.tab5_win1pushButton_2.setObjectName("tab5_win1pushButton_2")
        self.tab5_win1lineEdit_2.raise_()
        self.tab5_win1tableWidget.raise_()
        self.tab5_win1label_5.raise_()
        self.tab5_win1label_4.raise_()
        self.tab5_win1dateEdit.raise_()
        self.tab5_win1comboBox.raise_()
        self.tab5_win1label_3.raise_()
        self.tab5_win1label_2.raise_()
        self.tab5_win1lineEdit.raise_()
        self.tab5_win1lineEdit_3.raise_()
        self.tab5_win1lineEdit_4.raise_()
        self.tab5_win1label.raise_()
        self.tab5_win1comboBox_2.raise_()
        self.tab5_win1pushButton_2.raise_()

        _translate = QtCore.QCoreApplication.translate

        self.tab5_win1tableWidget.setSortingEnabled(False)
        self.tab5_win1label_5.setText(_translate("MainWindow", "단위"))
        self.tab5_win1label_4.setText(_translate("MainWindow", "기준일"))
        self.tab5_win1label_3.setText(_translate("MainWindow", "고객"))
        self.tab5_win1label_2.setText(_translate("MainWindow", "고객그룹"))
        self.tab5_win1lineEdit_3.setText(_translate("MainWindow", "순자산 증감"))
        self.tab5_win1lineEdit_4.setText(_translate("MainWindow", "수탁고 설정액"))
        self.tab5_win1pushButton_2.setText(_translate("MainWindow", "엑셀 변환"))

        # QT디자이너 외 구현
        self.tab5_newWindow1.setWindowModality(QtCore.Qt.ApplicationModal)  # 하위창 컨트롤 금지
        self.tab5_newWindow1.resize(1213, 355)
        self.tab5_win1lineEdit.setText(group)
        self.tab5_win1label.setText('홀세일 ' + team)
        self.tab5_win1dateEdit.setDate(parse(date1))
        self.tab5_win1comboBox_2.addItems(['억','원'])
        if Ui_MainWindow.tab5changeWonFlag == True:
            self.tab5_win1comboBox_2.setCurrentText('억')
        else:
            self.tab5_win1comboBox_2.setCurrentText('원')
        fund_cd = ''
        if group == 'NPS':
            fund_cd = 'NPS'
        self.newcreateTable(5, 1, '', group, team, fund_cd, self.tab5_win1dateEdit.text())
        self.tab5_newWindow1.show()

        # 이벤트
        self.tab5_win1dateEdit.dateChanged.connect(
            lambda: self.newcreateTable(5, 1, '', group, team, fund_cd, self.tab5_win1dateEdit.text()))  # 탭5 날짜 조회 얘 바뀌면 밑에 2개도 같이 됨
        self.tab5_win1comboBox.currentTextChanged.connect(
            lambda: self.newcreateTable(5, 1, 're', group, team, fund_cd, self.tab5_win1dateEdit.text()))  # 탭5 고객 재조회
        self.tab5_win1comboBox_2.currentTextChanged.connect(
            lambda: self.newcreateTable(5, 1, 're', group, team, fund_cd, self.tab5_win1dateEdit.text()))  # 탭5 단위 재조회
        row = self.tab5_win1tableWidget.cellClicked.connect(self.tab5_win1returnCode)  # 탭5 표 클릭시
        self.tab5_win1tableWidget.doubleClicked.connect(lambda: self.tab5_win1searchValue(fund_cd))  # 탭5 펀드검색
        self.tab5_win1pushButton_2.clicked.connect(lambda: self.toExcel("5", "1", '그룹별 현황'))  # 엑셀변환 버튼
        self.tab5_win1tableWidget.horizontalHeader().sectionDoubleClicked.connect(self.tab5_win1HeaderDbclick) #헤더 더블클릭시 기준날짜 보여줌

    def tab5_win1HeaderDbclick(self,logicalIndex):
        """헤더 더블클릭시 조회 기준날짜 보여줌"""
        try:
            tableheader = ['유형', '설정액', '순자산', '전월말대비', '전분기말대비', '전년말대비', '전전년말대비', '전월말', '전분기말', '전년말', '전전년말']
            header=['lastmonth','lastquater','lastyear','last2year']
            date=self.tab5_win1dateEdit.text()
            month=date[0:7]
            sql = query.returnSQL('tab5_headerDbclick').format(date=date,month=month)
            cur.execute(sql)
            row = cur.fetchall()
            df = pd.DataFrame(row)
            df.columns = header
            if logicalIndex==1 or logicalIndex==2:
                if self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).text() in tableheader:
                    self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).setText(self.tab5_dateEdit.text()[5:10])
                else:
                    self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).setText(tableheader[logicalIndex])
            elif logicalIndex==3 or logicalIndex==7:
                if self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).text() in tableheader:
                    date=(pd.to_datetime(df['lastmonth']).dt.date).values[0]
                    self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).setText(str(date)[2:10])
                else:
                    self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).setText(tableheader[logicalIndex])
            elif logicalIndex==4 or logicalIndex==8:
                if self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).text() in tableheader:
                    date=(pd.to_datetime(df['lastquater']).dt.date).values[0]
                    self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).setText(str(date)[2:10])
                else:
                    self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).setText(tableheader[logicalIndex])
            elif logicalIndex==5 or logicalIndex==9:
                if self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).text() in tableheader:
                    date=(pd.to_datetime(df['lastyear']).dt.date).values[0]
                    self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).setText(str(date)[2:10])
                else:
                    self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).setText(tableheader[logicalIndex])
            elif logicalIndex==6 or logicalIndex==10:
                if self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).text() in tableheader:
                    date=(pd.to_datetime(df['last2year']).dt.date).values[0]
                    self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).setText(str(date)[2:10])
                else:
                    self.tab5_win1tableWidget.horizontalHeaderItem(logicalIndex).setText(tableheader[logicalIndex])
        except:
            traceback.print_exc()

    def tab5_win1searchValue(self, fund_cd):
        """탭5 팝업의팝업 생성"""
        try:
            if Ui_MainWindow.row <= len(Ui_MainWindow.mainWindow_df5_1Re.index) - 1 and Ui_MainWindow.col <= len(
                    Ui_MainWindow.mainWindow_df5_1Re.columns) - 1:
                self.windowItems(Ui_MainWindow.tab5win1Item, self.tab5_win1lineEdit.text(), Ui_MainWindow.tab5team, fund_cd)
        except:
            traceback.print_exc()

    def tab5_win1returnCode(self, row, col):
        """ 팝업의팝업으로 넘길 그룹명,팀. 더블클릭 이벤트에는 클릭값 받는 인자가 없음"""
        try:
            if self.tab5_win1tableWidget.item(row, 0):
                Ui_MainWindow.tab5win1Item = self.tab5_win1tableWidget.item(row, 0).text()
            Ui_MainWindow.col = col
            Ui_MainWindow.row = row
        except:
            traceback.print_exc()

    # ---------------------------- 탭5 창2 windowItems

    def windowItems(self, items, group, team, fund_cd):
        # item:항목,group:고객그룹,team:관리팀
        self.tab5_win2label_5 = QtWidgets.QLabel(self.tab5_newWindow2)
        self.tab5_win2label_5.setGeometry(QtCore.QRect(360, 10, 41, 21))
        self.tab5_win2label_5.setObjectName("tab5_win2label_5")
        self.tab5_win2dateEdit = QtWidgets.QDateEdit(self.tab5_newWindow2)
        self.tab5_win2dateEdit.setGeometry(QtCore.QRect(400, 10, 91, 22))
        self.tab5_win2dateEdit.setReadOnly(True)
        self.tab5_win2dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 8), QtCore.QTime(0, 0, 0)))
        self.tab5_win2dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.tab5_win2dateEdit.setCalendarPopup(True)
        self.tab5_win2dateEdit.setObjectName("tab5_win2dateEdit")
        self.tab5_win2label_2 = QtWidgets.QLabel(self.tab5_newWindow2)
        self.tab5_win2label_2.setGeometry(QtCore.QRect(97, 10, 51, 21))
        self.tab5_win2label_2.setObjectName("tab5_win2label_2")
        self.tab5_win2lineEdit = QtWidgets.QLineEdit(self.tab5_newWindow2)
        self.tab5_win2lineEdit.setGeometry(QtCore.QRect(150, 10, 61, 21))
        self.tab5_win2lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.tab5_win2lineEdit.setReadOnly(True)
        self.tab5_win2lineEdit.setObjectName("tab5_win2lineEdit")
        self.tab5_win2lineEdit_2 = QtWidgets.QLineEdit(self.tab5_newWindow2)
        self.tab5_win2lineEdit_2.setGeometry(QtCore.QRect(0, 60, 1241, 21))
        self.tab5_win2lineEdit_2.setReadOnly(True)
        self.tab5_win2lineEdit_2.setObjectName("tab5_win2lineEdit_2")
        self.tab5_win2lineEdit_3 = QtWidgets.QLineEdit(self.tab5_newWindow2)
        self.tab5_win2lineEdit_3.setGeometry(QtCore.QRect(200, 60, 301, 21))
        self.tab5_win2lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.tab5_win2lineEdit_3.setReadOnly(True)
        self.tab5_win2lineEdit_3.setObjectName("tab5_win2lineEdit_3")
        self.tab5_win2lineEdit_4 = QtWidgets.QLineEdit(self.tab5_newWindow2)
        self.tab5_win2lineEdit_4.setGeometry(QtCore.QRect(500, 60, 341, 21))
        self.tab5_win2lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.tab5_win2lineEdit_4.setReadOnly(True)
        self.tab5_win2lineEdit_4.setObjectName("tab5_win2lineEdit_4")
        self.tab5_win2label = QtWidgets.QLabel(self.tab5_newWindow2)
        self.tab5_win2label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.tab5_win2label.setAutoFillBackground(True)
        self.tab5_win2label.setText("")
        self.tab5_win2label.setObjectName("tab5_win2label")
        self.tab5_win2label_3 = QtWidgets.QLabel(self.tab5_newWindow2)
        self.tab5_win2label_3.setGeometry(QtCore.QRect(230, 10, 31, 21))
        self.tab5_win2label_3.setObjectName("tab5_win2label_3")
        self.tab5_win2lineEdit_5 = QtWidgets.QLineEdit(self.tab5_newWindow2)
        self.tab5_win2lineEdit_5.setGeometry(QtCore.QRect(260, 10, 81, 21))
        self.tab5_win2lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.tab5_win2lineEdit_5.setReadOnly(True)
        self.tab5_win2lineEdit_5.setObjectName("tab5_win2lineEdit_5")
        self.tab5_win2tableWidget = QtWidgets.QTableWidget(self.tab5_newWindow2)
        self.tab5_win2tableWidget.setGeometry(QtCore.QRect(0, 80, 1241, 421))
        self.tab5_win2tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tab5_win2tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab5_win2tableWidget.setAlternatingRowColors(True)
        self.tab5_win2tableWidget.setObjectName("tab5_win2tableWidget")
        self.tab5_win2tableWidget.setColumnCount(0)
        self.tab5_win2tableWidget.setRowCount(0)
        self.tab5_win2comboBox = QtWidgets.QComboBox(self.tab5_newWindow2)
        self.tab5_win2comboBox.setEnabled(True)
        self.tab5_win2comboBox.setGeometry(QtCore.QRect(1200, 37, 41, 22))
        self.tab5_win2comboBox.setEditable(False)
        self.tab5_win2comboBox.setCurrentText("")
        self.tab5_win2comboBox.setObjectName("tab5_win2comboBox")
        self.tab5_win2label_6 = QtWidgets.QLabel(self.tab5_newWindow2)
        self.tab5_win2label_6.setGeometry(QtCore.QRect(1172, 40, 31, 21))
        self.tab5_win2label_6.setObjectName("tab5_win2label_6")
        self.tab5_win2pushButton = QtWidgets.QPushButton(self.tab5_newWindow2)
        self.tab5_win2pushButton.setGeometry(QtCore.QRect(1170, 3, 71, 21))
        self.tab5_win2pushButton.setObjectName("tab5_win2pushButton")
        self.tab5_win2lineEdit_2.raise_()
        self.tab5_win2label_5.raise_()
        self.tab5_win2dateEdit.raise_()
        self.tab5_win2label_2.raise_()
        self.tab5_win2lineEdit.raise_()
        self.tab5_win2lineEdit_3.raise_()
        self.tab5_win2lineEdit_4.raise_()
        self.tab5_win2label.raise_()
        self.tab5_win2label_3.raise_()
        self.tab5_win2lineEdit_5.raise_()
        self.tab5_win2tableWidget.raise_()
        self.tab5_win2comboBox.raise_()
        self.tab5_win2label_6.raise_()
        self.tab5_win2pushButton.raise_()

        _translate = QtCore.QCoreApplication.translate

        self.tab5_win2label_5.setText(_translate("MainWindow", "기준일"))
        self.tab5_win2label_2.setText(_translate("MainWindow", "고객그룹"))
        self.tab5_win2lineEdit_3.setText(_translate("MainWindow", "순자산 증감"))
        self.tab5_win2lineEdit_4.setText(_translate("MainWindow", "수탁고 설정액"))
        self.tab5_win2label_3.setText(_translate("MainWindow", "항목"))
        self.tab5_win2tableWidget.setSortingEnabled(False)
        self.tab5_win2label_6.setText(_translate("MainWindow", "단위"))
        self.tab5_win2pushButton.setText(_translate("MainWindow", "엑셀 변환"))

        # QT디자이너 외 구현
        try:
            self.tab5_newWindow2.resize(1246, 503)
            self.tab5_newWindow2.setWindowModality(QtCore.Qt.ApplicationModal)  # 하위창 컨트롤 금지
            self.tab5_win2label.setText('홀세일 ' + team)
            self.tab5_win2lineEdit.setText(group)
            self.tab5_win2lineEdit_5.setText(items)
            self.tab5_win2dateEdit.setDate(parse(self.tab5_win1dateEdit.text()))
            self.tab5_win2comboBox.addItems(['억', '원'])
            if Ui_MainWindow.tab5changeWonFlag==True:
                self.tab5_win2comboBox.setCurrentText('억')
            else:
                self.tab5_win2comboBox.setCurrentText('원')
            self.newcreateTable(5, 2, '', Ui_MainWindow.mainWindow_df5_1, self.tab5_win2lineEdit_5.text(), '', '')
            self.tab5_newWindow2.show()

        # 이벤트
            self.tab5_win2comboBox.currentTextChanged.connect(
                lambda: self.newcreateTable(5, 2, '', Ui_MainWindow.mainWindow_df5_1, self.tab5_win2lineEdit_5.text(), '', '')) # 단위 조회
            self.tab5_win2pushButton.clicked.connect(lambda: self.toExcel("5", "2", '상품별 현황'))  # 엑셀변환 버튼

        except:
            traceback.print_exc()

    # -----------------------------tab6
    def tab6_layout(self):
        '''1:1 매칭되는 펀드들 HK01, VH03'''

    def paintEvent(self, event):
        print('이벤트시작')
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawPoint(self, qp):
        qp.setPen(QPen(QtCore.blue, 8))
        qp.drawPoint(self.width() / 2, self.height() / 2)

    def drawText(self, event, qp):
        qp.setPen(QtGui.QColor(0, 0, 0))
        qp.setFont(QFont('나눔명조', 35))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, '스산한 늦가을\n아니.. 초겨울인가?')

    # ----------------------------공통

    def newcreateTable(self, tab, win, re, val1, val2, val3, val4):
        """탭순서,새창순서,재조회여부,아무변수1~4가 들어옴"""
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
            # val1=데이터프레임
            try:
                df2 = val1
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
                          '판매보수', '운용보수', '사무관리보수', '수탁보수', '펀드평가보수', '자산관리보수', '상품관리보수', '성과보수', '성과보수여부', 'Total',
                          '설정액',
                          '설정좌수', '총자산', '순자산', '기준가', '누적수익지수', '펀드약명',
                          '영문명', '운용역', '운용사명', '수탁은행', '수탁사명', '사무수탁사명', '펀드평가사', '판매사갯수', '판매사명', '협회표준코드', '금감원코드',
                          '예탁원펀드코드', '예탁원종목코드', '상품분류코드',
                          '상품분류2차', '집합투자기구분류',
                          '펀드결제수수료여부', '분배방식', '당기결산방식', '시가평가여부', '장단기구분', '국외세액환급여부', '이관일', '이수일', '투자자', '부사무관리사명',
                          '해외전용과표가격대상여부', '해외전용과표가격적용일',
                          '설정대금확정일1', '설정일1', '환매대금확정일1', '환매일1', '환매대금확정일2', '환매일2', 'BM명', 'GIPS펀드유형', '채권평가사보수유예시작일',
                          '채권평가사보수유예종료일', '배당기준운용사',
                          '신주인수권증서평가기준(폐지일)', '공모청약수수료기준', '단위형구분', '수익차등여부', '사모분류', '일반투자자포함여부']
                alignRight = ['20', '21', '22', '23', '24', '25', '26', '27', '29', '30', '31', '32', '33',
                              '34']  # 오른쪽 정렬할 컬럼순서들
                sqlValue = self.tab3_searchValue()
                df = pd.DataFrame(sqlValue)
                df.columns = header
                self.tab3_tableWidget.setColumnCount(len(df.columns))
                self.tab3_tableWidget.setRowCount(len(df.index))
                self.tab3_tableWidget.setHorizontalHeaderLabels(header)
                self.setTableData(df, 3, 0, startTime, alignRight)
                self.tab3_tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정
            except:
                self.tab3_tableWidget.clear()
                self.tab3_tableWidget.setRowCount(1)
                self.tab3_tableWidget.setColumnCount(len(header))
                self.tab3_tableWidget.setHorizontalHeaderLabels(header)
                traceback.print_exc()

        elif tab == 3 and win == 1:
            # val1=최소날짜, val2=최대날짜, val4=펀드코드
            header = ['기준일자', '기준가격', '전일대비', '설정금액', '설정좌수', '당일설정좌수', '당일해지좌수', '좌수증감', '총자산', '총자산일간변동', '순자산',
                      '순자산일간변동']
            try:
                if re == "":
                    sql += query.returnSQL('tab3_win1SearchQuery').format(val4)
                    # print(sql)
                    cur.execute(sql)
                    row = cur.fetchall()
                    df = pd.DataFrame(row)
                elif re == "re":
                    minDate = val1
                    maxDate = val2
                    df = Ui_MainWindow.mainWindow_df3_1.copy()
                    if self.tab3_win1checkBox.isChecked():
                        df = df.query('기준일자>=@minDate')
                    if self.tab3_win1checkBox_2.isChecked():
                        df = df.query('기준일자<=@maxDate')
                df.columns = header
                self.tab3_win1tableWidget.setColumnCount(len(df.columns))
                self.tab3_win1tableWidget.setRowCount(len(df.index))
                self.tab3_win1tableWidget.setHorizontalHeaderLabels(header)
                self.setTableData(df, 3, 1, startTime, '')
                if re == "":
                    Ui_MainWindow.mainWindow_df3_1 = df.copy()
                Ui_MainWindow.mainWindow_df3_1Re = df.copy()
                self.tab3_win1tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정
            except:
                self.tab3_win1tableWidget.clear()
                self.tab3_win1tableWidget.setRowCount(1)
                self.tab3_win1tableWidget.setColumnCount(len(header))
                self.tab3_win1tableWidget.setHorizontalHeaderLabels(header)
                traceback.print_exc()

        elif tab == 3 and win == 2:
            # val1=클릭한 박스
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
                    Ui_MainWindow.mainWindow_df3_2 = df.copy()
                Ui_MainWindow.mainWindow_df3_2Re = df.copy()
                self.tab3_win2tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정

            except:
                self.tab3_win2tableWidget.clear()
                self.tab3_win2tableWidget.setRowCount(1)
                self.tab3_win2tableWidget.setColumnCount(len(header))
                self.tab3_win2tableWidget.setHorizontalHeaderLabels(header)
                traceback.print_exc()

        elif tab == 3 and win == 3:
            # val1=콤보박스1 값 val2=콤보박스2 값 ,val3=펀드코드
            alignRight = ['3', '4']  # 오른쪽 정렬할 숫자값들
            header = ['기준일자', '그룹', '수익자명', '구좌', '설정자산', '자산증감', '설정좌수', '좌수증감', '판매사']
            if val1 == '전체' and val2 == '':
                re = ''
            try:
                if re == "":
                    sql += query.returnSQL('tab3_win3SearchQuery').format(val3)
                    # print(sql)
                    cur.execute(sql)
                    row = cur.fetchall()
                    df = pd.DataFrame(row)
                    df.columns = header
                    self.tab3_win3tableWidget.setColumnCount(len(df.columns))
                    self.tab3_win3tableWidget.setRowCount(len(df.index))
                    self.tab3_win3tableWidget.setHorizontalHeaderLabels(header)
                    self.setTableData(df, 3, 3, '', alignRight)

                elif re == "re":
                    minDate = self.tab3_win3dateEdit.text()
                    maxDate = self.tab3_win3dateEdit_2.text()

                    df = Ui_MainWindow.mainWindow_df3_3
                    if self.tab3_win3checkBox.isChecked():
                        df = df.query('기준일자>=@minDate')
                    if self.tab3_win3checkBox_2.isChecked():
                        df = df.query('기준일자<=@maxDate')
                    if val1 != '전체':
                        df = df.query('수익자명==@val1')
                    if val2 != '전체':
                        val2 = int(val2)
                        df = df.query('구좌==@val2')
                    df.columns = header
                    self.tab3_win3tableWidget.setColumnCount(len(df.columns))
                    self.tab3_win3tableWidget.setRowCount(len(df.index))
                    self.tab3_win3tableWidget.setHorizontalHeaderLabels(header)
                    self.setTableData(df, 3, 3, '', alignRight)
                    Ui_MainWindow.mainWindow_df3_3Re = df.copy()
                if re == "":
                    self.tab3_win3comboBox.addItem("전체")
                    groupd = df.groupby(['수익자명']).count().iloc[:, 0]
                    [self.tab3_win3comboBox.addItem(str(i)) for i in groupd.index]
                    self.tab3_win3comboBox_2.addItem('전체')
                    Ui_MainWindow.mainWindow_df3_3 = df.copy()
                    Ui_MainWindow.mainWindow_df3_3Re = df.copy()
                if len(df.index) == 0:
                    self.tab3_win3tableWidget.setRowCount(1)
                self.tab3_win3tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정
            except:
                self.tab3_win3tableWidget.clear()
                self.tab3_win3tableWidget.setRowCount(1)
                self.tab3_win3tableWidget.setColumnCount(len(header))
                self.tab3_win3tableWidget.setHorizontalHeaderLabels(header)
                traceback.print_exc()

        elif tab == 4 and win == 0:
            # val=날짜1, val2=날짜2, val3=수익자명
            header = ['일자', '수익그룹', '수익자명', '구좌', '설정금액', '증감', '본부', '고객그룹', '유형']
            try:
                if re == "":
                    sql += query.returnSQL('tab4_searchQuery').format(val1.replace('-', '/'), val2.replace('-', '/'))
                    if val3 != '전체':
                        sql += " and suik_name='{}'".format(val3)
                    # print(sql)
                    cur.execute(sql)
                    row = cur.fetchall()
                    df = pd.DataFrame(row)
                df.columns = header
                val = (df['수익자명'].drop_duplicates().values.tolist())
                val.sort()
                [self.tab4_comboBox.addItem(i) for i in val]

                self.tab4_tableWidget.setColumnCount(len(df.columns))
                self.tab4_tableWidget.setRowCount(len(df.index))
                self.tab4_tableWidget.setHorizontalHeaderLabels(header)
                self.setTableData(df, 4, 0, startTime, '')
                if re == "":
                    Ui_MainWindow.mainWindow_df4_0 = df
                self.tab4_tableWidget.resizeColumnsToContents()  # 컬럼 크기 조정

            except:
                self.tab4_tableWidget.clear()
                self.tab4_tableWidget.setRowCount(1)
                self.tab4_tableWidget.setColumnCount(len(header))
                self.tab4_tableWidget.setHorizontalHeaderLabels(header)
                traceback.print_exc()

        elif tab == 5 and win == 0:
            # val1=날짜
            header = ['고객그룹', '설정액 합', '설정액', '전월말대비', '전분기말대비', '전년말대비', '설정액', '전월말대비', '전분기말대비', '전년말대비']
            try:
                if re == "":
                    sql += query.returnSQL('tab5_searchQuery').format(date=val1,month=val1[0:7])
                    # print(sql)
                    cur.execute(sql)
                    row = cur.fetchall()
                    df = pd.DataFrame(row)
                df.columns = header
                self.tab5_tableWidget.setColumnCount(len(df.columns))
                self.tab5_tableWidget.setRowCount(len(df.index))
                self.tab5_tableWidget.setHorizontalHeaderLabels(header)
                Ui_MainWindow.mainWindow_df5_0 = df.copy()
                self.setTableData(df, 5, 0, '', '')
                self.tab5_tableWidget.resizeColumnsToContents()
                if self.tab5_tableWidget.rowCount() >= 10:
                    indexWidth = 23
                else:
                    indexWidth = 16
                width1 = self.tab5_tableWidget.columnWidth(0) + self.tab5_tableWidget.columnWidth(1)  # 헤더 사이즈 조정
                width2 = self.tab5_tableWidget.columnWidth(2)+ self.tab5_tableWidget.columnWidth(3) + \
                         self.tab5_tableWidget.columnWidth(4) + self.tab5_tableWidget.columnWidth(5)
                width3 = self.tab5_tableWidget.columnWidth(6) + self.tab5_tableWidget.columnWidth(7) \
                         + self.tab5_tableWidget.columnWidth(8) + self.tab5_tableWidget.columnWidth(9)
                self.tab5_lineEdit_2.setGeometry(QtCore.QRect(indexWidth + width1, 50, width2, 21))
                self.tab5_lineEdit_3.setGeometry(
                    QtCore.QRect(indexWidth + width1 + width2, 50, width3, 21))
            except:
                self.tab5_tableWidget.clear()
                self.tab5_tableWidget.setRowCount(1)
                self.tab5_tableWidget.setColumnCount(len(header))
                self.tab5_tableWidget.setHorizontalHeaderLabels(header)
                traceback.print_exc()

        elif tab == 5 and win == 1:
            # val1=group,val2=team,val3=NPS val4=날짜
            header = ['유형', '설정액', '순자산', '전월말대비', '전분기말대비', '전년말대비', '전전년말대비', '전월말', '전분기말', '전년말', '전전년말']
            try:
                if val3 == 'NPS':
                    val1 = '연기금'
                    val3 = '='
                else:
                    val3 = '<>'
                if re == "":
                    sql += query.returnSQL('tab5_win1searchQuery').format(date=val4, suik_group=val1, mg_bu=val2,
                                                                          nps=val3, month=val4[0:7])
                    # print(sql)
                    cur.execute(sql)
                    row = cur.fetchall()

                    if row:
                        df = pd.DataFrame(row)
                        df.columns = ['SUIK_NAME', 'INTE_FUND_TYPE', 'SUIK_SET_MONEY', 'SUIK_NET_MONEY',
                                      'SUIK_NET_MONEYSUM', 'SUIK_NET_MONEYSUM2',
                                      'SUIK_NET_MONEYSUM3', 'SUIK_NET_MONEYSUM4',
                                      'SUIK_SET_MONEY1', 'SUIK_SET_MONEY2', 'SUIK_SET_MONEY3', 'SUIK_SET_MONEY4']

                        Ui_MainWindow.mainWindow_df5_1 = df.copy()
                        self.tab5_win1comboBox.clear()
                        val = (df['SUIK_NAME'].drop_duplicates().values.tolist())
                        self.tab5_win1comboBox.addItem('전체')
                        [self.tab5_win1comboBox.addItem(i) for i in val]

                elif re == "re":
                    row=0
                    df = Ui_MainWindow.mainWindow_df5_1.copy()
                    suik_name = self.tab5_win1comboBox.currentText()
                    if self.tab5_win1comboBox.currentText() != '전체':
                        df = df.query("SUIK_NAME==@suik_name")
                if row or re == "re":
                    df = df.groupby(df['INTE_FUND_TYPE']).sum()
                    df = df.reset_index()
                    df.columns = header
                    Ui_MainWindow.mainWindow_df5_1Re = df.copy()
                    Ui_MainWindow.mainWindow_df5_1Ex = df.copy()
                    self.tab5_win1tableWidget.setColumnCount(len(df.columns))
                    self.tab5_win1tableWidget.setRowCount(len(df.index))
                    self.tab5_win1tableWidget.setHorizontalHeaderLabels(header)
                    self.setTableData(df, 5, 1, '', '')
                    self.tab5_win1tableWidget.resizeColumnsToContents()

                    if self.tab5_win1tableWidget.rowCount() >= 10:
                        indexWidth = 23
                    else:
                        indexWidth = 16
                    width1 = self.tab5_win1tableWidget.columnWidth(0) + self.tab5_win1tableWidget.columnWidth(
                        1) + self.tab5_win1tableWidget.columnWidth(2)  # 헤더 사이즈 조정
                    width2 = self.tab5_win1tableWidget.columnWidth(3) + self.tab5_win1tableWidget.columnWidth(
                        4) + self.tab5_win1tableWidget.columnWidth(5) + self.tab5_win1tableWidget.columnWidth(6)
                    width3 = self.tab5_win1tableWidget.columnWidth(7) + self.tab5_win1tableWidget.columnWidth(
                        8) + self.tab5_win1tableWidget.columnWidth(9) + self.tab5_win1tableWidget.columnWidth(10)
                    self.tab5_win1lineEdit_3.setGeometry(QtCore.QRect(indexWidth + width1, 50, width2, 21))
                    self.tab5_win1lineEdit_4.setGeometry(
                        QtCore.QRect(indexWidth + width1 + width2-1, 50, width3, 21))
                else:
                    self.tab5_win1tableWidget.setColumnCount(len(header))
                    self.tab5_win1tableWidget.setHorizontalHeaderLabels(header)
                    self.tab5_win1tableWidget.setRowCount(1)

            except:
                self.tab5_win1tableWidget.clear()
                self.tab5_win1tableWidget.setRowCount(1)
                self.tab5_win1tableWidget.setColumnCount(len(header))
                self.tab5_win1tableWidget.setHorizontalHeaderLabels(header)
                traceback.print_exc()

        elif tab == 5 and win == 2:
            # val1=Ui_MainWindow.mainWindow_df5_1, val2=항목값
            header = ['수익자명', '설정액', '순자산', '전월말대비', '전분기말대비', '전년말대비', '전전년말대비', '전월말', '전분기말', '전년말', '전전년말']
            try:
                df = val1
                if re == "":
                    items = val2
                    df = df.query("INTE_FUND_TYPE==@items")
                Ui_MainWindow.mainWindow_df5_2 = df.copy()
                df = df.groupby(df['SUIK_NAME']).sum()
                df = df.reset_index()
                df.columns = header
                Ui_MainWindow.mainWindow_df5_2Re = df.copy() #추후 조건줄때 사용할 용도
                Ui_MainWindow.mainWindow_df5_2Ex = df.copy()
                self.tab5_win2tableWidget.setColumnCount(len(df.columns))
                self.tab5_win2tableWidget.setRowCount(len(df.index))
                self.tab5_win2tableWidget.setHorizontalHeaderLabels(header)
                self.setTableData(df, 5, 2, '', '')
                self.tab5_win2tableWidget.resizeColumnsToContents()

                if self.tab5_win2tableWidget.rowCount() >= 10:
                    indexWidth = 23
                else:
                    indexWidth = 16
                width1 = self.tab5_win2tableWidget.columnWidth(0) + self.tab5_win2tableWidget.columnWidth(
                    1) + self.tab5_win2tableWidget.columnWidth(2)  # 헤더 사이즈 조정
                width2 = self.tab5_win2tableWidget.columnWidth(3) + self.tab5_win2tableWidget.columnWidth(
                    4) + self.tab5_win2tableWidget.columnWidth(5) + self.tab5_win2tableWidget.columnWidth(6)
                width3 = self.tab5_win2tableWidget.columnWidth(7) + self.tab5_win2tableWidget.columnWidth(
                    8) + self.tab5_win2tableWidget.columnWidth(9) + self.tab5_win2tableWidget.columnWidth(10)
                self.tab5_win2lineEdit_3.setGeometry(QtCore.QRect(indexWidth + width1, 60, width2, 21))
                self.tab5_win2lineEdit_4.setGeometry(
                    QtCore.QRect(indexWidth + width1 + width2-1, 60, width3,
                                 21))

            except:
                self.tab5_win2tableWidget.clear()
                self.tab5_win2tableWidget.setRowCount(1)
                self.tab5_win2tableWidget.setColumnCount(len(header))
                self.tab5_win2tableWidget.setHorizontalHeaderLabels(header)
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
                            self.tab3_tableWidget.item(i, j).setTextAlignment(
                                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            elif tab == 3 and win == 1:
                for i, arr in enumerate(nArray):
                    for j, val in enumerate(arr):
                        if self.parseFloat(val) != 0 or val == 0:
                            self.tab3_win1tableWidget.setItem(i, j, QTableWidgetItem(self.setComma(2,str(val),False)))
                            self.tab3_win1tableWidget.item(i, j).setTextAlignment(
                                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                            if float(val) < 0:
                                self.tab3_win1tableWidget.item(i, j).setBackground(Ui_MainWindow.minus)
                        else:
                            self.tab3_win1tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            elif tab == 3 and win == 2:
                for i, arr in enumerate(nArray):
                    [self.tab3_win2tableWidget.setItem(i, j, QTableWidgetItem(str(val))) for j, val in enumerate(arr)]
            elif tab == 3 and win == 3:
                for i, arr in enumerate(nArray):
                    for j, val in enumerate(arr):
                        if self.parseFloat(val) != 0 or val == 0:
                            self.tab3_win3tableWidget.setItem(i, j, QTableWidgetItem(self.setComma(2,str(val),False)))
                            self.tab3_win3tableWidget.item(i, j).setTextAlignment(
                                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                            if float(val) < 0:
                                self.tab3_win3tableWidget.item(i, j).setBackground(Ui_MainWindow.minus)
                        else:
                            self.tab3_win3tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            elif tab == 4 and win == 0:
                for i, arr in enumerate(nArray):
                    for j, val in enumerate(arr):
                        if j==4 or j==5:
                            self.tab4_tableWidget.setItem(i, j, QTableWidgetItem(self.setComma(1, val, True)))
                            self.tab4_tableWidget.item(i, j).setTextAlignment(
                                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                        else:
                            self.tab4_tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

            elif tab == 5 and win == 0:
                if self.tab5_comboBox.currentText() == '억':
                    Ui_MainWindow.tab5changeWonFlag=True
                else:
                    Ui_MainWindow.tab5changeWonFlag=False
                for i, arr in enumerate(nArray):
                    for j, val in enumerate(arr):
                        val=self.changeWon(val,Ui_MainWindow.tab5changeWonFlag)
                        if j == 0:
                            self.tab5_tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                            self.tab5_tableWidget.item(i, j).setTextAlignment(
                            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                        else:
                            self.tab5_tableWidget.setItem(i, j, QTableWidgetItem(self.setComma(1,val,True)))
                            self.tab5_tableWidget.item(i, j).setTextAlignment(
                            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                        if j == 1:
                            self.tab5_tableWidget.item(i, j).setBackground(Ui_MainWindow.bold)
                        Ui_MainWindow.mainWindow_df5_0.iloc[i,j]=val

            elif tab == 5 and win == 1:
                calval=0
                if self.tab5_win1comboBox_2.currentText() == '억':
                    Ui_MainWindow.tab5changeWonFlag = True
                else:
                    Ui_MainWindow.tab5changeWonFlag = False
                for i, arr in enumerate(nArray):
                    for j, val in enumerate(arr):
                        val = self.changeWon(val, Ui_MainWindow.tab5changeWonFlag)
                        if j == 0:
                            self.tab5_win1tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                            self.tab5_win1tableWidget.item(i, j).setTextAlignment(
                                QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                        else:
                            if j == 2 and self.tab5_win1lineEdit_3.text()=='순자산 증감':
                                calval=val
                                self.tab5_win1tableWidget.setItem(i, j, QTableWidgetItem(self.setComma(1,val,True)))
                            elif j >2 and j<7:
                                self.tab5_win1tableWidget.setItem(i, j, QTableWidgetItem(self.setComma(1,calval-val,True)))
                                val = calval-val
                            else:
                                self.tab5_win1tableWidget.setItem(i, j, QTableWidgetItem(self.setComma(1,val,True)))
                            self.tab5_win1tableWidget.item(i, j).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                        Ui_MainWindow.mainWindow_df5_1Ex.iloc[i, j] = val
                self.tab5_win1tableWidget.insertRow(len(df.index))
                self.tab5_win1tableWidget.setItem(len(df.index), 0, QTableWidgetItem('합계'))
                self.tab5_win1tableWidget.item(len(df.index), 0).setTextAlignment(
                    QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                if not df.empty:
                    sumList = df.sum()
                    sumList[0] = '합계'
                    calval=0

                    for k in range(1, 11):
                        sumList[k] = self.changeWon(sumList[k], Ui_MainWindow.tab5changeWonFlag)
                        if k== 2 and self.tab5_win1lineEdit_3.text()=='순자산 증감':
                            calval=sumList[k]
                            self.tab5_win1tableWidget.setItem(len(df.index), k,
                                 QTableWidgetItem(self.setComma(1,sumList[k],True)))

                        elif k>2 and k<7:
                            self.tab5_win1tableWidget.setItem(len(df.index), k,
                                 QTableWidgetItem(self.setComma(1,calval-sumList[k],True)))
                            sumList[k]=calval - sumList[k]
                        else:
                            self.tab5_win1tableWidget.setItem(len(df.index), k,
                                 QTableWidgetItem(self.setComma(1,sumList[k],True)))
                        self.tab5_win1tableWidget.item(len(df.index), k).setTextAlignment(
                                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                    sumList_df=pd.DataFrame(columns=sumList.index)
                    sumList_df.loc[0]=sumList
                    Ui_MainWindow.mainWindow_df5_1Ex = pd.concat([Ui_MainWindow.mainWindow_df5_1Ex, sumList_df],
                                                                 ignore_index=True)

            elif tab == 5 and win == 2:
                calval = 0
                if self.tab5_win2comboBox.currentText() == '억':
                    Ui_MainWindow.tab5changeWonFlag = True
                else:
                    Ui_MainWindow.tab5changeWonFlag = False
                for i, arr in enumerate(nArray):
                    for j, val in enumerate(arr):
                        val = self.changeWon(val, Ui_MainWindow.tab5changeWonFlag)
                        if j == 0:
                            self.tab5_win2tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                            self.tab5_win2tableWidget.item(i, j).setTextAlignment(
                                QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                        else:
                            if j==2 and self.tab5_win2lineEdit_3.text()=='순자산 증감':
                                calval=val
                                self.tab5_win2tableWidget.setItem(i, j, QTableWidgetItem(self.setComma(1,val,True)))
                            elif j>2 and j<7:
                                self.tab5_win2tableWidget.setItem(i, j, QTableWidgetItem(self.setComma(1,calval-val,True)))
                                val=calval-val
                            else:
                                self.tab5_win2tableWidget.setItem(i, j, QTableWidgetItem(self.setComma(1,val,True)))
                            self.tab5_win2tableWidget.item(i, j).setTextAlignment(
                                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                        Ui_MainWindow.mainWindow_df5_2Ex.iloc[i, j] = val
                self.tab5_win2tableWidget.insertRow(len(df.index))
                self.tab5_win2tableWidget.setItem(len(df.index), 0, QTableWidgetItem('합계'))
                self.tab5_win2tableWidget.item(len(df.index), 0).setTextAlignment(
                    QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

                if not df.empty:
                    sumList = df.sum()
                    sumList[0] = '합계'
                    calval=0

                    for k in range(1, 11):
                        sumList[k] = self.changeWon(sumList[k], Ui_MainWindow.tab5changeWonFlag)
                        if k==2 and self.tab5_win2lineEdit_3.text()=='순자산 증감':
                            calval = sumList[k]
                            self.tab5_win2tableWidget.setItem(len(df.index), k,
                                                              QTableWidgetItem(self.setComma(1, sumList[k], True)))
                        if k>2 and k<7:
                            self.tab5_win2tableWidget.setItem(len(df.index), k,
                                                              QTableWidgetItem(self.setComma(1, calval-sumList[k], True)))
                            sumList[k] = calval - sumList[k]
                        else:
                            self.tab5_win2tableWidget.setItem(len(df.index), k,
                                        QTableWidgetItem(self.setComma(1,sumList[k],True)))
                        self.tab5_win2tableWidget.item(len(df.index), k).setTextAlignment(
                            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    sumList_df = pd.DataFrame(columns=sumList.index)
                    sumList_df.loc[0] = sumList
                    Ui_MainWindow.mainWindow_df5_2Ex = pd.concat([Ui_MainWindow.mainWindow_df5_2Ex, sumList_df],
                                                                 ignore_index=True)


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

    def setComma(self,types,val,tostr):
        """1000 단위 콤마 붙여서 리턴 types= 1정수(소수점 반올림), 2소수, tostr= True 문자 반환, False 그대로반환"""
        try:
            if len(str(val)) >= Ui_MainWindow.commaLength:
                if types==1 and val!=0:
                    val = format(int(val), ",")
                elif types==2 and val!=0:
                    val = format(float(val), ",")
            if tostr==True:
                return str(val)
            return val
        except:
            traceback.print_exc()

    def delComma(self, val):
        """1000 단위 콤마 제거해서 리턴"""
        try:
            val = val.replace(',', '')
            return val
        except:
            traceback.print_exc()

    def toExcel(self, tab, win, title):
        """엑셀 변환 저장 tab은 탭, win은 창 번호(메인은 0) 저장시 셀칸 늘리는건 해결 못 함"""
        try:
            a = QMessageBox()
            lengthCal = []
            rowCount=0
            if tab == "1" and win == "0":
                rowCount = len(Ui_MainWindow.mainWindow_df1_0)
            elif tab == "3" and win == "1":
                rowCount = len(Ui_MainWindow.mainWindow_df3_1Re)
            elif tab == "3" and win == "3":
                rowCount = len(Ui_MainWindow.mainWindow_df3_3Re)
            if tab == "5" and win == "0":
                rowCount = len(Ui_MainWindow.mainWindow_df5_0)
            elif tab == "5" and win == "1":
                rowCount = len(Ui_MainWindow.mainWindow_df5_1Ex)
            elif tab == "5" and win == "2":
                rowCount = len(Ui_MainWindow.mainWindow_df5_2Ex)
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
                    elif tab == "5" and win == "0":
                        header = ['고객그룹', '설정액 합', '홀세일1 설정액', '홀세일1 전월말',
                                  '홀세일1 전분기말', '홀세일1 전년말','홀세일2 설정액',
                                  '홀세일2 전월말', '홀세일2 전분기말', '홀세일2 전년말']
                        df=Ui_MainWindow.mainWindow_df5_0
                        df.columns = header
                        excel_writer = StyleFrame.ExcelWriter(excelPath)
                        sf = StyleFrame(df)
                        sf.apply_headers_style(styler_obj=Styler(bg_color=utils.colors.grey))
                        for i, val in enumerate(header):
                            if len(str(df.max()[i]))>len(val):  # 단위: 원
                                sf.apply_column_style(cols_to_style=[val],
                                                      styler_obj=Styler(horizontal_alignment='right',
                                                                        number_format='#,##0',font_size=11),
                                                      width=(len(df.max())*17.5/8.05)+1)
                            else: #단위: 억
                                sf.apply_column_style(cols_to_style=[val],
                                                      styler_obj=Styler(horizontal_alignment='right',
                                                                        number_format='#,##0',font_size=11),
                                                      width=(len(val)*17.5/8.05)+1)
                        sf.apply_column_style(cols_to_style=['고객그룹'],styler_obj=Styler(horizontal_alignment='left'))
                        sf.to_excel(
                            excel_writer=excel_writer,best_fit=None, columns_and_rows_to_freeze=None
                        )
                        excel_writer.save()
                    elif tab == "5" and win == "1":
                        header = ['유형','설정액', '순자산',
                                  '순자산 전월말', '순자산 전분기말','순자산 전년말', '순자산 전전년말',
                                  '수탁고 전월말','수탁고 전분기말', '수탁고 전년말', '수탁고 전전년말']
                        df = Ui_MainWindow.mainWindow_df5_1Ex
                        df.columns = header
                        excel_writer = StyleFrame.ExcelWriter(excelPath)
                        sf = StyleFrame(df)
                        sf.apply_headers_style(styler_obj=Styler(bg_color=utils.colors.grey))

                        for i, val in enumerate(header):
                            lengthCal = [len(str(j)) for j in df.iloc[:, i]]
                            if max(lengthCal) > len(val):  # 단위: 원
                                sf.apply_column_style(cols_to_style=[val],
                                                      styler_obj=Styler(horizontal_alignment='right',
                                                                        number_format='#,##0',font_size=11),
                                                      width=(max(lengthCal) * 12 / 8.5) + 4)
                            else:  # 단위: 억
                                sf.apply_column_style(cols_to_style=[val],
                                                      styler_obj=Styler(horizontal_alignment='right',
                                                                        number_format='#,##0',font_size=11),
                                                      width=(len(val) * 12 / 8.5) + 6)
                        sf.apply_column_style(cols_to_style=['유형'], styler_obj=Styler(horizontal_alignment='left'))
                        sf.to_excel(
                            excel_writer=excel_writer, best_fit=None, columns_and_rows_to_freeze=None
                        )
                        excel_writer.save()
                    elif tab == "5" and win == "2":
                        header = ['수익자명','설정액', '순자산',
                                  '순자산 전월말', '순자산 전분기말','순자산 전년말', '순자산 전전년말',
                                  '수탁고 전월말','수탁고 전분기말', '수탁고 전년말', '수탁고 전전년말']
                        df = Ui_MainWindow.mainWindow_df5_2Ex
                        df.columns = header
                        excel_writer = StyleFrame.ExcelWriter(excelPath)
                        sf = StyleFrame(df)
                        sf.apply_headers_style(styler_obj=Styler(bg_color=utils.colors.grey))

                        for i, val in enumerate(header):
                            lengthCal = [len(str(j)) for j in df.iloc[:, i]]
                            if max(lengthCal) > len(val):  # 단위: 원
                                sf.apply_column_style(cols_to_style=[val],
                                                      styler_obj=Styler(horizontal_alignment='right',
                                                                        number_format='#,##0',font_size=11),
                                                      width=(max(lengthCal) * 12 / 8.5) + 4)
                            else:  # 단위: 억
                                sf.apply_column_style(cols_to_style=[val],
                                                      styler_obj=Styler(horizontal_alignment='right',
                                                                        number_format='#,##0',font_size=11),
                                                      width=(len(val) * 12 / 8.5) + 6)
                        sf.apply_column_style(cols_to_style=['수익자명'], styler_obj=Styler(horizontal_alignment='left'))
                        sf.to_excel(
                            excel_writer=excel_writer, best_fit=None, columns_and_rows_to_freeze=None
                        )
                        excel_writer.save()



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

    def parseFloat(self, par):
        """정수, 실수만 실수타입으로 변환해 리턴 그 외에는 0리턴"""
        try:
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
                returnvalue = par
                returnvalue = decimal.Decimal(par) #int64->decimal 변환 안됨
            return returnvalue
        except:
            traceback.print_exc()

    def changeWon(self,val,flag):
        """숫자 받아 나눈 뒤에 int값으로 반환, val=값, flag=사용체크 여부"""
        try:
            if (str(type(val)).find('int')>0 or str(type(val)).find('float')>0) and flag==True:
                val=int(math.floor(val/Ui_MainWindow.won))
            if (str(type(val)).find('int')>0 or str(type(val)).find('float')>0) and flag==False:
                val=int(math.floor(val))
            return val
        except:
            traceback.print_exc()

    def test(self):
        try:
            header = ['고객그룹', '설정액 합', '홀세일1 설정액', '홀세일1 전월말대비', '홀세일1 전분기말대비', '홀세일1 전년말대비', '', '설정액1', '전월말대비', '전분기말대비', '전년말대비']
            pp = [('NPS', '0', '3', '4','5','6','7','7','8','9'),
                  ('공제회', '0', '7', '8','5','6','6','7','8','9'),
                  ('금융일반', '0', '11', '12','5','6','6','7','8','9'),
                  ('일반법인', '0', '11', '12','5','6','','7','8','9')]
            headers=['고객그룹','설정액 합','홀세일1설정액','홀세일1전월','홀세일1전분기','홀세일1전년', '홀세일2설정액', '홀세일2전월', '홀세일2전분기', '홀세일2전년']
            df11 = pd.DataFrame(pp)
            df11.columns=headers
            print(df11)
            df13=Ui_MainWindow.mainWindow_df5_0
            print(df13)
            self.asd(df13,headers)


        except:
            traceback.print_exc()

    def asd(self, dfaa,columns):
        try:
            dfaa.columns=columns
            excel_writer = StyleFrame.ExcelWriter('example.xlsx')
            sf = StyleFrame(dfaa,Styler(horizontal_alignment='right'))
            sf.to_excel(
                excel_writer=excel_writer,
                best_fit=columns, columns_and_rows_to_freeze=None
            )
            sf.apply_column_style(cols_to_style=['홀세일1설정액'],
                                  styler_obj=Styler(font_color=utils.colors.green, bold=True),
                                  style_header=True)
            excel_writer.save()

        except:
            traceback.print_exc()

    def closeApp(self):
        """프로그램 종료시"""
        print('종료')

    # ---------------------------------메뉴바

    def popup1(self, update):
        self.popup1_label = QtWidgets.QLabel(self.popup_version)
        self.popup1_label.setGeometry(QtCore.QRect(74, 3, 61, 16))
        self.popup1_label.setObjectName("popup1_label")
        self.popup1_label_2 = QtWidgets.QLabel(self.popup_version)
        self.popup1_label_2.setGeometry(QtCore.QRect(140, 3, 61, 16))
        self.popup1_label_2.setAutoFillBackground(True)
        self.popup1_label_2.setText("")
        self.popup1_label_2.setObjectName("popup1_label_2")
        self.popup1_label_3 = QtWidgets.QLabel(self.popup_version)
        self.popup1_label_3.setGeometry(QtCore.QRect(74, 50, 41, 21))
        self.popup1_label_3.setObjectName("popup1_label_3")
        self.popup1_label_4 = QtWidgets.QLabel(self.popup_version)
        self.popup1_label_4.setGeometry(QtCore.QRect(116, 50, 41, 21))
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
        self.popup1_label_6 = QtWidgets.QLabel(self.popup_version)
        self.popup1_label_6.setGeometry(QtCore.QRect(74, 28, 61, 16))
        self.popup1_label_6.setObjectName("popup1_label_6")
        self.popup1_label_7 = QtWidgets.QLabel(self.popup_version)
        self.popup1_label_7.setGeometry(QtCore.QRect(140, 28, 61, 16))
        self.popup1_label_7.setAutoFillBackground(True)
        self.popup1_label_7.setText("")
        self.popup1_label_7.setObjectName("popup1_label_7")
        self.popup1_pushbutton = QtWidgets.QPushButton(self.popup_version)
        self.popup1_pushbutton.setGeometry(QtCore.QRect(208, 0, 61, 23))
        self.popup1_pushbutton.setObjectName("popup1_pushbutton")
        self.popup1_pushbutton_2 = QtWidgets.QPushButton(self.popup_version)
        self.popup1_pushbutton_2.setGeometry(QtCore.QRect(208, 23, 61, 23))
        self.popup1_pushbutton_2.setObjectName("popup1_pushbutton_2")

        _translate = QtCore.QCoreApplication.translate

        self.popup1_label.setText(_translate("MainWindow", "해당 버전:"))
        self.popup1_label_3.setText(_translate("MainWindow", "개발자:"))
        self.popup1_label_4.setText(_translate("MainWindow", "송병규"))
        self.popup1_label_6.setText(_translate("MainWindow", "최신 버전:"))
        self.popup1_pushbutton.setText(_translate("MainWindow", "사이트"))
        self.popup1_pushbutton_2.setText(_translate("MainWindow", "다운로드"))

        # Qt디자이너 외 구현
        self.popup_version.resize(274, 69)
        self.popup1_label_2.setText(update)
        self.popup_version.setWindowModality(QtCore.Qt.ApplicationModal)  # 하위창 컨트롤 금지
        pixmap = QtGui.QPixmap(resource_path('ci.jpg'))
        pixmap = pixmap.scaledToHeight(int(60))
        self.popup1_label_5.setPixmap(pixmap)
        self.latestUpdate(update)
        self.popup_version.show()




        # 이벤트
        self.popup1_pushbutton.clicked.connect(lambda: self.linkSite(3))  # 사이트 접속
        self.popup1_pushbutton_2.clicked.connect(lambda: self.linkSite(4))  # 최신버전 다운

    def latestUpdate(self,update):
        """홈페이지 업데이트 날짜 긁어옴"""
        try:
            newdate=[]
            req = requests.get(Ui_MainWindow.userinfo['ip']+':5000/download')
            soup = bs4.BeautifulSoup(req.text, "html.parser")
            soup = soup.findAll('a', {'id': 'recently'})
            for i in soup:
                newdate=i.get_text().replace('/','-')
            self.popup1_label_7.setText(newdate)
            newdate=parse(newdate)
            update=parse(update)
            if update==newdate:
                self.popup1_pushbutton_2.hide()
            elif update<newdate:
                self.popup1_label_7.setStyleSheet('color: red')
                self.popup1_pushbutton.show()
                self.popup1_pushbutton_2.show()
            else:
                self.popup1_label_7.setStyleSheet('color: red')
                self.popup1_pushbutton.show()
                self.popup1_pushbutton_2.show()

        except:
            traceback.print_exc()
            self.popup1_label_7.setText('접속 불가')
            self.popup1_label_7.setStyleSheet('color: red')
            self.popup1_pushbutton.hide()
            self.popup1_pushbutton_2.hide()

    def linkSite(self, val1):
        """링크 혹은 다운로드"""
        try:
            if val1 == 1:
                webbrowser.open('https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableWidget.html')
            elif val1 == 2:
                webbrowser.open('https://wikidocs.net/')
            elif val1 == 3:
                webbrowser.open_new(Ui_MainWindow.userinfo['ip']+':5000/download/')
            elif val1 == 4:
                if os.path.exists('main.exe'):
                    print('~')
                    url = Ui_MainWindow.userinfo['ip'] + ':5000/static/file/hkamudfl.exe'
                    urllib.request.urlretrieve(url, "hkamudfl.exe")
                    os.startfile('hkamudfl.exe')
                    os._exit(1)
                else:
                    print('~~')
                    url = Ui_MainWindow.userinfo['ip'] + ':5000/static/file/main.exe'
                    urllib.request.urlretrieve(url, "main.exe")
                    os._exit(1)
        except:
            traceback.print_exc()

    # ---------------------------------------main

if __name__ == '__main__':
    server=[{'id': 'system', 'pw': '1234','connect': 'localhost:1521/xe', 'ip':'http://192.168.123.3'},
           {'id': 'HKCL','pw': 'hkcl','connect': '11.10.5.11:1521/hkfund', 'ip':'http://11.10.5.34'}]
    userinfo={}
    if socket.gethostbyname(socket.gethostname())=='192.168.123.3':
        userinfo.update(server[0])
        print('테스트용')
    else:
        userinfo.update(server[1])
        print('개발용')

    conn = cx_Oracle.connect(userinfo['id'],userinfo['pw'],userinfo['connect'])
    cur = conn.cursor()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# 현재 setcomma에서 length 값 이하는 표시가 안되고 그걸 내리면 더블클릭시 코드값을 잘못 가져감

# conn = cx_Oracle.connect("HKCL", "hkcl", "11.10.5.11:1521/hkfund")
# conn = cx_Oracle.connect("system", "1234", "localhost:1521/xe")
# pyuic5 -x mainFrame.ui -o mainFrame.py
# pyuic5 -x popupVersion.ui -o popupVersion.py
# pyuic5 -x windowQuery.ui -o windowQuery.py
# pyuic5 -x windowGraphic.ui -o windowGraphic.py
# pyuic5 -x windowList.ui -o windowList.py
# pyuic5 -x windowCode.ui -o windowCode.py
# pyuic5 -x windowEarn.ui -o windowEarn.py
# pyuic5 -x windowGroup.ui -o windowGroup.py
# pyuic5 -x windowItems.ui -o windowItems.py
# gcc -c clang.c
# gcc -o clang.so -shared -f PIC clang.c