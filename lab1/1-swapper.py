import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class Swapper(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Swapper')

        self.btn = QPushButton('-->', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 150)
        self.btn.clicked.connect(self.swap)

        self.in1 = QLineEdit(self)
        self.in1.move(45, 200)

        self.in2 = QLineEdit(self)
        self.in2.move(200, 200)
        

    def swap(self):
        temp = self.in1.text()
        self.in1.setText(self.in2.text())
        self.in2.setText(temp)
        
        if self.btn.text() == '-->':
            self.btn.setText('<--')
        else:
            self.btn.setText('-->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Swapper()
    ex.show()
    sys.exit(app.exec())