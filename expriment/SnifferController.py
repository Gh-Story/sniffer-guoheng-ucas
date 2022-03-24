# -*- coding: utf-8 -*-
"""
Editor : GH

This is a temporary script file.
"""
from PyQt5.QtWidgets import *
from Sniffer import *
import time
class SnifferController():
    def __init__(self,ui=None):
        self.ui = ui
        self.sniffer = None

    def getAdapterIfaces(self):
        c = []
        for i in repr(conf.route).split('\n')[1:]:
            tmp = i[50:94].rstrip()
            if len(tmp)>0:
                c.append(tmp)
        c = list(set(c))
        return c

    def loadAdapterIfaces(self):
        ifaces  = self.getAdapterIfaces()
        self.ui.setAdapterIfaces(ifaces)
    
    def setConnection(self):
        self.ui.buttonStart.clicked.connect(self.Start)
        
        self.ui.buttonPause.clicked.connect(self.Stop)

        self.ui.buttonFilter.clicked.connect(self.Filter)
    
    def Start(self):
        if self.sniffer is None:
            self.sniffer = Sniffer()
            self.setSniffer()
            self.sniffer.HandleSignal.connect(self.myCallBack)
            self.sniffer.start()
        elif self.sniffer.conditionFlag :
            self.setSniffer()
            self.sniffer.resume()

    def setSniffer(self):
        self.sniffer.filter = self.ui.filter
        self.sniffer.iface=self.ui.comboBoxIfaces.currentText()
    
    def myCallBack(self,packet):
        row = self.ui.tableWidget.rowCount()
        '''
        packetTime = '{:.7f}'.format(packet.time - self.ui.startTime)
        if IP in packet:
            src = packet[IP].src
            dst = packet[IP].dst
            print(src)
            print(dst)
        type = packet.type
        lens = str(len(packet))
        print(row)
        print(packetTime)
        print(type)
        print(lens)
        '''
        packet.show()
    
    def Stop(self):
        self.sniffer.pause()

    
    def Filter(self):
        print("this is filter")


