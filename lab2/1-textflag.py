import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class TextFlag(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('text.ui', self)
        self.rbtns = [[self.rb1_w, self.rb1_b, self.rb1_r], [self.rb2_w, self.rb2_b, self.rb2_r], [self.rb3_w, self.rb3_b, self.rb3_r]]
        self.pb.clicked.connect(self.draw)

    def draw(self):
        self.label.setText('')
        for rbtns_group in self.rbtns:
            for rb in rbtns_group:
                if rb.isChecked():
                    self.label.setText(self.label.text() + rb.text() + '    ')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextFlag()
    ex.show()
    sys.exit(app.exec())
