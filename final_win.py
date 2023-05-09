from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def results(self):
        if self.exp.age < 7:
            self.index = 0
            return ' немає даних для такого віку'
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t2)) - 200) / 10
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return text_res1
            elif self.index < 21 and self.index >= 17:
                return text_res2
            elif self.index < 17 and self.index >= 12:
                return text_res3
            elif self.index < 12 and self.index >= 6.5:
                return text_res4
            else:
                return text_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return text_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return text_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return text_res3
            elif self.index < 10.5 and self.index >= 5:
                return text_res4
            else:
                return text_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return text_res1
            elif self.index < 18 and self.index >= 14:
                return text_res2
            elif self.index < 14 and self.index >= 9:
                return text_res3
            elif self.index < 9 and self.index >= 3.5:
                return text_res4
            else:
                return text_res5
        if self.exp.age >= 15:
            if self.index >= 15:
                return text_res1
            elif self.index < 15 and self.index >= 11:
                return text_res2
            elif self.index < 11 and self.index >= 6:
                return text_res3
            elif self.index < 6 and self.index >= 0.5:
                return text_res4
            else:
                return text_res5
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.workheart_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.workheart_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)    
