# -*- coding: utf-8 -*-
"""
Editor : GH

This is a temporary script file.
"""
class SnifferController():
    def __init__(self):
        self.ui = None
        self.sniffer = None
    
    def setUi(self,ui):
        self.ui = ui

    def setSniffer(self,sniffer):
        self.sniffer = sniffer

    def loadAdapterIfaces(self):
        ifaces  = self.sniffer.getAdapterIfaces()
        self.ui.setAdapterIfaces(ifaces)

def ControllerRun():
    sc = SnifferController()
    return sc
