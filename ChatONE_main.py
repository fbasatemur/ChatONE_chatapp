# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:53:12 2020

@author: fbasatemur
"""



if __name__ == "__main__":
      
      import sys
      
      from ChatONE_gui import Window
      from PyQt5.QtWidgets import QApplication
      
      app = QApplication(sys.argv)
      
      window = Window()
      
      sys.exit(app.exec_())
            