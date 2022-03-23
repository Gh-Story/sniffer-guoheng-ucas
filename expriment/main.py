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
    ui = GuiRun()
    sn = SnifferRun()
    sc = ControllerRun()
    sc.setUi(ui)
    sc.setSniffer(sn)