# -*- coding: utf-8 -*-
"""
Editor : GH

This is a temporary script file.
"""



from PyQt5.QtWidgets import *
from Sniffer import *
from SnifferGui import *
import time
from parsePacket import *
class SnifferController():
    def __init__(self,ui):
        self.ui = ui
        self.sniffer = None

    def getAdapterIfaces(self):
        c = []
        for i in repr(conf.route).split('\n')[1:]:
            #tmp = i[50:94].rstrip()
            tmp = re.search(r'[a-zA-Z](.*)[a-zA-Z0-9]',i).group()[0:44].rstrip()
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
        self.ui.tableWidget.itemClicked.connect(self.ui.showItemDetail)
        self.ui.buttonPostFilter.clicked.connect(self.PostFilter)
        self.ui.buttonTrace.clicked.connect(self.Trace)

    
    def Start(self):
        if self.sniffer is None:
            self.ui.startTime = time.time()
            self.sniffer = Sniffer()
            self.setSniffer()
            self.sniffer.HandleSignal.connect(self.myCallBack)
            self.sniffer.start()
            print('start sniffing')
        elif self.sniffer.conditionFlag :
            if self.ui.iface != self.ui.comboBoxIfaces.currentText()  or self.sniffer.filter != self.ui.filter :
                self.setSniffer()
                self.ui.clearTable()
            self.sniffer.resume()

    def setSniffer(self):
        self.sniffer.filter = self.ui.filter
        self.sniffer.iface=self.ui.comboBoxIfaces.currentText()
        self.ui.iface = self.ui.comboBoxIfaces.currentText()
    
    def myCallBack(self,packet):
        if self.ui.filter ==  'http' or self.ui.filter ==  'https':
            if packet.haslayer('TCP') ==False:
                return
            if packet[TCP].dport != 80 and packet[TCP].sport != 80 and packet[TCP].dport != 443 and packet[TCP].sport != 443:
                return                
        res = []
        myPacket = MyPacket()
        myPacket.parse(packet,self.ui.startTime)
        packetTime = myPacket.packTimne
        lens = myPacket.lens
        src = myPacket.layer_3['src']
        dst = myPacket.layer_3['dst']
        type = None
        info = None
        if myPacket.layer_1['name'] is not None:
            type = myPacket.layer_1['name']
            info = myPacket.layer_1['info']
        elif myPacket.layer_2['name'] is not None:
            type = myPacket.layer_2['name']
            info = myPacket.layer_2['info']
        elif myPacket.layer_3['name'] is not None:
            type = myPacket.layer_3['name']
            info = myPacket.layer_3['info']

        res.append(packetTime)
        res.append(src)
        res.append(dst)
        res.append(type)
        res.append(lens)
        res.append(info)
        res.append(myPacket)
        self.ui.setTableItems(res)

    def PostFilter(self):
        self.ui.postFilter()

    def Trace(self):
        pass
    
    def Stop(self):
        self.sniffer.pause()

    def Filter(self):
        self.ui.buildFilter()
    
    




