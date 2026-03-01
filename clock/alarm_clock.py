import sys
import datetime
import winsound
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QLineEdit, QVBoxLayout)
from PyQt5.QtCore import Qt, QTimer

class Alarm_Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.front_label = QLabel("Alarm", self)
        self.set_time = QLineEdit(self)
        self.set_time.setPlaceholderText("Set a time (HH:MM:SS)")
        self.set_time_button = QPushButton("Set", self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_time)

        self.alarm_time = None
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Alarm")
        self.front_label.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()

        vbox.addWidget(self.front_label)
        vbox.addWidget(self.set_time)
        vbox.addWidget(self.set_time_button)

        self.setLayout(vbox)

        self.setStyleSheet("""
            QLabel{
                font-family: Arial;
                font-size: 50px;
                padding: 50px;
                color: hsl(295, 36%, 20%);
                background-color: hsl(295, 36%, 60%);
                border-radius: 20px;
            }                       
            QPushButton{
                font-family: Arial;
                font-size: 38px;
                padding: 25px 35px;
                border-radius: 20px;
                background-color: hsl(295, 36%, 64%);
                color: hsl(295, 36%, 20%);
            }
            QPushButton:hover{
                background-color: hsl(295, 40%, 80%);
            }
            QLineEdit{
               background-color: hsl(295, 40%, 70%);
               color: hsl(295, 36%, 20%);
               font-size: 50px;
            }
        """)

        self.set_time_button.clicked.connect(self.get_time)

    def get_time(self):
        text = self.set_time.text()
        try:
            self.alarm_time = datetime.datetime.strptime(text, "%H:%M:%S").time()
            self.timer.start(1000)
        except ValueError:
            self.front_label.setText("Invalid Input!")

    def check_time(self):
        current_time = datetime.datetime.now().time()
        self.front_label.setText(current_time.strftime("%H:%M:%S"))

        if current_time.hour == self.alarm_time.hour and \
           current_time.minute == self.alarm_time.minute and \
           current_time.second == self.alarm_time.second:
            self.timer.stop()
            winsound.Beep(1500, 1000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    alarm_clock = Alarm_Clock()
    alarm_clock.show()
    sys.exit(app.exec_())
