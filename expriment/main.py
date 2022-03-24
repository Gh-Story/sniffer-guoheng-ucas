# -*- coding: utf-8 -*-
"""
Editor : GH

"""
import imp
from SnifferGui import *
from SnifferController import *
from Sniffer import *
import sys
import os


if __name__ == "__main__":
    #vscode的python插件是直接绝对路径运行,所以加载icon会出问题，需要先chdir保证相对路径正确
    os.chdir(sys.path[0])
    app = QtWidgets.QApplication(sys.argv)
    ui = SnifferGui() #v
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sc = SnifferController(ui)#C

    sc.loadAdapterIfaces()
    sc.setConnection()

    sys.exit(app.exec_())
   