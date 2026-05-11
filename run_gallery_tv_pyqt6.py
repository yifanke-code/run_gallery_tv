# -*- coding: UTF-8 -*-
import sys
import os
import json
import time
import subprocess
from pathlib import Path

from PyQt6.QtCore import Qt, QSize, QRect
from PyQt6.QtGui import QFont, QIcon, QColor, QPalette
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QGridLayout, QListWidget, QPushButton, QLabel, QFileDialog,
    QFrame, QSplitter, QAbstractItemView, QStyle
)

# Dark Theme QSS
DARK_THEME = """
QMainWindow {
    background-color: #121212;
}

QWidget {
    background-color: #121212;
    color: #E0E0E0;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 13px;
}

QFrame#PlaylistCard {
    background-color: #1E1E1E;
    border-radius: 8px;
    border: 1px solid #333333;
}

QFrame#PlaylistCard:hover {
    border: 1px solid #3A8DFF;
}

QLabel#CardTitle {
    font-weight: bold;
    font-size: 15px;
    color: #3A8DFF;
    padding: 5px;
}

QListWidget {
    background-color: #252525;
    border: none;
    border-radius: 4px;
    padding: 5px;
    outline: none;
}

QListWidget::item {
    padding: 8px;
    border-radius: 4px;
}

QListWidget::item:selected {
    background-color: #3A8DFF;
    color: white;
}

QListWidget::item:hover {
    background-color: #333333;
}

QPushButton {
    background-color: #333333;
    border: none;
    padding: 8px 15px;
    border-radius: 4px;
    font-weight: 500;
}

QPushButton:hover {
    background-color: #444444;
}

QPushButton:pressed {
    background-color: #555555;
}

QPushButton#PrimaryButton {
    background-color: #3A8DFF;
    color: white;
}

QPushButton#PrimaryButton:hover {
    background-color: #4A9DFF;
}

QPushButton#PlayButton {
    background-color: #2E7D32;
    color: white;
    font-weight: bold;
}

QPushButton#PlayButton:hover {
    background-color: #388E3C;
}

QPushButton#ToolButton {
    padding: 5px;
    min-width: 30px;
}

QLabel#PathLabel {
    background-color: #1E1E1E;
    padding: 10px;
    border-radius: 4px;
    color: #BBBBBB;
    font-style: italic;
}
"""

class PlaylistCard(QFrame):
    def __init__(self, title, index, parent_form):
        super().__init__()
        self.setObjectName("PlaylistCard")
        self.index = index
        self.parent_form = parent_form
        
        layout = QVBoxLayout(self)
        
        # Header
        header = QHBoxLayout()
        self.title_label = QLabel(title)
        self.title_label.setObjectName("CardTitle")
        header.addWidget(self.title_label)
        header.addStretch()
        layout.addLayout(header)
        
        # List and Controls
        body = QHBoxLayout()
        self.list_widget = QListWidget()
        body.addWidget(self.list_widget)
        
        controls = QVBoxLayout()
        self.btn_up = QPushButton("↑")
        self.btn_up.setObjectName("ToolButton")
        self.btn_up.clicked.connect(lambda: parent_form.up_i(index))
        
        self.btn_dn = QPushButton("↓")
        self.btn_dn.setObjectName("ToolButton")
        self.btn_dn.clicked.connect(lambda: parent_form.dn_i(index))
        
        self.btn_del = QPushButton("×")
        self.btn_del.setObjectName("ToolButton")
        self.btn_del.setStyleSheet("color: #FF5252;")
        self.btn_del.clicked.connect(lambda: parent_form.del_i(index))
        
        controls.addWidget(self.btn_up)
        controls.addWidget(self.btn_dn)
        controls.addStretch()
        controls.addWidget(self.btn_del)
        body.addLayout(controls)
        
        layout.addLayout(body)
        
        # Footer Play Button
        self.btn_play = QPushButton("PLAY")
        self.btn_play.setObjectName("PlayButton")
        self.btn_play.clicked.connect(lambda: parent_form.play_i(index))
        layout.addWidget(self.btn_play)

