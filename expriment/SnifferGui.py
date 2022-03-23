# -*- coding: utf-8 -*-
"""
Editor : GH

"""
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

class SnifferGui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1244, 890)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        #central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #顶部栏 状态栏 菜单栏
        self.gridLayoutBar = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayoutBar.setObjectName("gridLayoutBar")
        #主显示
        self.gridLayoutMainShow = QtWidgets.QGridLayout()
        self.gridLayoutMainShow.setObjectName("gridLayoutMainShow")
        #下面部份
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.textBrowserTmp = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.textBrowserTmp.sizePolicy().hasHeightForWidth())
        self.textBrowserTmp.setSizePolicy(sizePolicy)
        self.textBrowserTmp.setObjectName("textBrowserTmp")
        self.horizontalLayout.addWidget(self.textBrowserTmp)

        self.textBrowserShow = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.textBrowserShow.sizePolicy().hasHeightForWidth())
        self.textBrowserShow.setSizePolicy(sizePolicy)
        self.textBrowserShow.setObjectName("textBrowserShow")
        self.horizontalLayout.addWidget(self.textBrowserShow)

        self.gridLayoutMainShow.addLayout(self.horizontalLayout, 2, 0, 1, 1)#rowIndex,colIndex,rowWidth,colWidth

        #中间部分
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "root")
        self.gridLayoutMainShow.addWidget(self.treeWidget, 1, 0, 1, 1)


        #上面部分
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayoutMainShow.addWidget(self.tableWidget, 0, 0, 1, 1)

        #顶部工具栏 菜单栏 状态栏
        self.gridLayoutBar.addLayout(self.gridLayoutMainShow, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        '''
        菜单栏暂时不做，因为只做一部分功能，作为功能栏就行了。当功能达到一定规模就可以分类形成菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1244, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        '''
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolbar = QtWidgets.QToolBar(MainWindow)
        self.toolbar.setObjectName("toolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.toolbar.addSeparator()

        self.comboBoxIface = QComboBox()
        self.toolbar.addWidget(self.comboBoxIface)
        self.toolbar.addSeparator()

        
        self.buttonStart = QtWidgets.QPushButton()
        self.buttonStart.setIcon(QIcon("./static/start.png"))
        self.buttonStart.setStyleSheet("background:rgba(0,0,0,0);border:1px solid rgba(0,0,0,0);border-radius:5px;")
        self.buttonStart.setToolTip("开始捕获")
        self.toolbar.addWidget(self.buttonStart)
        self.toolbar.addSeparator()

        self.buttonPause = QtWidgets.QPushButton()
        self.buttonPause.setIcon(QIcon("./static/pause.png"))
        self.buttonPause.setStyleSheet("background:rgba(0,0,0,0);border:1px solid rgba(0,0,0,0);border-radius:5px;")
        self.buttonPause.setToolTip("暂停捕获")
        self.toolbar.addWidget(self.buttonPause)
        self.toolbar.addSeparator()

        self.buttonFilter = QtWidgets.QPushButton()
        self.buttonFilter.setIcon(QIcon("./static/filter.png"))
        self.buttonFilter.setStyleSheet("background:rgba(0,0,0,0);border:1px solid rgba(0,0,0,0);border-radius:5px;")
        self.buttonFilter.setToolTip("过滤筛选")
        self.toolbar.addWidget(self.buttonFilter)
        self.toolbar.addSeparator()

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SnifferGui"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "时间"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "源地址"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "目的地址"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "协议"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "长度"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "信息"))
        self.toolbar.setWindowTitle(_translate("MainWindow", "工具栏"))
        #self.buttonStart.setText(_translate("MainWindow", "开始"))

        self.tableWidget.horizontalHeader().setSectionsClickable(False) #可以禁止点击表头的列
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows) #设置 不可选择单个单元格，只可选择一行。
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) #设置表格不可更改
        self.tableWidget.verticalHeader().setVisible(False) #去掉垂直表头
        self.tableWidget.setColumnWidth(0,60)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,60)
        self.tableWidget.setColumnWidth(5,60)
        self.tableWidget.setColumnWidth(6,600)

        self.treeWidget.setHeaderHidden(True) #去掉表头
        self.treeWidget.setColumnCount(1)

def GuiRun():
    os.chdir(sys.path[0])
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SnifferGui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    return ui

