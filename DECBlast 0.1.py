import sys
import os
import urllib.request
import time
import json
import socket
import requests
import ipaddress

from urllib.request import Request, urlopen

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from PyQt5.QtCore import pyqtSignal,QDate






class Ui_MainWindow(object):
    # ?   lineEdit_2: QLineEdit
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DECBlast 0.1")
        MainWindow.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 2421, 921))
        self.tabWidget.setMinimumSize(QtCore.QSize(801, 0))
        self.tabWidget.setStyleSheet("QPushButton:hover {\n"
                                     "  background-color:silver\n"
                                     "}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(30, 302, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 40, 441, 291))
        self.textEdit_2.setStyleSheet("background-color:black")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(36, 20, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 441, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 91, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.wh1 = QtWidgets.QLabel(self.tab)
        self.wh1.setGeometry(QtCore.QRect(270, 39, 181, 41))
        self.wh1.setStyleSheet("color:red;")
        self.wh1.setText("")
        self.wh1.setObjectName("wh1")
        self.wh2 = QtWidgets.QLabel(self.tab)
        self.wh2.setGeometry(QtCore.QRect(270, 70, 181, 31))
        self.wh2.setStyleSheet("color:red;")
        self.wh2.setText("")
        self.wh2.setObjectName("wh2")
        self.wh3 = QtWidgets.QLabel(self.tab)
        self.wh3.setGeometry(QtCore.QRect(270, 80, 181, 61))
        self.wh3.setStyleSheet("color:red;")
        self.wh3.setText("")
        self.wh3.setObjectName("wh3")
        self.wh4 = QtWidgets.QLabel(self.tab)
        self.wh4.setGeometry(QtCore.QRect(270, 110, 181, 51))
        self.wh4.setStyleSheet("color:red;")
        self.wh4.setText("")
        self.wh4.setObjectName("wh4")
        self.wh5 = QtWidgets.QLabel(self.tab)
        self.wh5.setGeometry(QtCore.QRect(270, 130, 181, 61))
        self.wh5.setStyleSheet("color:red;")
        self.wh5.setText("")
        self.wh5.setObjectName("wh5")
        self.wh6 = QtWidgets.QLabel(self.tab)
        self.wh6.setGeometry(QtCore.QRect(270, 160, 181, 51))
        self.wh6.setStyleSheet("color:red;")
        self.wh6.setText("")
        self.wh6.setObjectName("wh6")
        self.wh7 = QtWidgets.QLabel(self.tab)
        self.wh7.setGeometry(QtCore.QRect(270, 180, 421, 61))
        self.wh7.setStyleSheet("color:red;")
        self.wh7.setText("")
        self.wh7.setObjectName("wh7")
        self.wh8 = QtWidgets.QLabel(self.tab)
        self.wh8.setGeometry(QtCore.QRect(270, 250, 261, 81))
        self.wh8.setStyleSheet("color:red;")
        self.wh8.setText("")
        self.wh8.setObjectName("wh8")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(260, 350, 111, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(260, 330, 441, 21))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_5.setGeometry(QtCore.QRect(260, 40, 441, 291))
        self.textEdit_5.setStyleSheet("background-color:black;color:red;")
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 302, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(36, 22, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(260, 15, 431, 31))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 40, 91, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line_2 = QtWidgets.QFrame(self.tab_3)
        self.line_2.setGeometry(QtCore.QRect(260, 350, 111, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(260, 330, 60, 21))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(36, 20, 101, 20))
        self.label_3.setToolTipDuration(-7)
        self.label_3.setStyleSheet("color:black;")
        self.label_3.setObjectName("label_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_4.setGeometry(QtCore.QRect(260, 40, 441, 291))
        self.textEdit_4.setStyleSheet("background-color:black;color:red;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(260, 20, 441, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 302, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 40, 91, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setGeometry(QtCore.QRect(260, 350, 111, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(260, 325, 111, 31))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1321, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.textEdit_4.setReadOnly(True)
        self.textEdit_5.setReadOnly(True)
        self.textEdit_2.setReadOnly(True)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("DECBlast 0.1", "DECBlast 0.1"))
        self.pushButton.setText(_translate("MainWindow", "Punch!"))
        self.label.setText(_translate("MainWindow", "               IP"))
        self.label_2.setText(
            _translate("MainWindow", "                                                              Work place"))
        self.label_7.setText(_translate("MainWindow", "version 0.1b"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Whois Function"))
        self.pushButton_3.setText(_translate("MainWindow", "Punch!"))
        self.label_5.setText(_translate("MainWindow", "               IP"))
        self.label_6.setText(
            _translate("MainWindow", "                                                              Work place"))
        self.label_8.setText(_translate("MainWindow", "version 0.1b"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Port Scanner "))
        self.label_3.setText(_translate("MainWindow", "               IP"))
        self.label_4.setText(
            _translate("MainWindow", "                                                              Work place"))
        self.pushButton_2.setText(_translate("MainWindow", "Punch!"))
        self.label_9.setText(_translate("MainWindow", "version 0.1b"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Blacklists checkout "))


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit_2.setText('')
        self.pushButton_3.clicked.connect(self.onPunch)
        self.pushButton.clicked.connect(self.onWhois)
        self.pushButton_2.clicked.connect(self.onList)
    def onList(self):
        getIP = self.lineEdit_3.text()

        self.threadclass2 = ThreadClass2(getIP,self)
        self.threadclass2.start()
        self.threadclass2.MySignal.connect(self.msg_thread2)
        self.threadclass2.finished.connect(self.msg_thread_finished2)


    def onPunch(self):
        host = self.lineEdit_2.text()

        self.threadclass = ThreadClass(host, self)
        self.threadclass.start()
        self.threadclass.mySignal.connect(self.msg_thread)
        self.threadclass.finished.connect(self.msg_thread_finished)

    def msg_thread2(self,text):


        self.textEdit_4.append(text)

    def msg_thread_finished2(self):
        pass

    def msg_thread(self, text):
        self.textEdit_5.append(text)

    def msg_thread_finished(self):
        pass
    def onWhois(self):
        getIP = self.lineEdit.text()
        try:
            getIPcheck = ipaddress.ip_network(getIP)

            req = Request(
                'http://smart-ip.net/info-json?callback=' + getIP,
                headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            url = "https://ipinfo.io/" + getIP + "/json"
            url2 = "http://api.whois.vu/?q=" + getIP
            getInfo = urllib.request.urlopen(url)
            infoList = json.load(getInfo)
            getInfo1 = urllib.request.urlopen(url2)
            infoList1 = json.load(getInfo1)

            #            geIP1 = ("IP: ", infoList["ip"])                        # ---
            geIP1 = (f'IP: {infoList["ip"]}')
            geIP2 = (f'City: {infoList["city"]}')
            geIP3 = (f'Country: {infoList["country"]}')
            geIP4 = (f'Hostname: {infoList1["hostname"]}')
            geIP5 = (f'Timezone: {infoList["timezone"]}')
            geIP6 = (f'Location: {infoList["loc"]}')
           # geIP7 = (f'Google Map Link: https://www.google.com/maps/place/@{infoList["loc"]}')  # +++

            self.wh1.setText(geIP1)
            self.wh2.setText(geIP2)
            self.wh3.setText(geIP3)
            self.wh4.setText(geIP4)
            self.wh5.setText(geIP5)
            self.wh6.setText(geIP6)
           # self.wh7.setText(geIP7)

        except ValueError:
            self.wh1.setText('Error! --->>> Invalid IP!')


class ThreadClass(QtCore.QThread):
    #    upd = pyqtSignal(int)
    mySignal = pyqtSignal(str)


    #                      vvvv
    def __init__(self, host, parent=None):
        super(ThreadClass, self).__init__(parent)
        self.host = host  # +++

    def run(self):
        mas = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445,
               514, 515,
               993, 995]
        #        host = self.lineEdit_2.emit(int)

        try:
            ipaddress.ip_network(self.host)  # self.host
            for port in mas:
                s = socket.socket()
                s.settimeout(1)
                try:
                    s.connect((self.host, port))
                    #                    time.sleep(1.5)
                    self.msleep(1500)
                    per2 = (str(port) + '<b style="background-color: black; color: green;"> open! </b>')
                    #                    self.textEdit_5.emit(per2)
                    self.mySignal.emit(per2)
                #                    print(per2)
                except socket.error:
                    per3 = (str(port) + '<b style="background-color: black; color: red;"> locked ! </b>')
                    #                    self.textEdit_5.emit(per3)
                    self.mySignal.emit(per3)
        except ValueError:
            self.mySignal.emit(' Error! --->>> Invalid IP!')

class ThreadClass2(QtCore.QThread,QMessageBox):
    MySignal = pyqtSignal(str)

    def __init__(self, getIP, parent=None):
        super(ThreadClass2, self).__init__(parent)
        self.getIP = getIP

    def run(self):


        try:
            ipaddress.ip_network(self.getIP)

            url = 'http://www.ip-score.com/ajax_handler/get_bls'

            blacklist = [
                'access.redhawk.org', 'b.barracudacentral.org', 'bl.shlink.org', 'bl.spamcannibal.org',
                'bl.spamcop.net', 'bl.tiopan.com', 'blackholes.wirehub.net', 'blacklist.sci.kun.nl',
                'block.dnsbl.sorbs.net', 'blocked.hilli.dk', 'bogons.cymru.com', 'cart00ney.surriel.com',
                'cbl.abuseat.org', 'cblless.anti-spam.org.cn', 'dev.null.dk', 'dialup.blacklist.jippg.org',
                'dialups.mail-abuse.org', 'dialups.visi.com', 'dnsbl.abuse.ch', 'dnsbl.anticaptcha.net',
                'dnsbl.antispam.or.id', 'dnsbl.dronebl.org', 'dnsbl.justspam.org', 'dnsbl.kempt.net',
                'dnsbl.sorbs.net', 'dnsbl.tornevall.org', 'dnsbl-1.uceprotect.net', 'duinv.aupads.org',
                'dnsbl-2.uceprotect.net', 'dnsbl-3.uceprotect.net', 'dul.dnsbl.sorbs.net', 'dul.ru',
                'escalations.dnsbl.sorbs.net', 'hil.habeas.com', 'black.junkemailfilter.com',
                'http.dnsbl.sorbs.net', 'intruders.docs.uu.se', 'ips.backscatterer.org',
                'korea.services.net', 'l2.apews.org', 'mail-abuse.blacklist.jippg.org',
                'misc.dnsbl.sorbs.net', 'msgid.bl.gweep.ca', 'new.dnsbl.sorbs.net',
                'no-more-funn.moensted.dk', 'old.dnsbl.sorbs.net', 'opm.tornevall.org', 'pbl.spamhaus.org',
                'proxy.bl.gweep.ca', 'psbl.surriel.com', 'pss.spambusters.org.ar', 'rbl.schulte.org',
                'rbl.snark.net', 'recent.dnsbl.sorbs.net', 'relays.bl.gweep.ca', 'relays.bl.kundenserver.de',
                'relays.mail-abuse.org', 'relays.nether.net', 'rsbl.aupads.org', 'sbl.spamhaus.org',
                'smtp.dnsbl.sorbs.net', 'socks.dnsbl.sorbs.net', 'spam.dnsbl.sorbs.net', 'spam.olsentech.net',
                'spamguard.leadmon.net', 'spamsources.fabel.dk', 'tor.dnsbl.sectoor.de', 'ubl.unsubscore.com',
                'web.dnsbl.sorbs.net', 'xbl.spamhaus.org', 'zen.spamhaus.org', 'zombie.dnsbl.sorbs.net',
                'dnsbl.inps.de', 'dyn.shlink.org', 'rbl.megarbl.net', 'bl.mailspike.net']

            for server in blacklist:
                try:
                    data = {'ip': self.getIP, 'server': server}

                    response = requests.post(url, data=data, timeout=3)

                    if response.status_code != 200:
                        raise ValueError('Expected 200 OK')

                    data = response.json()

                    rating = data[data.keys()[0]]

                    if rating != "":
                        self.MySignal.emit( \
                            '<b style="background-color: black; color: green;"> LISTED </b>' + server)

                except:
                    self.MySignal.emit("NOT LISTED: " + server)



        except ValueError:

             self.MySignal.emit(' Error! --->>> Invalid IP!')


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    w = Window()
    w.show()
    sys.exit(app.exec_())