class MainForm(QMainWindow):
    vlist = ["list0", "list1", "list2", "list3", "list4"]
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Run Gallery TV - Manager")
        self.resize(1100, 800)
        self.setStyleSheet(DARK_THEME)
        
        self.cmd = 'c:/program files/videolan/vlc/vlc.exe'
        self.myjson_fn = Path('./run_gallery_tv.json')
        self.myjson_data = {'path': '.', 'list0': [], 'list1': [], 'list2': [], 'list3': [], 'list4': []}
        
        self.init_ui()
        self.load_settings()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Top Bar: Path and Browse
        top_bar = QHBoxLayout()
        self.label_path = QLabel("Select a directory...")
        self.label_path.setObjectName("PathLabel")
        top_bar.addWidget(self.label_path, 1)
        
        self.btn_browse = QPushButton("Browse Folder")
        self.btn_browse.setObjectName("PrimaryButton")
        self.btn_browse.clicked.connect(self.filepath)
        top_bar.addWidget(self.btn_browse)
        main_layout.addLayout(top_bar)
        
        # Splitter for Library and Playlists
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Library Section
        library_widget = QWidget()
        library_layout = QVBoxLayout(library_widget)
        library_layout.setContentsMargins(0, 0, 0, 0)
        
        lib_title = QLabel("VIDEO LIBRARY")
        lib_title.setStyleSheet("font-weight: bold; color: #888; margin-bottom: 5px;")
        library_layout.addWidget(lib_title)
        
        self.listWidget = QListWidget()
        library_layout.addWidget(self.listWidget)
        
        self.splitter.addWidget(library_widget)
        
        # Playlists Grid Section
        playlists_widget = QWidget()
        self.grid_layout = QGridLayout(playlists_widget)
        self.grid_layout.setContentsMargins(10, 0, 0, 0)
        
        self.cards = []
        titles = ["Customer", "Vendor", "General", "Partner"]
        for i, title in enumerate(titles, 1):
            card = PlaylistCard(title, i, self)
            self.cards.append(card)
            self.grid_layout.addWidget(card, (i-1)//2, (i-1)%2)
            
        # Hook up the list widgets to the lw array for the logic
        # Note: lw[0] is unused in original add/del logic but used for saving
        self.lw = [None, self.cards[0].list_widget, self.cards[1].list_widget, 
                   self.cards[2].list_widget, self.cards[3].list_widget]
        
        self.splitter.addWidget(playlists_widget)
        self.splitter.setStretchFactor(1, 3)
        main_layout.addWidget(self.splitter)
        
        # Add to Playlist Button (Floating or Center)
        add_hint = QLabel("Select video on left, then click 'Add' on target card")
        add_hint.setStyleSheet("color: #666; font-size: 11px; padding: 5px;")
        main_layout.addWidget(add_hint)
        
        # We need "Add" buttons on each card now or a global context.
        # Let's add an "Add to Selected" button to each card for better UX.
        for i, card in enumerate(self.cards, 1):
            btn_add = QPushButton("+ Add Selected Video")
            btn_add.setObjectName("PrimaryButton")
            btn_add.clicked.connect(lambda checked, idx=i: self.add_i(idx))
            card.layout().insertWidget(1, btn_add)
            
        # Footer
        footer = QLabel("Ke學之父 @ 2026")
        footer.setAlignment(Qt.AlignmentFlag.AlignRight)
        footer.setStyleSheet("color: #444; font-size: 10px;")
        main_layout.addWidget(footer)

    def load_settings(self):
        if self.myjson_fn.exists():
            try:
                self.myjson_data = json.loads(self.myjson_fn.read_text())
                self.path = Path(self.myjson_data.get('path', '.'))
                self.lw_display()
                for i in range(1, 5):
                    self.lw_i_display(i)
            except Exception as e:
                print(f"Error loading settings: {e}")

    def lw_display(self):
        self.label_path.setText(str(self.path))
        if self.path.exists():
            f_list = [str(f.name) for f in self.path.glob('*.mp4')]
            self.listWidget.clear()
            self.listWidget.addItems(f_list)

    def filepath(self):
        file_path = QFileDialog.getExistingDirectory(self, "Select Video Directory", str(self.path))
        if file_path:
            self.path = Path(file_path)
            self.lw_display()
            self.save_list()

    def save_list(self):
        self.myjson_data['path'] = str(self.path)
        all_list = []
        for k in range(1, 5):
            n_list = [self.lw[k].item(i).text() for i in range(self.lw[k].count())]
            all_list = all_list + n_list
            self.myjson_data[self.vlist[k]] = n_list
        self.myjson_data[self.vlist[0]] = all_list
        self.myjson_fn.write_text(json.dumps(self.myjson_data))

    def lw_i_display(self, i):
        f_list = self.myjson_data.get(self.vlist[i], [])
        self.lw[i].clear()
        self.lw[i].addItems(f_list)

    def add_i(self, i):
        item = self.listWidget.currentItem()
        if not item: 
            return
        self.lw[i].addItem(item.text())
        self.save_list()

    def del_i(self, i):
        item = self.lw[i].currentItem()
        if not item: 
            return
        self.lw[i].takeItem(self.lw[i].row(item))
        self.save_list()

    def up_i(self, i):
        item = self.lw[i].currentItem()
        if not item: 
            return
        txt = item.text()
        row_i = self.lw[i].row(item)
        if row_i > 0:
            self.lw[i].takeItem(row_i)
            self.lw[i].insertItem(row_i - 1, txt)
            self.lw[i].setCurrentRow(row_i - 1)
        self.save_list()

    def dn_i(self, i):
        item = self.lw[i].currentItem()
        if not item: 
            return
        txt = item.text()
        row_i = self.lw[i].row(item)
        if row_i < self.lw[i].count() - 1:
            self.lw[i].takeItem(row_i)
            self.lw[i].insertItem(row_i + 1, txt)
            self.lw[i].setCurrentRow(row_i + 1)
        self.save_list()

    def play_i(self, i):
        v_list = self.myjson_data.get(self.vlist[i], [])
        if not v_list:
            return
            
        op_loop = "--loop"
        op_clear_queue = "--global-key-clear-playlist='CTRL+W'"
        op1 = "--one-instance"
        op2 = "--playlist-enqueue"
        
        # Kill existing VLC
        try:
            if sys.platform == "win32":
                subprocess.call(["taskkill", "/f", "/im", "vlc.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                subprocess.call(["pkill", "vlc"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
            
        time.sleep(1)
        
        # Start VLC with first item
        try:
            subprocess.Popen([self.cmd, '--width=640', '--height=480', op1, op_loop, op_clear_queue])
            for f in v_list:
                subprocess.Popen([self.cmd, '--width=640', '--height=480', op1, op_loop, op2, str(self.path / f)])
        except Exception as e:
            print(f"Error starting VLC: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion") # Ensure consistent look across platforms
    win = MainForm()
    win.show()
    sys.exit(app.exec())
