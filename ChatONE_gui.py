# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:23:37 2020

@author: fbasatemur
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import QTimer

from client_gui import Client, socket
from server_Thread import ServerThread


class Window(QWidget):
      
      def __init__(self):
            super().__init__()
            
            self.setGeometry(300, 300 ,560, 460)   # x, y, w, h
            self.setWindowTitle("Chat ONE")
            
            self.labelIp()      
            self.labelPort()      
            
            self.sendButton() 
            
            self.entryIp()      
            self.entryPort()    
            self.entryMssg()
            
            self.mssgSendShortcut()
            
            self.textEditor()
            
            self.buildButton()
            self.fontButton()       
            self.delButton()
            
            self.ipHost = "172.0.0.1"
            self.portHost = 1234
            self.portHostColor = "green"
            
            self.ipDest = "172.0.0.1"
            self.portDest = 2345
            self.portDestColor = "blue"
            
            self.labelHost()
            self.labelTarget()
            
            self.isClickedSave = False
            
            self.show()
            
      def labelHost(self):
            self.host_lbl = QLabel("HOST", self)
            self.host_lbl.move(50,30)
            
      def labelTarget(self):
            self.target_lbl = QLabel("DESTINATION", self)
            self.target_lbl.move(320,30)
            
      def labelIp(self):
            self.ipH_lbl = QLabel("IP ", self)
            self.ipH_lbl.move(50,50)
            
            self.ipD_lbl = QLabel("IP ", self)
            self.ipD_lbl.move(320,50)
            
      def labelPort(self):
            self.portH_lbl= QLabel("PORT ", self)
            self.portH_lbl.move(50,80)
            
            self.portD_lbl= QLabel("PORT ", self)
            self.portD_lbl.move(320,80)
            
      def textEditor(self):
            self.mssgLast_TextEditor = QTextEdit(self)
            self.mssgLast_TextEditor.move(50,150)
            self.mssgLast_TextEditor.resize(460, 200)
            
            
      def sendButton(self):
            self.send_Btn = QPushButton("SEND", self)
            self.send_Btn.resize(100,50)
            self.send_Btn.move(410,380)
            self.send_Btn.clicked.connect(self.sendButtonFunc)
            
      def mssgSendShortcut(self):
            self.sendShortcut = QShortcut(QKeySequence("Return"), self)        # Enter button
            self.sendShortcut.activated.connect(self.sendButtonFunc)
            
      
      def sendButtonFunc(self):
            
            try:
                  if self.isClickedSave:
                        self.client = Client(self.ipDest, self.portDest)
                        self.client.createSocket()
                        self.client.connect()
                        self.client.send(self.mssg_Entry.text())
                        self.insertMssgLastTextEditor(self.mssg_Entry.text() + "\n", str(self.portHost), self.portHostColor)
                        self.client.close()
                        
                        self.mssg_Entry.clear()
                        
            except socket.error as errorMssg:
                  self.showErrorMssg(self.client.exceptionHandling(errorMssg))
      
      def insertMssgLastTextEditor(self, insertMessage, identity, color):
            
            if insertMessage != "":
                  self.mssgLast_TextEditor.setTextColor(QColor(color))
                  self.mssgLast_TextEditor.insertPlainText(identity + ":")
                  self.mssgLast_TextEditor.setTextColor(QColor("black"))
                  self.mssgLast_TextEditor.insertPlainText(insertMessage)
            
            
      def delButton(self):
            self.del_Btn = QPushButton("DELETE", self)
            self.del_Btn.move(250,115)
            self.del_Btn.clicked.connect(self.delButtonFunc)
      
      def delButtonFunc(self):
            self.mssgLast_TextEditor.clear()
            
      def entryIp(self):
            self.ipH_Entry= QLineEdit(self)
            self.ipH_Entry.move(100,50)
            self.ipH_Entry.setText("127.0.0.1")
            
            self.ipD_Entry= QLineEdit(self)
            self.ipD_Entry.move(370,50)
            self.ipD_Entry.setText("127.0.0.1")
            
      def entryPort(self):
            self.portH_Entry = QLineEdit(self)
            self.portH_Entry.move(100,80)
            
            self.portD_Entry = QLineEdit(self)
            self.portD_Entry.move(370,80)
            
      def entryMssg(self):
            self.mssg_Entry = QLineEdit(self)
            self.mssg_Entry.move(50,380)
            self.mssg_Entry.resize(350,40)
      
      
      def fontButton(self):
            self.font_Btn = QPushButton("CHOSE FONT", self)
            self.font_Btn.move(150,115)
            self.font_Btn.clicked.connect(self.setFont)
            
            
      def setFont(self):
            font, ok = QFontDialog.getFont()
            
            if ok:
                  self.mssgLast_TextEditor.setFont(font)
                  self.mssg_Entry.setFont(font)
                  
      def buildButton(self):
            self.build_Btn = QPushButton("BUILD", self)
            self.build_Btn.move(50,115)
            self.build_Btn.clicked.connect(self.buildButtonFunc)
            
      def buildButtonFunc(self):            
            self.ipHost = str(self.ipH_Entry.text())
            self.ipDest = str(self.ipD_Entry.text())
            self.portHost = int(self.portH_Entry.text())
            self.portDest = int(self.portD_Entry.text())
            self.isClickedSave = True
            
            self.createServer()
            
            self.refreshInboxTimer = QTimer()
            self.refreshInboxTimer.timeout.connect(self.refreshInbox)
            self.refreshInboxTimer.start(500)
            
      def refreshInbox(self):
            self.insertMssgLastTextEditor(self.serverThread.byteMssgBuffer.decode("utf-8"), str(self.portDest), self.portDestColor)
            self.serverThread.byteMssgBuffer.clear()
      
      def createServer(self):
            self.serverThread = ServerThread(self.ipHost, self.portHost)
            self.serverThread.daemon = True
            self.serverThread.start()
            
            self.serverErrorTimer = QTimer()
            self.serverErrorTimer.timeout.connect(self.serverErrorControl)
            self.serverErrorTimer.start(500)
            
      def serverErrorControl(self):
            
            if self.serverThread.errorMssg != "":
                  self.showErrorMssg(self.serverThread.errorMssg)
                  self.serverErrorTimer.stop()
            
            elif self.serverThread.isBind != "":
                  self.insertMssgLastTextEditor(self.serverThread.isBind + "\n", str(self.portHost), self.portHostColor)
                  self.serverThread.isBind = ""
                  
                  
      def showErrorMssg(self, mssg):
            mssgBox = QMessageBox.warning(self, "Warning !", mssg)


            
      
      