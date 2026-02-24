from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QVBoxLayout, QHBoxLayout, QLineEdit,
                             QLabel, QWidget)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Temperature Converter")
        #Initialize widgets
        self.header = QLabel("Temperature Converter")
        self.label = QLabel("Enter temperature: ")
        self.enter_temp_line = QLineEdit(self)
        self.enter_temp_line.setPlaceholderText("20")

        self.c_to_f_button = QPushButton("°C to °F")
        self.f_to_c_button = QPushButton("°F to °C")
        self.c_to_k_button = QPushButton("°C to  K")
        self.k_to_c_button = QPushButton(" K to °C")
        self.f_to_k_button = QPushButton(" F to  K")
        self.k_to_f_button = QPushButton(" K to  F")

        self.initUI()

    def initUI(self):
        #Layout
        central_widget = QWidget()
        vbox = QVBoxLayout()
        vbox.addWidget(self.header)
        vbox.addWidget(self.label)
        vbox.addWidget(self.enter_temp_line)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.c_to_f_button)
        hbox1.addWidget(self.f_to_c_button)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.c_to_k_button)
        hbox2.addWidget(self.k_to_c_button)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.f_to_k_button)
        hbox3.addWidget(self.k_to_f_button)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setCentralWidget(central_widget)
        central_widget.setLayout(vbox)

        #Stylesheet
        self.label.setObjectName("label")
        self.header.setObjectName("header")

        self.setStyleSheet("""
            QLabel#header{
                color: black;
                font-size: 40px;
                font-weight: bold;
                font-family: Brush Script MT;
                text-decoration: underline;
            }
            QLabel#label{
                color: black;
                font-size: 30px;
                font-weight: bold;
                font-family: Pacifico;
            }
            QPushButton{
                font-size: 25px;
                font-family: Times New Roman;
                background-color: #b9c0eb;
                border: 2px solid black;
                border-radius: 10px;
                margin: 3px;
                padding: 2px;
            }
            QPushButton:hover{
                font-size: 30px;
                font-family: Segoe Script;
                background-color: #9ea7e1;
            }
            QLineEdit{
                background-color: #b9c0eb;
                font-family: Times New Roman;
                font-size: 30px;
                border: 2px solid black;
                border-radius: 10px;
                margin: 3px;
                padding: 2px;
            }
        """)

        #Button connect to functions

        self.c_to_f_button.clicked.connect(self.c_to_f)
        self.f_to_c_button.clicked.connect(self.f_to_c)
        self.c_to_k_button.clicked.connect(self.c_to_k)
        self.k_to_c_button.clicked.connect(self.k_to_c)
        self.f_to_k_button.clicked.connect(self.f_to_k)
        self.k_to_f_button.clicked.connect(self.k_to_f)

    def get_user_temp(self):
        line_text = self.enter_temp_line.text()
        if not line_text:
            self.label.setText("Please enter a temperature")
            return None
        try:
            text = float(line_text)
            return text
        except ValueError:
            self.label.setText("Please enter a correct value")
            return None

    def c_to_f(self):
        text = self.get_user_temp()
        if text is None:
            return
        calculate_c_to_f = (9 / 5) * text + 32
        self.label.setText(f"{calculate_c_to_f:.2f}")

    def f_to_c(self):
        text = self.get_user_temp()
        if text is None:
            return
        calculate_f_to_c = (5 / 9) * (text - 32)
        self.label.setText(f"{calculate_f_to_c:.2f}")

    def c_to_k(self):
        text = self.get_user_temp()
        if text is None:
            return
        calculate_c_to_k = text + 273.15
        self.label.setText(f"{calculate_c_to_k:.2f}")

    def k_to_c(self):
        text = self.get_user_temp()
        if text is None:
            return
        calculate_k_to_c = text - 273.15
        self.label.setText(f"{calculate_k_to_c:.2f}")

    def f_to_k(self):
        text = self.get_user_temp()
        if text is None:
            return
        calculate_f_to_k = (text - 32) * (5 / 9) + 273.15
        self.label.setText(f"{calculate_f_to_k:.2f}")

    def k_to_f(self):
        text = self.get_user_temp()
        if text is None:
            return
        calculate_k_to_f = (text - 273.15) * (9 / 5) + 32
        self.label.setText(f"{calculate_k_to_f:.2f}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()