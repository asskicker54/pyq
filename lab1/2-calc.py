import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Calculator')
        
        self.input = QLineEdit(self)
        self.input.move(50, 150)

        self.btn = QPushButton('Calculate', self)
        self.btn.move(150, 150)
        self.btn.clicked.connect(self.calculate)

        self.out = QLabel(self)
        self.out.move(250, 150)

    def calculate(self):
        self.out.setText(str(eval(self.input.text())))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    app.exit(app.exec())
