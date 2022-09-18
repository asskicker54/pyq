import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit
from PyQt5.QtGui import QFont

calc = ['/', '7', '8', '9','*', '4', '5', '6', '-', '1', '2', '3', '+', '0', '.']

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        self.setGeometry(400, 450, 400, 450)

        self.screen = QLineEdit("", self)
        self.screen.setGeometry(5, 5, 390, 150)
        self.screen.setFont(QFont("Arial", 40))
        self.screen.setPlaceholderText("0")
        
        i = 0
        x = 300
        y = 155
        self.btns = []
        for btn in calc:
            self.btns.append(QPushButton(btn, self))
            self.btns[i].setGeometry(x, y, 100, 50)
            self.btns[i].clicked.connect(self.insert_symbol)
            i += 1
            x += 100
            if x == 400:
                x = 0
                y += 55

        self.ac_btn = QPushButton("AC", self)
        self.ac_btn.setGeometry(0, 155, 100, 50)
        self.ac_btn.clicked.connect(self.clear)
        
        self.eq_btn = QPushButton("=", self)
        self.eq_btn.setGeometry(200, 375, 200, 50)
        self.eq_btn.clicked.connect(self.calculate)

    def insert_symbol(self):
        self.screen.setText(self.screen.text() + self.sender().text())

    def clear(self):
        self.screen.setText("")
        self.screen.setPlaceholderText("0")

    def calculate(self):
        self.screen.setText(str(round(eval(self.screen.text()), 3)))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = Calculator()
    exe.show()
    app.exit(app.exec())