'''
    def myCallBack(self,packet):
        res = []
        packetTime = '{:.7f}'.format(time.time() - self.ui.startTime)
        type = None
        src = None
        dst = None
        lens = str(len(packet))
        info = None

        if packet.type == 0x800 or packet.type == 0x2: # IPV4
            src = packet[IP].src
            dst = packet[IP].dst
            #TCP
            if packet[IP].proto == 6:
                #HTTP
                if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                    type = 'HTTP'  
                    if packet.haslayer('HTTPRequest'):
                        info = ('%s %s %s' % (packet.sprintf("{HTTPRequest:%HTTPRequest.Method%}").strip("'"),packet.sprintf("{HTTPRequest:%HTTPRequest.Path%}").strip("'"),packet.sprintf("{HTTPRequest:%HTTPRequest.Http-Version%}").strip("'")))
                    elif packet.haslayer('HTTPResponse'):
                        info = ('%s' % packet.sprintf("{HTTPResponse:%HTTPResponse.Status-Line%}").strip("'"))
                    
                elif  packet[TCP].dport == 443 or packet[TCP].sport == 443:
                    type = 'HTTPS'
                    info = ('%s -> %s Seq：%s Ack：%s Win：%s' % (packet[TCP].sport,packet[TCP].dport,packet[TCP].seq,packet[TCP].ack,packet[TCP].window))
                else:
                    type = 'TCP'
                    info = ('%s -> %s Seq：%s Ack：%s Win：%s' % (packet[TCP].sport,packet[TCP].dport,packet[TCP].seq,packet[TCP].ack,packet[TCP].window))  
            #UDP
            elif packet[IP].proto == 17:
                type = 'UDP' 
                info = ('%s -> %s 长度(len)：%s' % (packet[UDP].sport,packet[UDP].dport,packet[UDP].len))
            #ICMP
            elif packet[IP].proto == 1:
                type = 'ICMP'
                if packet[ICMP].type == 8:
                    info = ('Echo (ping) request id：%s seq：%s' % (packet[ICMP].id,packet[ICMP].seq))
                elif packet[ICMP].type == 0:
                    info = ('Echo (ping) reply id：%s seq：%s' % (packet[ICMP].id,packet[ICMP].seq))
                else:
                    info = ('type：%s id：%s seq：%s' % (packet[ICMP].type,packet[ICMP].id,packet[ICMP].seq))
            #IGMP
            elif packet[IP].proto == 2:
                type = 'IGMP'
            #其他协议
            else:
                type = str(packet[IP].proto)
        elif packet.type == 0x86dd: #IPV6
            src = packet[IPv6].src
            dst = packet[IPv6].dst
            #TCP
            if packet[IPv6].nh == 6:
                #HTTP
                if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                    type = 'HTTP' 
                    if packet.haslayer('HTTPRequest'):
                        info = ('%s %s %s' % (packet.sprintf("{HTTPRequest:%HTTPRequest.Method%}").strip("'"),packet.sprintf("{HTTPRequest:%HTTPRequest.Path%}").strip("'"),packet.sprintf("{HTTPRequest:%HTTPRequest.Http-Version%}").strip("'")))
                    elif packet.haslayer('HTTPResponse'):
                        info = ('%s' % packet.sprintf("{HTTPResponse:%HTTPResponse.Status-Line%}").strip("'"))
                elif  packet[TCP].dport == 443 or packet[TCP].sport == 443:
                    type = 'HTTPS'
                    info = ('%s -> %s Seq：%s Ack：%s Win：%s' % (packet[TCP].sport,packet[TCP].dport,packet[TCP].seq,packet[TCP].ack,packet[TCP].window))
                else:
                    type = 'TCP'  
                    info = ('%s -> %s Seq：%s Ack：%s Win：%s' % (packet[TCP].sport,packet[TCP].dport,packet[TCP].seq,packet[TCP].ack,packet[TCP].window))   
                #UDP
            elif packet[IPv6].nh == 17:
                type = 'UDP' 
                info = ('%s -> %s 长度(len)：%s' % (packet[UDP].sport,packet[UDP].dport,packet[UDP].len))
                #ICMP
            elif packet[IPv6].nh == 1:
                type = 'ICMP'
                if packet[ICMP].type == 8:
                    info = ('Echo (ping) request id：%s seq：%s' % (packet[ICMP].id,packet[ICMP].seq))
                elif packet[ICMP].type == 0:
                    info = ('Echo (ping) reply id：%s seq：%s' % (packet[ICMP].id,packet[ICMP].seq))
                else:
                    info = ('type：%s id：%s seq：%s' % (packet[ICMP].type,packet[ICMP].id,packet[ICMP].seq))
                #IGMP
            elif packet[IPv6].nh == 2:
                type = 'IGMP'
            #其他协议
            else:
                type = str(packet[IPv6].nh)
        elif packet.type == 0x806 : #ARP
            src = packet[ARP].psrc
            dst = packet[ARP].pdst
            if packet[ARP].op == 1:  #request
                info = ('Who has %s? Tell %s' % (packet[ARP].pdst,packet[ARP].psrc))
            elif packet[ARP].op == 2:  #reply
                info = ('%s is at %s' % (packet[ARP].psrc,packet[ARP].hwsrc))
            type = 'ARP'
        else:
            return
       
        res.append(packetTime)
        res.append(src)
        res.append(dst)
        res.append(type)
        res.append(lens)
        res.append(info)
        res.append(packet)
        self.ui.setTableItems(res)
        '''
