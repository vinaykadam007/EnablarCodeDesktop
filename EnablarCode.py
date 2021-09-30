from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os, platform
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from ecb.ecb import *
from eca.eca import *
from eci.eci import *
from os import path
import json
from datetime import date
import datetime
import server
from cryptography.fernet import Fernet
import requests
from PIL import Image
import urllib.request
# from fbs_runtime.application_context.PyQt5 import ApplicationContext

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

# test



def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

import pyautogui
width, height= pyautogui.size()
# print(width, height)



class MainApp(QDialog):

    def __init__(self):
        global labelwidget, buttonBluewidget, movie
        super().__init__()
    
        self.title = 'Enablar Code 3.4'
        # self.left = 10
        # self.top = 10
        # self.width = 320
        # self.height = 100
        self.obj = server.Worker()  
        self.thread = QThread() 
        # self.thread.quit() 
        self.obj.moveToThread(self.thread)
        self.obj.finished.connect(self.thread.quit)
        self.thread.started.connect(self.obj.run)
        self.thread.start()

        # sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        # print(" Screen size : "  + str(sizeObject.height()) + "x"  + str(sizeObject.width()))   


        size = width, height
        # print(size)
        im = Image.open("Splash.png")
        im_resized = im.resize(size, Image.ANTIALIAS)
        im_resized.save("Splash.png", "PNG")

        self.setStyleSheet("""
    QDialog {
        background-image: url("Splash.png"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
""")

        
        self.setWindowTitle(self.title)
        # self.setFixedHeight(768) 
        # self.setFixedWidth(1366) 
        self.setWindowFlags( Qt.WindowCloseButtonHint |  Qt.WindowMinimizeButtonHint)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        # icon_path = resource_path('enablAR.ico')#os.path.realpath("enablAR.ico") #Path(__file__).parent / "../icons/enablAR.ico"
        self.setWindowIcon(QIcon(str(resource_path('enablAR.ico'))))
        

        self.label = QLabel('''                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ''',self)
        
        self.label.setObjectName("label")
        labelwidget = self.label
        if width == 1920 and height == 1080:
            labelwidget.move(620, 300)
        elif width == 1366 and height == 768:
            labelwidget.move(450, 200)
        elif width == 1380 and height == 768:
            labelwidget.move(450, 200)
        elif width == 1280 and height == 960:
            labelwidget.move(450, 280)
        elif width == 1280 and height == 800:
            labelwidget.move(450, 220)
        elif width == 1280 and height == 768:
            labelwidget.move(450, 220)
        elif width == 1280 and height == 720:
            labelwidget.move(450, 160)
        elif width == 1024 and height == 768:
            labelwidget.move(360, 160)
        elif width == 1680 and height == 1050:
            labelwidget.move(520, 220)
        elif width == 1600 and height == 1200:
            labelwidget.move(520, 220)
        self.movie = QMovie(self)
        movie = self.movie

        self.buttonBlue = QPushButton('Basic',self)
        self.buttonBlue.installEventFilter(self)
        self.buttonBlue.clicked.connect(self.on_click_blocks)
        # self.buttonBlue.clicked.connect(self.colorchange)
        # self.buttonBlue.setFixedHeight(100)
        self.buttonBlue.setFixedWidth(260)
        # self.buttonBlue.setStyleSheet('QPushButton {  border-color: white; border-width: 0px; padding: 14px; border-style: outset; border-radius: 8px; background-color : blue; font-weight: regular; font-size: 10pt; font-family: Seoge UI; color: white; }')#setStyleSheet('QPushButton {  background-color : #92374d; color: white; }')
        # self.buttonBlue.setStyleSheet('QPushButton {  border-color: transparent; border-width: 0px; padding: 14px; border-style: outset; border-radius: 2px; background-color : transparent; font-weight: bold; font-size: 25pt; font-family: Seoge UI; color: white; }')
        
        self.buttonBlue.setStyleSheet('QPushButton {  border-color: black; border-width: 0px; padding: 14px; border-style: outset; border-radius: 20px; background-color : white; font-weight: regular; font-size: 22pt; font-family: Seoge UI; color: black; } QPushButton::hover {background-color: lightgreen;}')
        
        # self.buttonBlue.setToolTip('Basic mode')
        # buttonBlue.move(200, 590)
        if width == 1920 and height == 1080:
            # self.buttonBlue.move(240, 830)
            self.buttonBlue.move(100, 290)
        elif width == 1366 and height == 768:
            self.buttonBlue.move(50, 220)
            # self.buttonBlue.move(240, 350)
        elif width == 1360 and height == 768:
            self.buttonBlue.move(50, 220)
        elif width == 1280 and height == 960:
            self.buttonBlue.move(50, 310)
        elif width == 1280 and height == 800:
            self.buttonBlue.move(50, 270)
        elif width == 1280 and height == 768:
            self.buttonBlue.move(50, 270)
        elif width == 1280 and height == 720:
            self.buttonBlue.move(50, 240)
        elif width == 1024 and height == 768:
            self.buttonBlue.move(50, 200)
        elif width == 1680 and height == 1050:
            self.buttonBlue.move(100, 270)
        elif width == 1600 and height == 1200:
            self.buttonBlue.move(100, 270)
        # self.buttonBlue.setToolTipDuration(1000)
        self.buttonBlue.setCursor(QCursor(Qt.PointingHandCursor))
        buttonBluewidget = self.buttonBlue
        # layout.addWidget(buttonBlue,2,0)
       
        
        self.buttonRed = QPushButton('Intermediate', self)
        self.buttonRed.clicked.connect(self.on_click_designblocks)
        self.buttonRed.installEventFilter(self)
        # self.buttonRed.setFixedHeight(100)
        self.buttonRed.setFixedWidth(260)
        # buttonRed.setStyleSheet('QPushButton {  border-color: white; border-width: 0px; padding: 14px; border-style: outset; border-radius: 8px; background-color : red; font-weight: regular; font-size: 10pt; font-family: Seoge UI; color: white; }')#setStyleSheet('QPushButton {  background-color : #92374d; color: white; }')
        # self.buttonRed.setStyleSheet('QPushButton {  border-color: transparent; border-width: 0px; padding: 14px; border-style: outset; border-radius: 2px; background-color : transparent; font-weight: bold; font-size: 25pt; font-family: Seoge UI; color: white; }')
        self.buttonRed.setStyleSheet('QPushButton {  border-color: black; border-width: 0px; padding: 14px; border-style: outset; border-radius: 20px; background-color : white; font-weight: regular; font-size: 22pt; font-family: Seoge UI; color: black; } QPushButton::hover {background-color: lightgreen;}')
        # self.buttonRed.setToolTip('Intermediate mode')
        # self.buttonRed.move(540, 590)
        if width == 1920 and height == 1080:
            # self.buttonRed.move(780, 830)
            self.buttonRed.move(100, 550)
        elif width == 1366 and height == 768:
            self.buttonRed.move(50, 400)
        elif width == 1360 and height == 768:
            self.buttonRed.move(50, 400)
        elif width == 1280 and height == 960:
            self.buttonRed.move(50, 490)
        elif width == 1280 and height == 800:
            self.buttonRed.move(50, 450)
        elif width == 1280 and height == 768:
            self.buttonRed.move(50, 450)
        elif width == 1280 and height == 720:
            self.buttonRed.move(50, 400)
        elif width == 1024 and height == 768:
            self.buttonRed.move(50, 350)
        elif width == 1680 and height == 1050:
            self.buttonRed.move(100, 500)
        elif width == 1600 and height == 1200:
            self.buttonRed.move(100, 500)
        # self.buttonRed.setToolTipDuration(1000)
        self.buttonRed.setCursor(QCursor(Qt.PointingHandCursor))
        # layout.addWidget(buttonRed,2,1)
        
        self.buttonGreen = QPushButton('Advanced', self)
        self.buttonGreen.clicked.connect(self.on_designcode)
        self.buttonGreen.installEventFilter(self)
        self.buttonGreen.setFixedWidth(260)
        # self.buttonGreen.setFixedHeight(100)
        # buttonGreen.setStyleSheet('QPushButton {  border-color: white; border-width: 0px; padding: 14px; border-style: outset; border-radius: 8px; background-color : green; font-weight: regular; font-size: 10pt; font-family: Seoge UI; color: white; }')#setStyleSheet('QPushButton {  background-color : #92374d; color: white; }')
        # self.buttonGreen.setStyleSheet('QPushButton {  border-color: transparent; border-width: 0px; padding: 14px; border-style: outset; border-radius: 2px; background-color : transparent; font-weight: bold; font-size: 25pt; font-family: Seoge UI; color: white; }')
        self.buttonGreen.setStyleSheet('QPushButton {  border-color: black; border-width: 0px; padding: 14px; border-style: outset; border-radius: 20px; background-color : white; font-weight: regular; font-size: 22pt; font-family: Seoge UI; color: black; } QPushButton::hover {background-color: lightgreen;}')
        # self.buttonGreen.setToolTip('Advanced mode')
        # buttonGreen.move(980, 590)
        if width == 1920 and height == 1080:
            # self.buttonGreen.move(1450, 830)
            self.buttonGreen.move(100, 830)
        elif width == 1366 and height == 768:
            self.buttonGreen.move(50, 570)
        elif width == 1360 and height == 768:
            self.buttonGreen.move(50, 570)
        elif width == 1280 and height == 960:
            self.buttonGreen.move(50, 670)
        elif width == 1280 and height == 800:
            self.buttonGreen.move(50, 630)
        elif width == 1280 and height == 768:
            self.buttonGreen.move(50, 630)
        elif width == 1280 and height == 720:
            self.buttonGreen.move(50, 560)
        elif width == 1024 and height == 768:
            self.buttonGreen.move(50, 520)
        elif width == 1680 and height == 1050:
            self.buttonGreen.move(100, 740)
        elif width == 1600 and height == 1200:
            self.buttonGreen.move(100, 740)
        # self.buttonGreen.setToolTipDuration(1000)
        self.buttonGreen.setCursor(QCursor(Qt.PointingHandCursor))
        # layout.addWidget(buttonGreen,2,2)
        


        self.logout = QPushButton('Logout', self)
        self.logout.clicked.connect(self.on_logout)
        self.logout.installEventFilter(self)
        self.logout.setFixedWidth(120)
        self.logout.setFixedHeight(50)
        # self.logout.setFixedHeight(45)
        #  buttonGreen.setStyleSheet('QPushButton {  border-color: white; border-width: 0px; padding: 14px; border-style: outset; border-radius: 8px; background-color : green; font-weight: regular; font-size: 10pt; font-family: Seoge UI; color: white; }')#setStyleSheet('QPushButton {  background-color : #92374d; color: white; }')
        # self.buttonGreen.setStyleSheet('QPushButton {  border-color: transparent; border-width: 0px; padding: 14px; border-style: outset; border-radius: 2px; background-color : transparent; font-weight: bold; font-size: 25pt; font-family: Seoge UI; color: white; }')
        self.logout.setStyleSheet('QPushButton {  border-color: black; border-width: 0px; padding: 14px; border-style: outset; border-radius: 20px; background-color : white; font-weight: regular; font-size: 12pt; font-family: Seoge UI; color: black; } QPushButton::hover {background-color: #ffcccb;}')
        # self.buttonGreen.setToolTip('Advanced mode')
        # buttonGreen.move(980, 590)
        if width == 1920 and height == 1080:
            # self.buttonGreen.move(1450, 830)
            self.logout.move(1700, 50)
        elif width == 1366 and height == 768:
            self.logout.move(1200, 30)
        elif width == 1360 and height == 768:
            self.logout.move(1200, 30)
        elif width == 1280 and height == 960:
            self.logout.move(1100, 30)
        elif width == 1280 and height == 800:
            self.logout.move(1100, 30)
        elif width == 1280 and height == 768:
            self.logout.move(1100, 30)
        elif width == 1280 and height == 720:
            self.logout.move(1100, 30)
        elif width == 1024 and height == 768:
            self.logout.move(870, 30)
        elif width == 1680 and height == 1050:
            self.logout.move(1500, 100)
        elif width == 1600 and height == 1200:
            self.logout.move(1500, 100)
        # self.buttonGreen.setToolTipDuration(1000)
        self.logout.setCursor(QCursor(Qt.PointingHandCursor))

    
    @pyqtSlot()

    def on_logout(self):
        print("")
        try:
            os.remove(resource_path('reg.lic'))
        except:
            print('file not found')

        def _onlogin():
            global postreq
            # print('ee')
            # winpath = os.environ['WINDIR'] + "\\"
            # print(winpath)
    # inifile = open(winpath + filename)
            # print(platform.processor())
            
            hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
            hardwareid = hwid.split('-')
            finalid = "".join(hardwareid)
            # print(finalid)
            # idd = "BFEBFBFF000906EA2059"
            json1 = '''{"username":"'''+usertextbox.text()+'''","password":"'''+passtextbox.text()+'''","hw_id":"'''+finalid+'''"}'''
            # print(json1)
            with open(resource_path('login.txt'), 'w') as jsonfile:
                jsonfile.write(json1)

            json2 = json.loads(json1)
            postreq =  requests.post("http://173.82.227.236:8014/sign-in/", data = json2)
            # print(postreq.text)
            # print(postreq.status_code, postreq.reason)
            if postreq.status_code == 200:
                logindialog.reject()
                window.showMaximized()

                key = Fernet.generate_key()
                with open(resource_path('mykey.key'), 'wb') as mykey:
                    mykey.write(key)
                encoded = str(postreq.text).encode()

                f = Fernet(key)
                encrypted = f.encrypt(encoded)
                # print(encrypted)


                with open(resource_path('reg.lic'),'wb') as f:
                    f.write(encrypted)
            
            else:
                # print('else hai')
                if usertextbox.text() == "" or passtextbox.text() == "":
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText('''Please put your credentials''')
                    msgBox.setWindowTitle("Message")
                    msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
                    msgBox.setStandardButtons(QMessageBox.Ok)
                # msgBox.buttonClicked.connect(self.msgButtonClick)

                    returnValue = msgBox.exec_()
                else:
                    if postreq.status_code == 400:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Information)
                        msgBox.setText('''Username or password was incorrect''')
                        msgBox.setWindowTitle("Message")
                        msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
                        msgBox.setStandardButtons(QMessageBox.Ok)
                    # msgBox.buttonClicked.connect(self.msgButtonClick)

                        returnValue = msgBox.exec_()
                    else:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Information)
                        # print("******************************third expire*******************************")
                        msgBox.setText('''License expired
Email ID: contact@eduvance.in''')
                        msgBox.setWindowTitle("Message")
                        msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
                        msgBox.setStandardButtons(QMessageBox.Ok)
                    # msgBox.buttonClicked.connect(self.msgButtonClick)

                        returnValue = msgBox.exec_()
                        try:
                            os.remove(resource_path('reg.lic'))
                        except:
                            print('file not found')





        logindialog = QDialog()
        logindialog.setModal(True)
        logindialog.setFixedWidth(400)
        logindialog.setFixedHeight(400)
        logindialog.setWindowTitle("Login Credentials")
        icon_path = resource_path('enablAR.ico') #os.path.realpath("enablAR.ico") #Path(__file__).parent / "../icons/enablAR.ico"
        logindialog.setWindowIcon(QIcon(str(icon_path)))
        logindialog.setWindowFlags( Qt.WindowCloseButtonHint |  Qt.WindowMinimizeButtonHint)

        # logindialog.setStyleSheet("QDialog { background-color: white }")

        layout = QVBoxLayout()

        logobutton = QPushButton('', logindialog)
        # self.logobutton.clicked.connect(self.press)
        logobutton.setAutoFillBackground(True)
        logobutton.setIcon(QIcon(resource_path("enablAR.ico")));
        logobutton.setIconSize(QSize(200,100));
        # self.logobutton.setStyleSheet("background-image: url(" + resource_path('code/') + "/logo5.png);")
        logobutton.setStyleSheet("QPushButton { background-color : transparent; border:  none; }")


        usernamelabel = QLabel()
        usernamelabel.setText('Username')
        usernamelabel.setFont(QFont('Arial', 12))

        usertextbox = QLineEdit(logindialog, placeholderText="Enter Username")
        usertextbox.setStyleSheet("QLineEdit {background-color : white; border:  2; }")
        usertextbox.resize(80,50)
        f = usertextbox.font()
        f.setPointSize(11) # sets the size to 27
        usertextbox.setFont(f)

        passwordlabel = QLabel()
        passwordlabel.setText('Password')
        passwordlabel.setFont(QFont('Arial', 12))

        passtextbox = QLineEdit(logindialog, placeholderText="Enter Password")
        passtextbox.setStyleSheet("QLineEdit {background-color : white; border:  2; }")
        passtextbox.setEchoMode(QLineEdit.Password)
        passtextbox.resize(80,50)
        f = passtextbox.font()
        f.setPointSize(11) # sets the size to 27
        passtextbox.setFont(f)
        # passtextbox.setStyleSheet('lineedit-password-character: 9679')

        loginbutton = QPushButton('Login', logindialog)
        loginbutton.clicked.connect(_onlogin)
        loginbutton.setIconSize(QSize(100,100));
        loginbutton.setStyleSheet('QPushButton {  border-color: white; border-width: 0px; padding: 14px; border-style: outset; border-radius: 0px; background-color : #92374d; font-weight: regular; font-size: 10pt; font-family: Seoge UI; color: white; }')#setStyleSheet('QPushButton {  background-color : #92374d; color: white; }')
        loginbutton.setToolTip('Login')
        loginbutton.setToolTipDuration(1000)
        loginbutton.setCursor(QCursor(Qt.PointingHandCursor))



        layout.addWidget(logobutton)
        layout.addWidget(usernamelabel)
        layout.addWidget(usertextbox)
        layout.addWidget(passwordlabel)
        layout.addWidget(passtextbox)
        layout.addWidget(QWidget())
        layout.addWidget(loginbutton)
        logindialog.setLayout(layout)
        self.close()
        logindialog.show()


    def press(self):
        print('')

    # def colorchange(self):
    #     self.buttonBlue.setStyleSheet("QPushButton {background-color: green;}")

    def eventFilter(self, object, event):
        global labelwidget, buttonBluewidget, movie
    
        
        # movie.stop()
        
        if event.type() == QEvent.HoverMove:
            print()
            if object == self.buttonBlue:
                # print("xxxxx")
                movie.stop()
                # labelwidget.setStyleSheet("Qlabel{ background-color: transparent }")
                if width == 1920 and height == 1080:
                    self.movie.setFileName(resource_path("Basic.gif"))
                elif width == 1366 and height == 768:
                    self.movie.setFileName(resource_path("Basic1.gif"))
                elif width == 1360 and height == 768:
                    self.movie.setFileName(resource_path("Basic1.gif"))
                elif width == 1280 and height == 960:
                    self.movie.setFileName(resource_path("Basic2.gif"))
                elif width == 1280 and height == 800:
                    self.movie.setFileName(resource_path("Basic2.gif"))
                elif width == 1280 and height == 768:
                    self.movie.setFileName(resource_path("Basic2.gif"))
                elif width == 1280 and height == 720:
                    self.movie.setFileName(resource_path("Basic2.gif"))
                elif width == 1024 and height == 768:
                    self.movie.setFileName(resource_path("Basic3.gif"))
                elif width == 1680 and height == 1050:
                    self.movie.setFileName(resource_path("Basic.gif"))
                elif width == 1600 and height == 1200:
                    self.movie.setFileName(resource_path("Basic.gif"))
                labelwidget.setMovie(self.movie)
                
                movie.start()
                # buttonBluewidget.setStyleSheet("QPushButton::hover { border-color: black; border-width: 0px; padding: 14px; border-style: outset; border-radius: 20px;  font-weight: regular; font-size: 22pt; font-family: Seoge UI; color: black; background-color : white; }")
                return True
            elif object == self.buttonRed:
                # print("yyyyy")
                movie.stop()
                if width == 1920 and height == 1080:
                    self.movie.setFileName(resource_path("Intermediate.gif"))
                elif width == 1366 and height == 768:
                    self.movie.setFileName(resource_path("Intermediate1.gif"))
                elif width == 1360 and height == 768:
                    self.movie.setFileName(resource_path("Intermediate1.gif"))
                elif width == 1280 and height == 960:
                    self.movie.setFileName(resource_path("Intermediate2.gif"))
                elif width == 1280 and height == 800:
                    self.movie.setFileName(resource_path("Intermediate2.gif"))
                elif width == 1280 and height == 768:
                    self.movie.setFileName(resource_path("Intermediate2.gif"))
                elif width == 1280 and height == 720:
                    self.movie.setFileName(resource_path("Intermediate2.gif"))
                elif width == 1024 and height == 768:
                    self.movie.setFileName(resource_path("Intermediate3.gif"))
                elif width == 1680 and height == 1050:
                    self.movie.setFileName(resource_path("Intermediate.gif"))
                elif width == 1600 and height == 1200:
                    self.movie.setFileName(resource_path("Intermediate.gif"))

                labelwidget.setMovie(self.movie)
                
                movie.start()
                # buttonBluewidget.setStyleSheet("QPushButton::hover { border-color: black; border-width: 0px; padding: 14px; border-style: outset; border-radius: 20px;  font-weight: regular; font-size: 22pt; font-family: Seoge UI; color: black; background-color : white; }")
                return True
            elif object == self.buttonGreen:
                # print("zzzzz")
                movie.stop()
                if width == 1920 and height == 1080:
                    self.movie.setFileName(resource_path("Advanced.gif"))
                elif width == 1366 and height == 768:
                    self.movie.setFileName(resource_path("Advanced1.gif"))
                elif width == 1360 and height == 768:
                    self.movie.setFileName(resource_path("Advanced1.gif"))
                elif width == 1280 and height == 960:
                    self.movie.setFileName(resource_path("Advanced2.gif"))
                elif width == 1280 and height == 800:
                    self.movie.setFileName(resource_path("Advanced2.gif"))
                elif width == 1280 and height == 768:
                    self.movie.setFileName(resource_path("Advanced2.gif"))
                elif width == 1280 and height == 720:
                    self.movie.setFileName(resource_path("Advanced2.gif"))
                elif width == 1024 and height == 768:
                    self.movie.setFileName(resource_path("Advanced3.gif"))
                elif width == 1680 and height == 1050:
                    self.movie.setFileName(resource_path("Advanced.gif"))
                elif width == 1600 and height == 1200:
                    self.movie.setFileName(resource_path("Advanced.gif"))
                

                labelwidget.setMovie(self.movie)
                
                movie.start()
                # buttonBluewidget.setStyleSheet("QPushButton::hover { border-color: black; border-width: 0px; padding: 14px; border-style: outset; border-radius: 20px;  font-weight: regular; font-size: 22pt; font-family: Seoge UI; color: black; background-color : white; }")
                return True
            # else:
        # labelwidget.hide()  
        # self.movie.stop()
        # self.movie.destroyed()  
        
        return False


    def on_click_blocks(self):
        

        # print('click')
        
        from ecb.ecb import MainWindow
        # try:
        # appblock = QApplication(sys.argv)
        self.window = MainWindow()
        # self.ui = MainWindow()
        # self.ui.setup(self.window)
        
        self.close()
        self.window.showMaximized()
    


    def on_click_designblocks(self):
        # print('')
        from eci.eci import MainWindowbd 
        self.window = MainWindowbd()
        self.close()
        self.window.showMaximized()
        

    
    def on_designcode(self):
        # print('')
        from eca.eca import MainWindowsd
        self.window = MainWindowsd()
        self.close()
        self.window.showMaximized()
        


