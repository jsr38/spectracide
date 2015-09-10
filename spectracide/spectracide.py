#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
SpectraCide Raman Spectrometer Client Software 

Please see http:/// for details

author: Jeremy Reeve
website: https:/// 
last edited: 
"""


from PyQt5.QtCore import Qt,QObject
from PyQt5.QtWidgets import QApplication,QMainWindow
from main_window_auto import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":

    import sys
    a = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    a.exec_()

