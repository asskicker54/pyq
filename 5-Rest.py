import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QPlainTextEdit

class Cheque(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Restaraunt Cheque')
        #Hotdog
        self.hotdog = QLabel('Хот-дог - 100 руб.', self)
        self.hotdog.setGeometry(10, 25, 100, 25)

        self.hotdogFinal = QLabel("0", self)
        self.hotdogFinal.setGeometry(170, 25, 25, 25)
        self.hotdogFinal.setVisible(False)

        self.hotdogPlusBtn = QPushButton('+', self)
        self.hotdogPlusBtn.setGeometry(120, 0, 25, 25)
        self.hotdogPlusBtn.clicked.connect(self.add_del_hotdog)

        self.hotdogMinusBtn = QPushButton('-', self)
        self.hotdogMinusBtn.setGeometry(120, 50, 25, 25)
        self.hotdogMinusBtn.clicked.connect(self.add_del_hotdog)
        
        self.hotdogAmount = QLabel('0', self)
        self.hotdogAmount.setGeometry(128, 25, 25, 25)
        #Burger
        self.burger = QLabel('Бургер - 200 руб.', self)
        self.burger.setGeometry(10, 125, 100, 25)

        self.burgerFinal = QLabel("0", self)
        self.burgerFinal.setGeometry(170, 125, 25, 25)
        self.burgerFinal.setVisible(False)

        self.burgerPlusBtn = QPushButton('+', self)
        self.burgerPlusBtn.setGeometry(120, 100, 25, 25)
        self.burgerPlusBtn.clicked.connect(self.add_del_burger)

        self.burgerMinusBtn = QPushButton("-", self)
        self.burgerMinusBtn.setGeometry(120, 150, 25, 25)
        self.burgerMinusBtn.clicked.connect(self.add_del_burger)

        self.burgerAmount = QLabel("0", self)
        self.burgerAmount.setGeometry(128, 125, 25, 25)

        #Cheque
        self.chequeBtn = QPushButton("Получить чек", self)
        self.chequeBtn.setGeometry(200, 200, 100, 25)
        self.chequeBtn.clicked.connect(self.get_cheque)

        self.final = QPlainTextEdit("Чек:", self)
        self.final.setGeometry(0, 250, 600, 600)
        self.final.setReadOnly(True)

    def add_del_hotdog(self):
        if self.sender().text() == "+":
            self.hotdogAmount.setText(f"{int(self.hotdogAmount.text()) + 1}")
            self.hotdogFinal.setText(f"{int(self.hotdogAmount.text()) * 100}")
            self.hotdogFinal.setVisible(True)
        elif self.sender().text() == "-" and int(self.hotdogAmount.text()) > 0:
            self.hotdogAmount.setText(f"{int(self.hotdogAmount.text()) - 1}")
            if self.hotdogAmount.text() == "0":
                self.hotdogFinal.setVisible(False)
            else:
                self.hotdogFinal.setText(f"{int(self.hotdogAmount.text()) * 100}")

    def add_del_burger(self):
        if self.sender().text() == "+":
            self.burgerAmount.setText(f"{int(self.burgerAmount.text()) + 1}")
            self.burgerFinal.setText(f"{int(self.burgerAmount.text()) * 200}")
            self.burgerFinal.setVisible(True)
        elif self.sender().text() == "-" and int(self.burgerAmount.text()) > 0:
            self.burgerAmount.setText(f"{int(self.burgerAmount.text()) - 1}")
            if self.burgerAmount.text() == "0":
                self.burgerFinal.setVisible(False)
            else:
                self.burgerFinal.setText(f"{int(self.burgerAmount.text()) * 200}")

    def get_cheque(self):
        self.final.appendPlainText(f"\n ХОТДОГ:\tx{self.hotdogAmount.text()}\t{self.hotdogFinal.text()}руб.")
        self.final.appendPlainText(f"\n БУРГЕР:\tx{self.burgerAmount.text()}\t{self.burgerFinal.text()}руб.")
        
        self.final.appendPlainText(f"\nИТОГО:\t\t{int(self.burgerFinal.text()) + int(self.hotdogFinal.text())}руб.")
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cheque()
    ex.show()
    app.exit(app.exec())
