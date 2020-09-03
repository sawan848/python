# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 20:23:45 2020

@author: ksawa
"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100,100,280,80)
window.move(60,15)
helloMsg=QLabel('<h1>Hello World</h1>',parent=window)
helloMsg.move(60,15)
window.show()
sys.exit(app.exec_())