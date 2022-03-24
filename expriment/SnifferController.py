# -*- coding: utf-8 -*-
"""
Editor : GH

This is a temporary script file.
"""
class SnifferController():
    def __init__(self,ui=None,sn=None):
        self.ui = ui
        self.sniffer = sn
    
    def setUi(self,ui):
        self.ui = ui

    def setSniffer(self,sniffer):
        self.sniffer = sniffer

    def loadAdapterIfaces(self):
        ifaces  = self.sniffer.getAdapterIfaces()
        self.ui.setAdapterIfaces(ifaces)
    
    def setConnection(self):
        self.ui.buttonStart.clicked.connect(self.Start)
        
        self.ui.buttonPause.clicked.connect(self.Stop)

        self.ui.buttonFilter.clicked.connect(self.Filter)
    
    def Start(self):
        print("this start")
    
    def Stop(self):
        print("this is stop")
    
    def Filter(self):
        print("this is filter")


