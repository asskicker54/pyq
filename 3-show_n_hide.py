import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QCheckBox

class Show_n_Hide(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Show 'n' hide")

        self.cbox1 = QCheckBox('1', self)
        self.cbox1.move(10, 0)
        self.cbox1.stateChanged.connect(self.change)

        self.cbox2 = QCheckBox('2', self)
        self.cbox2.move(10, 50)
        self.cbox2.stateChanged.connect(self.change)

        self.cbox3 = QCheckBox('3', self)
        self.cbox3.move(10, 100)
        self.cbox3.stateChanged.connect(self.change)

        self.text1 = QLabel('Text1', self)
        self.text1.move(100, 0)
        self.text1.setVisible(False)

        self.text2 = QLabel('Text2', self)
        self.text2.move(100, 50)
        self.text2.setVisible(False)

        self.text3 = QLabel('Text3', self)
        self.text3.move(100, 100)
        self.text3.setVisible(False)

    def change(self):
        if self.cbox1.isChecked() == True:
            self.text1.setVisible(True)
        else: 
            self.text1.setVisible(False)

        if self.cbox2.isChecked() == True:
            self.text2.setVisible(True)
        else: 
            self.text2.setVisible(False)
        
        if self.cbox3.isChecked() == True:
            self.text3.setVisible(True)
        else: 
            self.text3.setVisible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Show_n_Hide()
    ex.show()
    app.exit(app.exec())

        