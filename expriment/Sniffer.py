# -*- coding: utf-8 -*-
"""
Editor : GH

This is a temporary script file.
"""

from scapy.all import *
import os
import time
import multiprocessing
from scapy.layers import http
import numpy as np
import matplotlib.pyplot as plt
import binascii
from PyQt5 import QtCore,QtGui,QtWidgets

class Sniffer(QtCore.QThread):
    def __init__(self) -> None:
        super().__init__()
        pass

    def getAdapterIfaces(self):
        c = []
        for i in repr(conf.route).split('\n')[1:]:
            tmp = i[50:94].rstrip()
            if len(tmp)>0:
                c.append(tmp)
        c = list(set(c))
        return c
    
    def run(self):
        pass


