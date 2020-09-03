# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:59:19 2020

@author: ksawa
"""
import sys
from PyQt5.QtWidgets import QDialog,QApplication



app=QApplication(sys.argv)
dialog=QDialog()
dialog.show()
sys.exit(app.exec_())