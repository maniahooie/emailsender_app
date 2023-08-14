from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox
from PyQt5 import uic
import sys
from email_sender import send_email

class EmailSender(QMainWindow):
    def __init__(self):
        super(EmailSender, self).__init__()

        #load ui file
        uic.loadUi("emailsender.ui", self)

        #define our widgets
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.send_email)

    def send_email(self):
        if self.lineEdit.text():
            send_email(recipient=self.lineEdit.text(), email=self.textEdit.toPlainText())
        else:
            message = QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setText("invalid recipient")
            message.setWindowTitle("error!")
            message.exec_()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailSender()
    window.show()
    app.exec_()
