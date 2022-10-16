import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from password import check_password, PasswordError
from phone import check_number, PhoneException

class SignIn(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('6.ui', self)
        self.pushButton.clicked.connect(self.register)
        
    def register(self):
        try:
            check_password(self.password.text())
            check_number(self.phone.text())
        except PasswordError as e:
            self.status_label.setText(f"Password error: {str(e)}")
        except PhoneException as e:
            self.status_label.setText(f"Phone error: {str(e)}")
        else:
            self.status_label.setText("Welcome!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SignIn()
    ex.show()
    sys.exit(app.exec_())