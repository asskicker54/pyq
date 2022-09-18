from cProfile import label
import sys

from PyQt5.QtWidgets import QLabel, QPushButton, QApplication, QWidget

MORZE = {'0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.', 'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..'
        }


class MorzeTranslator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Translator')
        self.buttons = []
        x = 0
        y = 100
        i = 0
        for letter in MORZE:
            self.buttons.append(QPushButton(letter, self))
            self.buttons[i].move(x, y)
            self.buttons[i].clicked.connect(self.printMorze)
            i += 1
            x += 75
            if x == 750:
                y += 25
                x = 0

        self.label = QLabel('', self)
        self.label.setGeometry(150, 20, 500, 50)

    def printMorze(self):
        self.label.setText(self.label.text() + MORZE[self.sender().text()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = MorzeTranslator()
    exe.show()
    app.exit(app.exec())