import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QWidget, QStackedWidget
from PyQt5.QtCore import Qt
from digital_clock import Digital_Clock
from stopwatch import Stopwatch
from alarm_clock import Alarm_Clock

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clock")
        #Widgets
        self.ui_label = QLabel("🎀 CLOCK 🎀", self)
        self.digital_clock_button = QPushButton("View Clock")
        self.stopwatch_button = QPushButton("Stopwatch")
        self.alarm_button = QPushButton("Set Alarm")
        self.initUI()

    def initUI(self):

        #Layout Manager
        self.ui_label.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        vbox.addWidget(self.ui_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.digital_clock_button)
        hbox.addWidget(self.stopwatch_button)
        hbox.addWidget(self.alarm_button)

        vbox.addLayout(hbox)
        central_widget = QWidget(self)
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        self.stack = QStackedWidget()
        self.digital_screen = Digital_Clock()
        self.stopwatch_screen = Stopwatch()
        self.alarm_screen = Alarm_Clock()
        self.stack.addWidget(self.digital_screen)
        self.stack.addWidget(self.stopwatch_screen)
        self.stack.addWidget(self.alarm_screen)

        self.stack.hide()
        vbox.addWidget(self.stack)

        vbox.setContentsMargins(50, 50, 50, 50)
        vbox.setSpacing(20)
        hbox.setSpacing(30)

        self.setStyleSheet("""
            QPushButton, QLabel{
                font-family: Times New Roman;    
            }
            QLabel{
                font-size: 50px;
                padding: 50px;
                color: hsl(295, 36%, 20%);
                background-color: hsl(295, 36%, 60%);
                border-radius: 20px;
            }
            QPushButton{
                font-size: 38px;
                padding: 25px 35px;
                border-radius: 20px;
                background-color: hsl(295, 36%, 64%);
                color: hsl(295, 36%, 20%);
            }
            QPushButton:hover{
                background-color: hsl(295, 40%, 80%);
            }
            """)

        for screen in [self.stopwatch_screen, self.digital_screen, self.alarm_screen]:
            screen.setStyleSheet("""
                                    background-color: hsl(295, 36%, 90%);
                                    
                                """)

        self.digital_clock_button.clicked.connect(
            lambda: self.show_screen(0)
        )
        self.stopwatch_button.clicked.connect(
            lambda: self.show_screen(1)
        )
        self.alarm_button.clicked.connect(
            lambda: self.show_screen(2)
        )
    def show_screen(self, index):
        self.stack.setCurrentIndex(index)
        self.stack.show()
        self.ui_label.hide()

def main():
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()