import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class DailyPlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('planner.ui', self)
        self.ok.clicked.connect(self.add)

    def add(self):
        date = str(self.calendar.selectedDate().toPyDate())
        name = self.name_text.toPlainText()
        time = str(self.timeEdit.time().toPyTime())
        mark = name + " - " + date + " в " + time
        self.list.addItem(mark)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DailyPlanner()
    ex.show()
    sys.exit(app.exec())