def login():
    global key, postreq, jsonog, f2
    # print("""*********************************************
    # ***********************************************""")
    print( 'connected' if connect() else 'no internet!')
    if connect():
        try:

            if os.path.isfile(resource_path('reg.lic')):
                # window.show()
                hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                hardwareid = hwid.split('-')
                finalid = "".join(hardwareid)
                # print(finalid)
                # idd = "BFEBFBFF000906EA2059"
                # json1 = '''{"username":"'''+usertextbox.text()+'''","password":"'''+passtextbox.text()+'''","hw_id":"'''+finalid+'''"}'''
                # print(json1)
                with open(resource_path('login.txt'),'r+') as loginfile:
                    json1 = loginfile.read()

                json2 = json.loads(json1)
                postreq =  requests.post("http://173.82.227.236:8014/sign-in/", data = json2)
                # print(postreq.text)
                # print(postreq.status_code, postreq.reason)
                if postreq.status_code == 200:
                    key = Fernet.generate_key()
                    with open(resource_path('mykey.key'), 'wb') as mykey:
                        mykey.write(key)
                    encoded = str(postreq.text).encode()

                    f = Fernet(key)
                    encrypted = f.encrypt(encoded)
                    # print(encrypted)


                    with open(resource_path('reg.lic'),'wb') as f:
                        f.write(encrypted)
                    
                    with open('mykey.key','rb') as f:
                        key = f.read()

                    with open(resource_path('reg.lic'),'rb') as file:
                        encrypted = file.read()
                        # print('encrypted', encrypted)
                    f = Fernet(key)
                    # print('f2', f)

                    jsonstr = f.decrypt(encrypted)

                    # print(jsonstr.decode())
                    jsonog = json.loads(jsonstr.decode())
                    # print(str(jsonog["expiry_date"]).split('-'))
                    expirylist = str(jsonog["expiry_date"]).split('-')
                    current_time = datetime.datetime.now()
                    thisyear = current_time.year
                    expirydate = datetime.datetime(int(expirylist[0]), int(expirylist[1]), int(expirylist[2]))
                    currentdate = datetime.datetime(int(current_time.year), int(current_time.month), int(current_time.day))
                    # print(type(thisyear))
                    # print(expirydate)
                    # print(currentdate)
                    if currentdate < expirydate:
                        window.showMaximized()
                    elif currentdate == expirydate:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Information)
                        # print("******************************same day expire warning*******************************")
                        msgBox.setText('''License expiring by tomorrow
Email ID: contact@eduvance.in''')
                        msgBox.setWindowTitle("Message")
                        msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        returnValue = msgBox.exec_()
                        window.showMaximized()
                    else:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Information)
                        # print("******************************first expire*******************************")
                        msgBox.setText('''License expired
            Email ID: contact@eduvance.in''')
                        msgBox.setWindowTitle("Message")
                        msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
                        msgBox.setStandardButtons(QMessageBox.Ok)
                    # msgBox.buttonClicked.connect(self.msgButtonClick)

                        returnValue = msgBox.exec_()
                        try:
                            os.remove(resource_path('reg.lic'))
                        except:
                            print('file not found')
                        # QApplication.quit()

                        def _onlogin():
                            global postreq
                            # print('ee')
                            # winpath = os.environ['WINDIR'] + "\\"
                            # print(winpath)
                    # inifile = open(winpath + filename)
                            # print(platform.processor())
                            
                            hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                            hardwareid = hwid.split('-')
                            finalid = "".join(hardwareid)
                            # print(finalid)
                            # idd = "BFEBFBFF000906EA2059"
                            json1 = '''{"username":"'''+usertextbox.text()+'''","password":"'''+passtextbox.text()+'''","hw_id":"'''+finalid+'''"}'''
                            # print(json1)
                            with open(resource_path('login.txt'), 'w') as jsonfile:
                                jsonfile.write(json1)

                            json2 = json.loads(json1)
                            postreq =  requests.post("http://173.82.227.236:8014/sign-in/", data = json2)
                            # print(postreq.text)
                            # print(postreq.status_code, postreq.reason)
                            if postreq.status_code == 200:
                                logindialog.reject()
                                window.showMaximized()

                                key = Fernet.generate_key()
                                with open(resource_path('mykey.key'), 'wb') as mykey:
                                    mykey.write(key)
                                encoded = str(postreq.text).encode()

                                f = Fernet(key)
                                encrypted = f.encrypt(encoded)
                                # print(encrypted)


                                with open(resource_path('reg.lic'),'wb') as f:
                                    f.write(encrypted)
                            
                            else:
                                print('else hai')
                                if usertextbox.text() == "" or passtextbox.text() == "":
                                    msgBox = QMessageBox()
                                    msgBox.setIcon(QMessageBox.Information)
                                    msgBox.setText('''Please put your credentials''')
                                    msgBox.setWindowTitle("Message")
                                    msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
                                    msgBox.setStandardButtons(QMessageBox.Ok)
                                # msgBox.buttonClicked.connect(self.msgButtonClick)

                                    returnValue = msgBox.exec_()
                                else:
                                    if postreq.status_code == 400:
                                        msgBox = QMessageBox()
                                        msgBox.setIcon(QMessageBox.Information)
                                        msgBox.setText('''Username or password was incorrect''')
                                        msgBox.setWindowTitle("Message")
                                        msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
                                        msgBox.setStandardButtons(QMessageBox.Ok)
                                    # msgBox.buttonClicked.connect(self.msgButtonClick)

                                        returnValue = msgBox.exec_()
                                    else:
                                        msgBox = QMessageBox()
                                        msgBox.setIcon(QMessageBox.Information)
                                        # print("******************************third expire*******************************")
                                        msgBox.setText('''License expired
    Email ID: contact@eduvance.in''')
                                        msgBox.setWindowTitle("Message")
                                        msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
                                        msgBox.setStandardButtons(QMessageBox.Ok)
                                    # msgBox.buttonClicked.connect(self.msgButtonClick)

                                        returnValue = msgBox.exec_()
                                        try:
                                            os.remove(resource_path('reg.lic'))
                                        except:
                                            print('file not found')
                            # logindialog.()
                            
                            # app.exec_()
                



                        
                        logindialog = QDialog()
                        logindialog.setModal(True)
                        logindialog.setFixedWidth(400)
                        logindialog.setFixedHeight(400)
                        logindialog.setWindowTitle("Login Credentials")
                        icon_path = resource_path('enablAR.ico') #os.path.realpath("enablAR.ico") #Path(__file__).parent / "../icons/enablAR.ico"
                        logindialog.setWindowIcon(QIcon(str(icon_path)))
                        logindialog.setWindowFlags( Qt.WindowCloseButtonHint |  Qt.WindowMinimizeButtonHint)

                        # logindialog.setStyleSheet("QDialog { background-color: white }")

                        layout = QVBoxLayout()

                        logobutton = QPushButton('', logindialog)
                        # self.logobutton.clicked.connect(self.press)
                        logobutton.setAutoFillBackground(True)
                        logobutton.setIcon(QIcon(resource_path("enablAR.ico")));
                        logobutton.setIconSize(QSize(200,100));
                        # self.logobutton.setStyleSheet("background-image: url(" + resource_path('code/') + "/logo5.png);")
                        logobutton.setStyleSheet("QPushButton { background-color : transparent; border:  none; }")


                        usernamelabel = QLabel()
                        usernamelabel.setText('Username')
                        usernamelabel.setFont(QFont('Arial', 12))

                        usertextbox = QLineEdit(logindialog, placeholderText="Enter Username")
                        usertextbox.setStyleSheet("QLineEdit {background-color : white; border:  2; }")
                        usertextbox.resize(80,50)
                        f = usertextbox.font()
                        f.setPointSize(11) # sets the size to 27
                        usertextbox.setFont(f)

                        passwordlabel = QLabel()
                        passwordlabel.setText('Password')
                        passwordlabel.setFont(QFont('Arial', 12))

                        passtextbox = QLineEdit(logindialog, placeholderText="Enter Password")
                        passtextbox.setStyleSheet("QLineEdit {background-color : white; border:  2; }")
                        passtextbox.setEchoMode(QLineEdit.Password)
                        passtextbox.resize(80,50)
                        f = passtextbox.font()
                        f.setPointSize(11) # sets the size to 27
                        passtextbox.setFont(f)
                        # passtextbox.setStyleSheet('lineedit-password-character: 9679')

                        loginbutton = QPushButton('Login', logindialog)
                        loginbutton.clicked.connect(_onlogin)
                        loginbutton.setIconSize(QSize(100,100));
                        loginbutton.setStyleSheet('QPushButton {  border-color: white; border-width: 0px; padding: 14px; border-style: outset; border-radius: 0px; background-color : #92374d; font-weight: regular; font-size: 10pt; font-family: Seoge UI; color: white; }')#setStyleSheet('QPushButton {  background-color : #92374d; color: white; }')
                        loginbutton.setToolTip('Login')
                        loginbutton.setToolTipDuration(1000)
                        loginbutton.setCursor(QCursor(Qt.PointingHandCursor))



                        layout.addWidget(logobutton)
                        layout.addWidget(usernamelabel)
                        layout.addWidget(usertextbox)
                        layout.addWidget(passwordlabel)
                        layout.addWidget(passtextbox)
                        layout.addWidget(QWidget())
                        layout.addWidget(loginbutton)
                        logindialog.setLayout(layout)
                        logindialog.show()
                else:
                
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    # print("******************************second expire*******************************")
                    msgBox.setText('''License is expired
Email ID: contact@eduvance.in''')
                    msgBox.setWindowTitle("Message")
                    msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
                    msgBox.setStandardButtons(QMessageBox.Ok)
                # msgBox.buttonClicked.connect(self.msgButtonClick)

                    returnValue = msgBox.exec_()
                    # os.remove(resource_path('reg.lic'))
                    try:
                        os.remove(resource_path('reg.lic'))
                    except:
                        print('file not found')
                    # QApplication.quit()
            else:
                def _onlogin():
                    global postreq
                    # print('ee')
                    # winpath = os.environ['WINDIR'] + "\\"
                    # print(winpath)
            # inifile = open(winpath + filename)
                    # print(platform.processor())
                    
                    hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                    hardwareid = hwid.split('-')
                    finalid = "".join(hardwareid)
                    # print(finalid)
                    # idd = "BFEBFBFF000906EA2059"
                    json1 = '''{"username":"'''+usertextbox.text()+'''","password":"'''+passtextbox.text()+'''","hw_id":"'''+finalid+'''"}'''
                    # print(json1)
                    with open(resource_path('login.txt'), 'w') as jsonfile:
                        jsonfile.write(json1)

                    json2 = json.loads(json1)
                    postreq =  requests.post("http://173.82.227.236:8014/sign-in/", data = json2)
                    # print(postreq.text)
                    # print(postreq.status_code, postreq.reason)
                    if postreq.status_code == 200:
                        logindialog.reject()
                        window.showMaximized()

                        key = Fernet.generate_key()
                        with open(resource_path('mykey.key'), 'wb') as mykey:
                            mykey.write(key)
                        encoded = str(postreq.text).encode()

                        f = Fernet(key)
                        encrypted = f.encrypt(encoded)
                        # print(encrypted)


                        with open(resource_path('reg.lic'),'wb') as f:
                            f.write(encrypted)

                    else:
                        # print('else hai')
                        if usertextbox.text() == "" or passtextbox.text() == "":
                            msgBox = QMessageBox()
                            msgBox.setIcon(QMessageBox.Information)
                            msgBox.setText('''Please put your credentials''')
                            msgBox.setWindowTitle("Message")
                            msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
                            msgBox.setStandardButtons(QMessageBox.Ok)
                        # msgBox.buttonClicked.connect(self.msgButtonClick)

                            returnValue = msgBox.exec_()
                        else:
                            if postreq.status_code == 400:
                                msgBox = QMessageBox()
                                msgBox.setIcon(QMessageBox.Information)
                                msgBox.setText('''Username or password was incorrect''')
                                msgBox.setWindowTitle("Message")
                                msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
                                msgBox.setStandardButtons(QMessageBox.Ok)
                            # msgBox.buttonClicked.connect(self.msgButtonClick)

                                returnValue = msgBox.exec_()
                            else:
                                msgBox = QMessageBox()
                                msgBox.setIcon(QMessageBox.Information)
                                # print("******************************third expire1*******************************")
                                msgBox.setText('''License expired
Email ID: contact@eduvance.in''')
                                msgBox.setWindowTitle("Message")
                                msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
                                msgBox.setStandardButtons(QMessageBox.Ok)
                            # msgBox.buttonClicked.connect(self.msgButtonClick)

                                returnValue = msgBox.exec_()
                                try:
                                    os.remove(resource_path('reg.lic'))
                                except:
                                    print('file not found')
            

                    
                logindialog = QDialog()
                logindialog.setModal(True)
                logindialog.setFixedWidth(400)
                logindialog.setFixedHeight(400)
                logindialog.setWindowTitle("Login Credentials")
                icon_path = resource_path('enablAR.ico') #os.path.realpath("enablAR.ico") #Path(__file__).parent / "../icons/enablAR.ico"
                logindialog.setWindowIcon(QIcon(str(icon_path)))
                logindialog.setWindowFlags( Qt.WindowCloseButtonHint |  Qt.WindowMinimizeButtonHint)

                # logindialog.setStyleSheet("QDialog { background-color: white }")

                layout = QVBoxLayout()

                logobutton = QPushButton('', logindialog)
                # self.logobutton.clicked.connect(self.press)
                logobutton.setAutoFillBackground(True)
                logobutton.setIcon(QIcon(resource_path("enablAR.ico")));
                logobutton.setIconSize(QSize(200,100));
                # self.logobutton.setStyleSheet("background-image: url(" + resource_path('code/') + "/logo5.png);")
                logobutton.setStyleSheet("QPushButton { background-color : transparent; border:  none; }")


                usernamelabel = QLabel()
                usernamelabel.setText('Username')
                usernamelabel.setFont(QFont('Arial', 12))

                usertextbox = QLineEdit(logindialog, placeholderText="Enter Username")
                usertextbox.setStyleSheet("QLineEdit {background-color : white; border:  2; }")
                usertextbox.resize(80,50)
                f = usertextbox.font()
                f.setPointSize(11) # sets the size to 27
                usertextbox.setFont(f)

                passwordlabel = QLabel()
                passwordlabel.setText('Password')
                passwordlabel.setFont(QFont('Arial', 12))

                passtextbox = QLineEdit(logindialog, placeholderText="Enter Password")
                passtextbox.setStyleSheet("QLineEdit {background-color : white; border:  2; }")
                passtextbox.setEchoMode(QLineEdit.Password)
                passtextbox.resize(80,50)
                f = passtextbox.font()
                f.setPointSize(11) # sets the size to 27
                passtextbox.setFont(f)
                # passtextbox.setStyleSheet('lineedit-password-character: 9679')

                loginbutton = QPushButton('Login', logindialog)
                loginbutton.clicked.connect(_onlogin)
                loginbutton.setIconSize(QSize(100,100));
                loginbutton.setStyleSheet('QPushButton {  border-color: white; border-width: 0px; padding: 14px; border-style: outset; border-radius: 0px; background-color : #92374d; font-weight: regular; font-size: 10pt; font-family: Seoge UI; color: white; }')#setStyleSheet('QPushButton {  background-color : #92374d; color: white; }')
                loginbutton.setToolTip('Login')
                loginbutton.setToolTipDuration(1000)
                loginbutton.setCursor(QCursor(Qt.PointingHandCursor))



                layout.addWidget(logobutton)
                layout.addWidget(usernamelabel)
                layout.addWidget(usertextbox)
                layout.addWidget(passwordlabel)
                layout.addWidget(passtextbox)
                layout.addWidget(QWidget())
                layout.addWidget(loginbutton)
                logindialog.setLayout(layout)
                logindialog.show()
        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText('''Sorry for the inconvenience, we will get back to you soon''')
            msgBox.setWindowTitle("Message")
            msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
            msgBox.setStandardButtons(QMessageBox.Ok)
        # # msgBox.buttonClicked.connect(self.msgButtonClick)

            returnValue = msgBox.exec_()
    else:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('''Please connect to the internet to proceed''')
        msgBox.setWindowTitle("Message")
        msgBox.setWindowIcon(QtGui.QIcon(resource_path("enablAR.ico")))
        msgBox.setStandardButtons(QMessageBox.Ok)
    # # msgBox.buttonClicked.connect(self.msgButtonClick)

        returnValue = msgBox.exec_()

    



if __name__ == '__main__':
    global window, postreq
    # print(browser_widget1)
    app = QApplication(sys.argv)
    # appctxt = ApplicationContext()
    # app.aboutToQuit.connect(self.closeEvent)
    window = MainApp()
    
    # if postreq.status_code == 200:

    # window.show()
    
    # window.hide()
    splash_path = os.path.realpath("enablAR.png")
    splash_pix = QPixmap(str(splash_path))
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    # splash.resize(600, 300)
    
    splash.show()
    k = 0
    for i in range(0,11):
        splash.setWindowOpacity(k)
        k = k + 0.1
        time.sleep(0.1)
    j = 1 
    for i in range(0,11):
        splash.setWindowOpacity(j)
        j = j - 0.1
        time.sleep(0.1)

    def login1(): 
        if splash.close():
            login()

            # window.showMaximized()

        else:
            app.quit()
    QTimer.singleShot(2000, login1)
    # app.exec_()
    # app = QApplication(sys.argv)
    # # app.aboutToQuit.connect(quitting) 
    # ex = MainApp()
    # # ex.closeEvent()
    
    
    sys.exit(app.exec_())