import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class NoteBook(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('notebook.ui', self)

        self.pb.clicked.connect(self.add)
        self.le.setPlaceholderText('Имя')
        self.le2.setPlaceholderText('Номер')

    def add(self):
        self.lw.addItem(f'{self.le.text()} - {self.le2.text()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NoteBook()
    ex.show()
    sys.exit(app.exec())