# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:43:40 2020

@author: fbasatemur
"""

#import sys
#import time
from server_gui import Server
from threading import Thread, Event
import socket
from PyQt5.QtWidgets import QMessageBox

class ServerThread(Thread):
      
      def __init__(self, ip, host):
            super().__init__()
            self.running_event = Event()
            self.ipHost = ip
            self.portHost = host
            self.byteMssgBuffer = bytearray()
            self.errorMssg = ""
            # self.strMssgBuffer = ""
            
            self.isBind = ""
            self.isListen = ""
            
      def run(self):
            
            try:
                  self.serverLocal = Server(self.ipHost, self.portHost)
                  self.serverLocal.createSocket()
                  self.isBind = self.serverLocal.bind()
                  self.serverLocal.listen()
                  
                  while not self.running_event.isSet():
                        
                        self.serverLocal.accept()
                        
                        while True:
                              
                              self.connectedAddress = str(self.serverLocal.adr)
                              data = self.serverLocal.recv(1024)
                              
                              if not data:
                                    break
                              
                              
                              self.byteMssgBuffer.extend(data + b'\n')
                              # self.strMssgBuffer = self.byteMssgBuffer.decode("utf-8")
                              
                        self.serverLocal.close()
            
            except socket.error as errorMg:
                    self.errorMssg = self.serverLocal.exceptionHandling(errorMg)
      
      
      def stop_thread(self):
            self.running_event.set()


#serverThread = ServerThread("localhost", 1122)
#serverThread.daemon = True
#serverThread.start()
#
#time.sleep(10)
#
#serverThread.stop_thread()
#serverThread.join()
#sys.exit()