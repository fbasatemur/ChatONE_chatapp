# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:40:02 2020

@author: fbasatemur
"""

import socket 

class Client():
      
      def __init__(self, ip, port):
            self.connectionIP = ip
            self.connectionPORT = port
            
      def createSocket(self):
            self.socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                  
      def connect(self):
            self.socket1.connect((self.connectionIP, self.connectionPORT)) 
      
      def send(self, mssg):
            self.socket1.send(mssg.encode('utf-8'))
      
      def close(self): 
            self.socket1.close()
            
      def exceptionHandling(self, mssg):
            return "ERROR: " + str(mssg)
      
      