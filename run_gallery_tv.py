# -*- coding: UTF-8 -*-
import sys,os
import json
import time

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
    QWidget)
from PySide6.QtWidgets import QPushButton, QApplication, QWidget, QMainWindow, QListWidget,QAbstractItemView
from PySide6.QtCore import QTimer, QTime
from run_gallery_tv_ui_ui import Ui_MainWindow
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
        self.lw=[self.listWidget_1,self.listWidget_1,self.listWidget_2,self.listWidget_3,self.listWidget_4]
        
        self.setWindowTitle('Start...')
        '''self.listWidget.addItem('video1.mp4')
        self.listWidget.addItem('company.mp4')
        self.listWidget.addItem('quality.mp4')
        self.listWidget.insertItem(0,'kkk')
        i=self.listWidget.item(0)
        i.setCheckState(Qt.Checked)'''        
        
        self.myjson_fn=Path('./run_gallery_tv.json')
        self.myjson_data={'path':'.','list0':[],'list1':[],'list2':[],'list3':[],'list4':[],}
        if self.myjson_fn.exists():
            self.myjson_data=json.loads(self.myjson_fn.read_text())
            self.path=Path(self.myjson_data['path'])
            self.lw_display()
            self.lw_1_display()
            self.lw_2_display()
            self.lw_3_display()
            self.lw_4_display()
        

        self.pushButton.clicked.connect(self.filepath)

        self.pushButton_add_1.clicked.connect(self.add_1)    
        self.pushButton_del_1.clicked.connect(self.del_1)  
        self.pushButton_up_1.clicked.connect(self.up_1) 
        self.pushButton_dn_1.clicked.connect(self.dn_1) 
        self.pushButton_play_1.clicked.connect(self.play_1) 
        self.pushButton_play_1.setStyleSheet("background-color:rgba(0,0,0,0);border: 0px;");

        self.pushButton_add_2.clicked.connect(self.add_2)    
        self.pushButton_del_2.clicked.connect(self.del_2)  
        self.pushButton_up_2.clicked.connect(self.up_2) 
        self.pushButton_dn_2.clicked.connect(self.dn_2) 
        self.pushButton_play_2.clicked.connect(self.play_2) 

        self.pushButton_add_3.clicked.connect(self.add_3)    
        self.pushButton_del_3.clicked.connect(self.del_3)  
        self.pushButton_up_3.clicked.connect(self.up_3) 
        self.pushButton_dn_3.clicked.connect(self.dn_3) 
        self.pushButton_play_3.clicked.connect(self.play_3) 

        self.pushButton_add_4.clicked.connect(self.add_4)    
        self.pushButton_del_4.clicked.connect(self.del_4)  
        self.pushButton_up_4.clicked.connect(self.up_4) 
        self.pushButton_dn_4.clicked.connect(self.dn_4) 
        self.pushButton_play_4.clicked.connect(self.play_4) 

        self.cmd='c:/program files/videolan/vlc/vlc.exe'



    def lw_display(self):
        self.label.setText(str(self.path))
        f_list=[str(f.name) for f in self.path.glob('*.mp4')]
        self.listWidget.clear()
        self.listWidget.addItems(f_list)            
  

    def filepath(self):
        root = tk.Tk()
        root.withdraw()        
        file_path = filedialog.askdirectory()
        self.label.setText(file_path)
        self.path=Path(file_path)
        self.lw_display()
        
    def save_list(self):
        self.myjson_data['path']=str(self.path)
        all_list=[]
        for k in range(5):
            if k==0: continue
            n_list=[self.lw[k].item(i).text()  for i in range(self.lw[k].count()) ]
            all_list=all_list+n_list
            self.myjson_data[self.vlist[k]]=n_list
        self.myjson_data[self.vlist[0]]=all_list
        self.myjson_fn.write_text(json.dumps(self.myjson_data))

    def lw_1_display(self):
        self.lw_i_display(1)
    def add_1(self) :
        self.add_i(1)
    def del_1(self) :
        self.del_i(1)
    def up_1(self) :
        self.up_i(1)
    def dn_1(self) :
        self.dn_i(1)
    def play_1(self):
        self.play_i(1)

    def lw_2_display(self):
        self.lw_i_display(2)
    def add_2(self) :
        self.add_i(2)
    def del_2(self) :
        self.del_i(2)
    def up_2(self) :
        self.up_i(2)
    def dn_2(self) :
        self.dn_i(2)
    def play_2(self):
        self.play_i(2)        

    def lw_3_display(self):
        self.lw_i_display(3)
    def add_3(self) :
        self.add_i(3)
    def del_3(self) :
        self.del_i(3)
    def up_3(self) :
        self.up_i(3)
    def dn_3(self) :
        self.dn_i(3)
    def play_3(self):
        self.play_i(3)        

    def lw_4_display(self):
        self.lw_i_display(4)
    def add_4(self) :
        self.add_i(4)
    def del_4(self) :
        self.del_i(4)
    def up_4(self) :
        self.up_i(4)
    def dn_4(self) :
        self.dn_i(4)                
    def play_4(self):
        self.play_i(4)


    def lw_i_display(self,i):
        f_list=self.myjson_data[self.vlist[i]]
        self.lw[i].clear()
        self.lw[i].addItems(f_list) 
    def add_i(self,i) :
        item=self.listWidget.currentItem()
        if not item: return
        self.lw[i].addItem(item.text())
        self.save_list()
    def del_i(self,i) :
        item=self.lw[i].currentItem()
        if not item: return
        self.lw[i].takeItem(self.lw[i].row(item))
        self.save_list()
    def up_i(self,i) :
        item=self.lw[i].currentItem()
        if not item: return
        txt=item.text()
        row_i=self.lw[i].row(item)
        if row_i>0:
            self.lw[i].takeItem(self.lw[i].row(item))
            self.lw[i].insertItem(row_i-1,txt)   
            self.lw[i].setCurrentRow(row_i-1)  
        self.save_list()
    def dn_i(self,i) :
        item=self.lw[i].currentItem()
        if not item: return
        txt=item.text()
        row_i=self.lw[i].row(item)
        if row_i<self.lw[i].count()-1:
            self.lw[i].takeItem(self.lw[i].row(item))
            self.lw[i].insertItem(row_i+1,txt)   
            self.lw[i].setCurrentRow(row_i+1)                       
        self.save_list()

    def play_i(self,i):
        v_list=self.myjson_data[self.vlist[i]]
        op_loop="--loop"

        op_clear_queue="--global-key-clear-playlist='CTRL+W'"
        op_no_playlist="--no-playlist-enqueue"
        op1="--one-instance"
        op2="--playlist-enqueue"
        os.system("taskkill /f /im  vlc.exe")
        time.sleep(1)
        p=subprocess.Popen([self.cmd,'--width=640','--height=480',op1,op_loop,op_clear_queue])
        for f in v_list:
            p=subprocess.Popen([self.cmd,'--width=640','--height=480',op1, op_loop, op2, self.path/f])        

if __name__=="__main__":           
    app=QApplication(sys.argv)
    win=MainForm()
    win.show()
    sys.exit(app.exec())