# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainForm.setWindowIcon(icon)
        MainForm.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setObjectName("label")
        self.tableLesh = QtWidgets.QTableWidget(self.tab)
        self.tableLesh.setGeometry(QtCore.QRect(3, 30, 251, 251))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableLesh.setFont(font)
        self.tableLesh.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableLesh.setLineWidth(1)
        self.tableLesh.setMidLineWidth(0)
        self.tableLesh.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableLesh.setAlternatingRowColors(False)
        self.tableLesh.setRowCount(0)
        self.tableLesh.setObjectName("tableLesh")
        self.tableLesh.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableLesh.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableLesh.setHorizontalHeaderItem(1, item)
        self.tableLesh.horizontalHeader().setCascadingSectionResizes(False)
        self.tableLesh.horizontalHeader().setDefaultSectionSize(117)
        self.tableLesh.verticalHeader().setDefaultSectionSize(23)
        self.startLesh = QtWidgets.QPushButton(self.tab)
        self.startLesh.setGeometry(QtCore.QRect(10, 530, 75, 23))
        self.startLesh.setStyleSheet("background-color: rgb(111, 111, 83);\n"
"color: #fff")
        self.startLesh.setObjectName("startLesh")
        self.stopLesh = QtWidgets.QPushButton(self.tab)
        self.stopLesh.setGeometry(QtCore.QRect(90, 530, 75, 23))
        self.stopLesh.setStyleSheet("background-color: rgb(111, 111, 83);\n"
"color: #fff")
        self.stopLesh.setObjectName("stopLesh")
        self.tableGustera = QtWidgets.QTableWidget(self.tab)
        self.tableGustera.setGeometry(QtCore.QRect(257, 30, 256, 251))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableGustera.setFont(font)
        self.tableGustera.setRowCount(0)
        self.tableGustera.setObjectName("tableGustera")
        self.tableGustera.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableGustera.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableGustera.setHorizontalHeaderItem(1, item)
        self.tableGustera.horizontalHeader().setDefaultSectionSize(119)
        self.tableGustera.verticalHeader().setDefaultSectionSize(23)
        self.tableBeloglazka = QtWidgets.QTableWidget(self.tab)
        self.tableBeloglazka.setGeometry(QtCore.QRect(517, 30, 256, 251))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableBeloglazka.setFont(font)
        self.tableBeloglazka.setRowCount(0)
        self.tableBeloglazka.setObjectName("tableBeloglazka")
        self.tableBeloglazka.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableBeloglazka.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableBeloglazka.setHorizontalHeaderItem(1, item)
        self.tableBeloglazka.horizontalHeader().setDefaultSectionSize(119)
        self.tableBeloglazka.verticalHeader().setDefaultSectionSize(23)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(6, 293, 191, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(260, 10, 251, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(520, 10, 211, 16))
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(4, 310, 769, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(0, 67, 0);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.lcdLesh = QtWidgets.QLCDNumber(self.tab)
        self.lcdLesh.setGeometry(QtCore.QRect(671, 510, 101, 23))
        self.lcdLesh.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdLesh.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdLesh.setDigitCount(10)
        self.lcdLesh.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdLesh.setObjectName("lcdLesh")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(4, 300, 768, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background-color: rgb(0, 67, 0);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.btnStartRipus = QtWidgets.QPushButton(self.tab_2)
        self.btnStartRipus.setGeometry(QtCore.QRect(10, 520, 75, 23))
        self.btnStartRipus.setStyleSheet("background-color: rgb(111, 111, 83);\n"
"color: #fff")
        self.btnStartRipus.setObjectName("btnStartRipus")
        self.btnStopRipus = QtWidgets.QPushButton(self.tab_2)
        self.btnStopRipus.setGeometry(QtCore.QRect(90, 520, 75, 23))
        self.btnStopRipus.setStyleSheet("background-color: rgb(111, 111, 83);\n"
"color: #fff")
        self.btnStopRipus.setObjectName("btnStopRipus")
        self.lcdRipus = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdRipus.setGeometry(QtCore.QRect(680, 510, 91, 23))
        self.lcdRipus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdRipus.setDigitCount(10)
        self.lcdRipus.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdRipus.setObjectName("lcdRipus")
        self.tableRipus = QtWidgets.QTableWidget(self.tab_2)
        self.tableRipus.setGeometry(QtCore.QRect(10, 50, 360, 202))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableRipus.setFont(font)
        self.tableRipus.setObjectName("tableRipus")
        self.tableRipus.setColumnCount(2)
        self.tableRipus.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableRipus.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableRipus.setHorizontalHeaderItem(1, item)
        self.tableRipus.horizontalHeader().setDefaultSectionSize(153)
        self.tableRipus.verticalHeader().setDefaultSectionSize(23)
        self.tableKorushka = QtWidgets.QTableWidget(self.tab_2)
        self.tableKorushka.setGeometry(QtCore.QRect(407, 50, 360, 202))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableKorushka.setFont(font)
        self.tableKorushka.setObjectName("tableKorushka")
        self.tableKorushka.setColumnCount(2)
        self.tableKorushka.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableKorushka.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableKorushka.setHorizontalHeaderItem(1, item)
        self.tableKorushka.horizontalHeader().setDefaultSectionSize(153)
        self.tableKorushka.verticalHeader().setDefaultSectionSize(23)
        self.lcdR = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdR.setGeometry(QtCore.QRect(110, 251, 161, 23))
        self.lcdR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdR.setDigitCount(18)
        self.lcdR.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdR.setObjectName("lcdR")
        self.lcdK = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdK.setGeometry(QtCore.QRect(510, 251, 161, 23))
        self.lcdK.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdK.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdK.setDigitCount(18)
        self.lcdK.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdK.setObjectName("lcdK")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(160, 17, 81, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(550, 20, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(7, 282, 171, 16))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(3, 291, 770, 211))
        self.textBrowser_3.setStyleSheet("background-color: rgb(0, 67, 0);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.btnStartSig = QtWidgets.QPushButton(self.tab_3)
        self.btnStartSig.setGeometry(QtCore.QRect(10, 520, 75, 23))
        self.btnStartSig.setStyleSheet("background-color: rgb(111, 111, 83);\n"
"color: #fff")
        self.btnStartSig.setObjectName("btnStartSig")
        self.btnStopSig = QtWidgets.QPushButton(self.tab_3)
        self.btnStopSig.setGeometry(QtCore.QRect(90, 520, 75, 23))
        self.btnStopSig.setStyleSheet("background-color: rgb(111, 111, 83);\n"
"color: #fff")
        self.btnStopSig.setObjectName("btnStopSig")
        self.tableRybec = QtWidgets.QTableWidget(self.tab_3)
        self.tableRybec.setGeometry(QtCore.QRect(3, 40, 251, 221))
        self.tableRybec.setRowCount(8)
        self.tableRybec.setObjectName("tableRybec")
        self.tableRybec.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableRybec.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableRybec.setHorizontalHeaderItem(1, item)
        self.tableRybec.verticalHeader().setDefaultSectionSize(23)
        self.tableSig = QtWidgets.QTableWidget(self.tab_3)
        self.tableSig.setGeometry(QtCore.QRect(263, 40, 251, 221))
        self.tableSig.setRowCount(8)
        self.tableSig.setObjectName("tableSig")
        self.tableSig.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableSig.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableSig.setHorizontalHeaderItem(1, item)
        self.tableSig.verticalHeader().setDefaultSectionSize(23)
        self.tableLudoga = QtWidgets.QTableWidget(self.tab_3)
        self.tableLudoga.setGeometry(QtCore.QRect(522, 40, 251, 221))
        self.tableLudoga.setRowCount(8)
        self.tableLudoga.setObjectName("tableLudoga")
        self.tableLudoga.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableLudoga.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableLudoga.setHorizontalHeaderItem(1, item)
        self.tableLudoga.verticalHeader().setDefaultSectionSize(23)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(60, 20, 131, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(330, 20, 141, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(580, 20, 131, 16))
        self.label_9.setObjectName("label_9")
        self.lcdSig = QtWidgets.QLCDNumber(self.tab_3)
        self.lcdSig.setGeometry(QtCore.QRect(671, 501, 101, 23))
        self.lcdSig.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdSig.setDigitCount(10)
        self.lcdSig.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdSig.setObjectName("lcdSig")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(5, 274, 171, 16))
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(3, 300, 771, 211))
        self.textBrowser_4.setStyleSheet("background-color: rgb(0, 67, 0);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.btnStartShuka = QtWidgets.QPushButton(self.tab_4)
        self.btnStartShuka.setGeometry(QtCore.QRect(10, 524, 75, 23))
        self.btnStartShuka.setStyleSheet("background-color: rgb(111, 111, 83);\n"
"color: #fff")
        self.btnStartShuka.setObjectName("btnStartShuka")
        self.btnStopShuka = QtWidgets.QPushButton(self.tab_4)
        self.btnStopShuka.setGeometry(QtCore.QRect(90, 524, 75, 23))
        self.btnStopShuka.setStyleSheet("background-color: rgb(111, 111, 83);\n"
"color: #fff")
        self.btnStopShuka.setObjectName("btnStopShuka")
        self.lcdShuka = QtWidgets.QLCDNumber(self.tab_4)
        self.lcdShuka.setGeometry(QtCore.QRect(673, 510, 101, 23))
        self.lcdShuka.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdShuka.setDigitCount(10)
        self.lcdShuka.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdShuka.setObjectName("lcdShuka")
        self.tableShuka = QtWidgets.QTableWidget(self.tab_4)
        self.tableShuka.setGeometry(QtCore.QRect(20, 50, 256, 192))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableShuka.setFont(font)
        self.tableShuka.setRowCount(5)
        self.tableShuka.setObjectName("tableShuka")
        self.tableShuka.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableShuka.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableShuka.setHorizontalHeaderItem(1, item)
        self.tableShuka.horizontalHeader().setDefaultSectionSize(117)
        self.tableShuka.verticalHeader().setDefaultSectionSize(23)
        self.tableBigShuka = QtWidgets.QTableWidget(self.tab_4)
        self.tableBigShuka.setGeometry(QtCore.QRect(500, 50, 256, 192))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableBigShuka.setFont(font)
        self.tableBigShuka.setRowCount(1)
        self.tableBigShuka.setObjectName("tableBigShuka")
        self.tableBigShuka.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableBigShuka.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableBigShuka.setHorizontalHeaderItem(1, item)
        self.tableBigShuka.horizontalHeader().setDefaultSectionSize(117)
        self.tableBigShuka.verticalHeader().setDefaultSectionSize(23)
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(120, 30, 47, 13))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(580, 30, 101, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(6, 280, 281, 16))
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser_5.setGeometry(QtCore.QRect(2, 300, 772, 192))
        self.textBrowser_5.setStyleSheet("background-color: rgb(0, 67, 0);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.btnStartSudak = QtWidgets.QPushButton(self.tab_5)
        self.btnStartSudak.setGeometry(QtCore.QRect(10, 520, 75, 23))
        self.btnStartSudak.setStyleSheet("background-color: rgb(111, 111, 83);\n"
"color: #fff")
        self.btnStartSudak.setObjectName("btnStartSudak")
        self.btnStopSudak = QtWidgets.QPushButton(self.tab_5)
        self.btnStopSudak.setGeometry(QtCore.QRect(90, 520, 75, 23))
        self.btnStopSudak.setStyleSheet("background-color: rgb(111, 111, 83);\n"
"color: #fff")
        self.btnStopSudak.setObjectName("btnStopSudak")
        self.tableSudak = QtWidgets.QTableWidget(self.tab_5)
        self.tableSudak.setGeometry(QtCore.QRect(21, 50, 256, 192))
        self.tableSudak.setRowCount(5)
        self.tableSudak.setObjectName("tableSudak")
        self.tableSudak.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableSudak.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableSudak.setHorizontalHeaderItem(1, item)
        self.tableSudak.horizontalHeader().setDefaultSectionSize(117)
        self.tableSudak.verticalHeader().setDefaultSectionSize(23)
        self.tableBigSudak = QtWidgets.QTableWidget(self.tab_5)
        self.tableBigSudak.setGeometry(QtCore.QRect(500, 50, 256, 192))
        self.tableBigSudak.setRowCount(1)
        self.tableBigSudak.setObjectName("tableBigSudak")
        self.tableBigSudak.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableBigSudak.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableBigSudak.setHorizontalHeaderItem(1, item)
        self.tableBigSudak.horizontalHeader().setDefaultSectionSize(117)
        self.tableBigSudak.verticalHeader().setDefaultSectionSize(23)
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setGeometry(QtCore.QRect(110, 30, 47, 13))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setGeometry(QtCore.QRect(580, 30, 101, 16))
        self.label_16.setObjectName("label_16")
        self.lcdSudak = QtWidgets.QLCDNumber(self.tab_5)
        self.lcdSudak.setGeometry(QtCore.QRect(672, 491, 101, 23))
        self.lcdSudak.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdSudak.setDigitCount(10)
        self.lcdSudak.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdSudak.setObjectName("lcdSudak")
        self.label_17 = QtWidgets.QLabel(self.tab_5)
        self.label_17.setGeometry(QtCore.QRect(4, 280, 181, 16))
        self.label_17.setObjectName("label_17")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.tab_6)
        self.textBrowser_6.setGeometry(QtCore.QRect(3, 310, 771, 192))
        self.textBrowser_6.setStyleSheet("background-color: rgb(0, 67, 0);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.tableUgor = QtWidgets.QTableWidget(self.tab_6)
        self.tableUgor.setGeometry(QtCore.QRect(240, 80, 256, 192))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableUgor.setFont(font)
        self.tableUgor.setRowCount(5)
        self.tableUgor.setObjectName("tableUgor")
        self.tableUgor.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableUgor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableUgor.setHorizontalHeaderItem(1, item)
        self.tableUgor.horizontalHeader().setDefaultSectionSize(117)
        self.tableUgor.verticalHeader().setDefaultSectionSize(23)
        self.btnStartUgor = QtWidgets.QPushButton(self.tab_6)
        self.btnStartUgor.setGeometry(QtCore.QRect(10, 520, 75, 23))
        self.btnStartUgor.setStyleSheet("background-color: rgb(111, 111, 83);\n"
"color: #fff")
        self.btnStartUgor.setObjectName("btnStartUgor")
        self.btnStopUgor = QtWidgets.QPushButton(self.tab_6)
        self.btnStopUgor.setGeometry(QtCore.QRect(90, 520, 75, 23))
        self.btnStopUgor.setStyleSheet("background-color: rgb(111, 111, 83);\n"
"color: #fff")
        self.btnStopUgor.setObjectName("btnStopUgor")
        self.label_18 = QtWidgets.QLabel(self.tab_6)
        self.label_18.setGeometry(QtCore.QRect(5, 290, 121, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_6)
        self.label_19.setGeometry(QtCore.QRect(358, 60, 47, 13))
        self.label_19.setObjectName("label_19")
        self.lcdUgor = QtWidgets.QLCDNumber(self.tab_6)
        self.lcdUgor.setGeometry(QtCore.QRect(673, 501, 101, 23))
        self.lcdUgor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdUgor.setDigitCount(10)
        self.lcdUgor.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdUgor.setObjectName("lcdUgor")
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainForm)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Промысел Ладога"))
        self.label.setText(_translate("MainForm", "Лещ не менее 5 кг."))
        self.tableLesh.setSortingEnabled(False)
        item = self.tableLesh.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableLesh.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        self.startLesh.setText(_translate("MainForm", "Старт"))
        self.stopLesh.setText(_translate("MainForm", "Стоп"))
        item = self.tableGustera.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableGustera.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        item = self.tableBeloglazka.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableBeloglazka.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        self.label_2.setText(_translate("MainForm", "Общий лог вылова:"))
        self.label_3.setText(_translate("MainForm", "Густера не менее 300 гр."))
        self.label_4.setText(_translate("MainForm", "Белоглазка не менее 250 гр."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainForm", "Лещ"))
        self.btnStartRipus.setText(_translate("MainForm", "Старт"))
        self.btnStopRipus.setText(_translate("MainForm", "Стоп"))
        item = self.tableRipus.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableRipus.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        item = self.tableKorushka.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableKorushka.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        self.label_5.setText(_translate("MainForm", "Рипус"))
        self.label_6.setText(_translate("MainForm", "Корюшка"))
        self.label_10.setText(_translate("MainForm", "Общий лог вылова:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainForm", "Рипус"))
        self.btnStartSig.setText(_translate("MainForm", "Старт"))
        self.btnStopSig.setText(_translate("MainForm", "Стоп"))
        item = self.tableRybec.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableRybec.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        item = self.tableSig.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableSig.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        item = self.tableLudoga.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableLudoga.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        self.label_7.setText(_translate("MainForm", "Рыбец не менее 250 гр."))
        self.label_8.setText(_translate("MainForm", "Сиг не менее 3 кг."))
        self.label_9.setText(_translate("MainForm", "Лудога не менее 350 гр."))
        self.label_11.setText(_translate("MainForm", "Общий лог вылова:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainForm", "Сиг"))
        self.btnStartShuka.setText(_translate("MainForm", "Старт"))
        self.btnStopShuka.setText(_translate("MainForm", "Стоп"))
        item = self.tableShuka.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableShuka.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        item = self.tableBigShuka.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableBigShuka.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        self.label_12.setText(_translate("MainForm", "Щука"))
        self.label_13.setText(_translate("MainForm", "Глубинная щука"))
        self.label_14.setText(_translate("MainForm", "Общий лог вылова:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainForm", "Щука"))
        self.btnStartSudak.setText(_translate("MainForm", "Старт"))
        self.btnStopSudak.setText(_translate("MainForm", "Стоп"))
        item = self.tableSudak.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableSudak.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        item = self.tableBigSudak.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableBigSudak.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        self.label_15.setText(_translate("MainForm", "Судак"))
        self.label_16.setText(_translate("MainForm", "Глубинный судак"))
        self.label_17.setText(_translate("MainForm", "Общий лог вылова:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainForm", "Судак"))
        item = self.tableUgor.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Рыба"))
        item = self.tableUgor.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Вес"))
        self.btnStartUgor.setText(_translate("MainForm", "Старт"))
        self.btnStopUgor.setText(_translate("MainForm", "Стоп"))
        self.label_18.setText(_translate("MainForm", "Общий лог вылова:"))
        self.label_19.setText(_translate("MainForm", "Угорь"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainForm", "Угорь"))
