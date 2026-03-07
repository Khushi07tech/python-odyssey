from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QVBoxLayout, QPushButton, QWidget)
from PyQt5.QtCore import Qt
import sys
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Your Companion")

        #Initialize widgets
        self.welcome_label = QLabel("Welcome", self)
        self.random_quote_label = QLabel("random", self)
        self.select_label = QLabel("Select", self)
        self.random_ayah_button = QPushButton("Ayah", self)
        self.random_prophet_button = QPushButton("Prophet", self)
        self.random_hadith_button = QPushButton("Hadith", self)

        #Connect buttons to functions

        self.layout()
        self.style()

    def layout(self):

        vbox = QVBoxLayout()

        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.random_quote_label.setAlignment(Qt.AlignCenter)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox.addWidget(self.welcome_label)
        vbox.addWidget(self.random_quote_label)
        vbox.addWidget(self.select_label)
        vbox.addWidget(self.random_ayah_button)
        vbox.addWidget(self.random_prophet_button)
        vbox.addWidget(self.random_hadith_button)
        central_widget.setLayout(vbox)

        self.random_ayah_button.clicked.connect(self.random_ayah)
        self.random_prophet_button.clicked.connect(self.random_prophet)
        self.random_hadith_button.clicked.connect(self.random_hadith)

    def style(self):
        self.setStyleSheet("""
            QLabel{
                font-family: calibri;
                font-size: 20px;
            }
            QPushButton{
                background-color: #7FB8C2;
                color: black;
                border-radius: 10px;
                border: 1px solid #7FB8C2;
                padding: 20px;
                font-family: Times New Roman;
                font-size: 20px; 
            }
    
            QPushButton:hover{
                background-color: #A8DADC;
                border-radius: 15px;
                padding: 15px;
                font-family: Times New Roman;
                font-size: 30px; 
            }
        """)

    def random_ayah(self):
        base_url = "https://api.quran.com/api/v4/verses/random?translations=131"
        params = {
            "translation": 131,
            "fields": "text_uthmani"
        }

        try:
            response = requests.get(base_url, params)
            response.raise_for_status()

            data = response.json()

            verse = data['verse']

            arabic_text = verse['text_uthmani']
            reference = verse['verse_key']

            self.random_quote_label.setText(arabic_text)
            self.welcome_label.setText(reference)


        except requests.exceptions.RequestException as e:
            print(f"Error Occured:\n{e}")


    def random_prophet(self):
            pass

    def random_hadith(self):
            pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
