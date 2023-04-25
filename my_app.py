from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from instr import *
import second_win

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.laoyut_line = QVBoxLayout()
        self.laoyut_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.laoyut_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.laoyut_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.laoyut_line)
    def next_click(self):
        self.hide()
        self.tw = second_win.TestWin()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mv = MainWin()
app.exec_()
