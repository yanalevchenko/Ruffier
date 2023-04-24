from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.index_text = QLabel(txt_index)
        self.workheart_text = QLabel(txt_workheart)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.workheart_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

app = QApplication([])
m = FinalWin()
app.exec_()