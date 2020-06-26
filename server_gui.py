# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:08:32 2020

@author: fbasatemur
"""

import socket

"""
      AF_UNIX: UNIX domain protokolleri
      AF_INET: TCP ve UDP için IPv4 protokolleri
      AF_INET6: TCP ve UDP için IPv6 protokolleri
      
      SOCK_STREAM: TCP bağlantı tipi
      SOCK_DGRAM: UDP bağlantı tipi
"""

class Server():
      
      def __init__(self, ip, port):
            self.serverIP = ip        # localhost
            self.serverPORT = port
            self.maxClient = 5

      def createSocket(self):
            self.socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
      def bind(self):
            self.socket1.bind((self.serverIP, self.serverPORT))
            return "socket connected to port: " + str(self.serverPORT)
            
      def listen(self):
            self.socket1.listen(self.maxClient)
      
      def accept(self):
            self.connection, self.adr = self.socket1.accept()
            
      def recv(self, bufferSize):
            return self.connection.recv(bufferSize)            
      
      def setTimeOut(self, waitTime):
            self.socket1.settimeout(waitTime)
      
      def close(self):
            self.connection.close()
            
      def exceptionHandling(self, mssg):
            return "ERROR: " + str(mssg)
      
      
      
      
      
      
      
      