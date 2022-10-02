import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from numpy import random

class RockGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('rockgame_start.ui', self)
        self.start_btn.clicked.connect(self.start)

    def start(self):
        rocks_am = self.rock_count.value()
        if rocks_am > 0:
            uic.loadUi('rockgame.ui', self)
            self.rocks.setText(str(rocks_am))
            self.take.clicked.connect(self.take_rocks)
    
    def take_rocks(self):
        if int(self.rocks.text()) - self.spinBox.value() <= 0:
            self.rocks.setText("Вы выиграли!")
            self.take.setEnabled(False)
        else:
            self.rocks.setText(str(int(self.rocks.text()) - self.spinBox.value()))
            self.last_action.setText(f"Вы взяли {self.spinBox.value()}.\n{self.last_action.text()}\n")
            self.ai_move()
    
    def ai_move(self):
        if int(self.rocks.text()) < 4:
            self.rocks.setText("Вы проиграли!")
            self.take.setEnabled(False)
            return
        
        if int(self.rocks.text()) % 4 == 0:
            value = random.randint(1, 4)
        else:
            value = int(self.rocks.text()) % 4
        
        self.rocks.setText(str(int(self.rocks.text()) - value))
        self.last_action.setText(f"\n Противник взял {value}.\n{self.last_action.text()}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RockGame()
    ex.show()
    sys.exit(app.exec_())