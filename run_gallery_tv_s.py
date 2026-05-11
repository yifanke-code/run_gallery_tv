# -*- coding: UTF-8 -*-
import sys,os
import json
import time
import vlc
import psutil
import subprocess

from multiprocessing import Process
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget, QGraphicsScene)
from PySide6.QtWidgets import QPushButton, QApplication, QWidget, QMainWindow, QListWidget,QAbstractItemView
from PySide6.QtCore import QTimer, QTime
from run_gallery_tv_s_ui import Ui_MainWindow
import tkinter as tk
from tkinter import filedialog


import pyperclip
import os.path as op
#import subprocess
from pathlib import Path
#import urllib.request
import shutil
import re
#from valbum import valbum as va

import string
import pandas as pd
import subprocess
import platform

        
        
class MainForm(QMainWindow,Ui_MainWindow):
    cur_dir_files=[]
    lw=[]
    vlist=["list0","list1","list2","list3","list4"]    

    def __init__(self):
        
        super(MainForm, self).__init__()
            
        self.setupUi(self)
        #self.timer=QTimer()
        #self.timer.timeout.connect(self.check_and_runvlc)
        self.timer=QTimer()
        self.timer.timeout.connect(self.check_and_runvlc)
        #self.timer.start(60000) #60 secs     

        self.timer2=QTimer()
        self.timer2.timeout.connect(self.close_vlc)   
        self.timer2.start(5000)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        #self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()
        self.setWindowTitle('Start...')
        '''self.listWidget.addItem('video1.mp4')
        self.listWidget.addItem('company.mp4')
        self.listWidget.addItem('quality.mp4')
        self.listWidget.insertItem(0,'kkk')
        i=self.listWidget.item(0)
        i.setCheckState(Qt.Checked)'''        
        
        self.myjson_fn=Path('d:/VIDEO/run_gallery_tv.json')
        self.myjson_data={'path':'.','list0':[],'list1':[],'list2':[],'list3':[],'list4':[],}
        if self.myjson_fn.exists():
            self.myjson_data=json.loads(self.myjson_fn.read_text())
            self.path=Path(self.myjson_data['path'])
        else:
            self.myjson_fn=Path('./run_gallery_tv.json')
            if self.myjson_fn.exists():
                self.myjson_data=json.loads(self.myjson_fn.read_text())
                self.path=Path(self.myjson_data['path'])            

        


        self.pushButton_play_1.clicked.connect(self.play_1) 
        self.pushButton_play_1.setStyleSheet("background-color:rgba(0,0,0,0);border: 0px;")

 
        self.pushButton_play_2.clicked.connect(self.play_2) 
        self.pushButton_play_2.setStyleSheet("background-color:rgba(0,0,0,0);border: 0px;")


        self.pushButton_play_3.clicked.connect(self.play_3) 
        self.pushButton_play_3.setStyleSheet("background-color:rgba(0,0,0,0);border: 0px;")


        self.pushButton_play_4.clicked.connect(self.play_4) 
        self.pushButton_play_4.setStyleSheet("background-color:rgba(0,0,0,0);border: 0px;")

        self.cmd='c:/program files/videolan/vlc/vlc.exe'
        self.media_player=vlc.MediaPlayer()
        #self.cmd='vlc.exe'

        
        fn=Path('D:/VIDEO/dimension.setting')
        fnl=Path('./dimension.setting')
        if fn.exists():
            s=fn.read_text().split(' ')
            sn=[int(f) for f in s]
        elif fnl.exists():
            s=fnl.read_text().split(' ')
            sn=[int(f) for f in s]            
        else:
            sn=[1918,1078,1920,1080]    

        self.graphicsView.setGeometry(0, 0, sn[2]          , sn[3])  #graphicsview在回字大口

                # setting status bar message
        self.statusBar().showMessage("This is status bar")

        # setting  border
        self.statusBar().setStyleSheet("border :3px solid black;")

        # setting tool tip for status bar
        self.statusBar().setToolTip("Hello ! from status bar")

        # setting visibility status to False
        self.statusBar().setVisible(False)

        scene = QGraphicsScene()      # 加入 QGraphicsScene
        scene.setSceneRect(0, 0, sn[0]     , sn[1])      # 設定 QGraphicsScene 位置與大小   scene在回字小口, 正中間
        if Path('D:/VIDEO/start_1.jpg').exists():
            img = QPixmap(Path('D:/VIDEO/start_1.jpg'))         # 加入圖片
        else:
            img = QPixmap(Path('./start_1.jpg'))
        scene.addPixmap(img)                    # 將圖片加入 scene

        self.graphicsView.setScene(scene)                  # 設定 QGraphicsView 的場景為 scene
        
        '''f=Path('d:/VIDEO/autoplay.on')
        if f.exists():
            self.duration=[int(i) for i in f.read_text().split('\n')]
            self.play_i(4,True)
        else:
            f=Path('./autoplay.on')
            if f.exists():
                self.duration=[int(i) for i in f.read_text().split('\n')]'''
            


    def keyPressEvent(self, event):
        key = event.key()
        
        if key == Qt.Key_1:            
            self.play_i(1,False)
        elif key == Qt.Key_2:
            self.play_i(2,False)
        elif key == Qt.Key_3:
            self.play_i(3,False)
        elif key == Qt.Key_4:
            self.play_i(4,False)
        elif key == Qt.Key_0 or key==Qt.Key_A:
            self.play_i(0,True)            
        elif key== Qt.Key_8:
            self.check_proc()
        elif key== Qt.Key_K:
            sys.exit(app.exec())            
        elif key== Qt.Key_9:
            os.environ["VLC_VERBOSE"] = str("-1")
            f1=('test.mkv')

            instance = vlc.Instance('--no-audio', '--fullscreen')
            player=instance.media_player_new()

            #f2='G:\\Movie\\X2-64 ERROR\\Flight.Photographers.2025.1080p.WEBRip.x264.AAC-[YTS.MX].mp4'
            m1=instance.media_new(f1)
            #m2=vlc.Media(f2)
            player.set_media(m1)
            #self.media_player.set_media(m2)
            player.play()

            playing = set([1,2,3,4])
            play = True
            while play:

                time.sleep(0.5)
                state = self.media_player.get_state()
                if state in playing:
                    continue
                else:
                    play = False
            try:
                self.media_player.stop()
            except:
                pass



    def play_1(self):
        self.play_i(1,False)


    def play_2(self):
        self.play_i(2,False)        


    def play_3(self):
        self.play_i(3,False)        
               
    def play_4(self):
        self.play_i(4,False)

    def play_0(self):
        self.play_i(0,True)        

    def check_proc(self):
        progs = str(subprocess.check_output('tasklist'))
        if 'vlc.exe' in progs:
            #print('with vlc')
            return True
        else:
            #print('no vlc')
            return False
        
    def check_and_runvlc(self):
        if not self.check_proc():
            self.play_0()
        #self.timer.start(60000)

    def close_vlc(self):
        self.timer2.start(5000)
        #self.count=self.count+1
        
        #print(self.count)
        if not self.check_proc() and not self.timer.isActive():
            self.timer.start(60000)
            #if self.play_list<4 and self.count>(self.duration[self.play_list-1]+2):
            #    os.system("taskkill /f /im  vlc.exe")

    def play_i(self,i,loop):
        self.play_list=i
        v_list=self.myjson_data[self.vlist[i]]
        if loop:
            op_loop="--loop"
        else:
            op_loop=""
        op_start_time="--start_time=0"
        op_play_and_exit="--play-and-exit"
        op_clear_queue="--global-key-clear-playlist='CTRL+W'"
        op_no_playlist="--no-playlist-enqueue"
        op1="--one-instance"
        op2="--playlist-enqueue"
        if self.check_proc():
            os.system("taskkill /f /im  vlc.exe")
        time.sleep(1)
        duration=0
        self.count=0
        if loop:
            p=subprocess.Popen([self.cmd,'--fullscreen',op1,op_loop,op_clear_queue])
            for f in v_list:
                p=subprocess.Popen([self.cmd,'--fullscreen',op1, op_loop, op2, self.path/f])        
        else:
            p=subprocess.Popen([self.cmd,'--fullscreen',op1,op_play_and_exit,op_clear_queue])
            for f in v_list:
                p=subprocess.Popen([self.cmd,'--fullscreen',op1, op_play_and_exit,op2, self.path/f])    
                #player=vlc.MediaPlayer()
                #media=vlc.Media(self.path/f)  
                #player.set_media(media) 
                #len=player.get_length()
                #duration=duration+len
            #time.sleep(self.duration[i-1]+2)
        
            

if __name__=="__main__":           
    app=QApplication(sys.argv)
    win=MainForm()



    win.show()
    sys.exit(app.exec())