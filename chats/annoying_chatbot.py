import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import random
from annoying_responses import responses

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle ("AnnoyingGPT - dramatic responses")
        self.setGeometry (450, 100, 500, 500)

        self.response = responses
        central_widget = QWidget(self)
        self.setCentralWidget (central_widget)
        central_widget.setStyleSheet("""
                                     background-color: black;
                                     color: white;
                                     """)

        self.input_field = QLineEdit(central_widget)
        self.input_field.setPlaceholderText("Type anything here...")
        self.input_field.setFont(QFont("Arial", 12))
        self.input_field.setStyleSheet ("""
                                        background-color: #111;
                                        color: white;
                                        padding: 8px;
                                        border-radius: 8px;
                                        """)

        self.button = QPushButton ("Ask!", central_widget)
        self.label = QLabel ("You Ask, I answer!", central_widget)
        self.label.setWordWrap(True)
        self.label.setAlignment (Qt.AlignCenter)
        self.initUI()

        label1 = QLabel ("AnnoyingGPT", central_widget)
        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(QFont("Times New Roman", 50))
        label1.setStyleSheet("font-weight: bold;")

        label2 = QLabel ("(aka 'primitive ChatGPT'😂🤖)", central_widget)
        label2.setAlignment(Qt.AlignCenter)
        label2.setFont(QFont("Times New Roman", 15))

        label3 = QLabel ("Not a real AI(Just AI-inspired chatbot simulator)", central_widget)
        label3.setAlignment(Qt.AlignCenter)
        label3.setFont(QFont("Arial", 7))
        label3.setStyleSheet("font-style: italic;")

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addStretch(2)
        vbox.addWidget(self.label)
        vbox.addStretch(1)
        central_widget.setLayout(vbox)

        input_box = QVBoxLayout()
        input_box.addWidget (self.input_field)
        input_box.addWidget(self.button, Qt.AlignCenter)
        vbox.addLayout (input_box)

    def initUI (self):
        self.button.setStyleSheet("""
                       QPushButton{
                                  font-size: 40px;
                                  background-color: white;
                                  color: black;
                                  border-radius: 14px;
                                  padding: 10px;
                                  }
                       QPushButton:hover {
                                   background-color:#ddd
                       }
                                  """)
        self.button.clicked.connect (self.on_click)
        self.input_field.returnPressed.connect(self.on_click)

        self.label.setStyleSheet("""
                                   font-size: 20px;
                                   padding: 10px
                                """)

    def on_click (self):
        print ("Button Clicked!")
        response = random.choice (self.response)
        self.label.setText (response)
        self.button.setText ("Ask again")

def main ():
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main ()