#Imports
import os
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QLineEdit)
from PyQt5.QtCore import Qt

#main widget
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        # widgets
        self.city_label = QLabel("Select a city", self)
        self.city_input = QLineEdit(self)
        self.get_weather = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    #initUI
    def initUI(self):
        #stuff
        self.setWindowTitle("WEATHER APP")
        self.city_input.returnPressed.connect(self.fetch_weather)
        #layout
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        #Align center
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        #Object name
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather.setObjectName("get_weather")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        #StyleSheet
        self.setStyleSheet(
            """
            QPushButton, QLabel{
                font-family: Times New Roman;
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#city_label{
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 30px;
            }
            QLabel#temperature_label{
                font-size: 75px;
                font-family: calibri;
            }
            QLabel#emoji_label{
                font-size: 80px;
                font-family: segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 30px;
                font-family: calibri;
            }
            """
        )

        #when button clicked
        self.get_weather.clicked.connect(self.fetch_weather)

    #fetch weather
    def fetch_weather(self):
        #key setup
        api_key = os.getenv("OPENWEATHER_API_KEY").strip()
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        #try-except
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data['cod'] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden\nAccess is denied")
                case 404:
                    self.display_error("Not Found\nCity not found")
                case 500:
                    self.display_error("Internal Server Error\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout\nNo reponse from the server")
                case _:
                    self.display_error(f"HTTP error occured\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error: {req_error}")

    #display error
    def display_error(self, message):

        #Set temperature label to the error text
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)

        # Clear other variables
        self.emoji_label.clear()
        self.description_label.clear()

    #display weather
    def display_weather(self, data):

        #temperature in diff scales
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67

        # weather id
        weather_id = data["weather"][0]["id"]

        #weather description
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_f:.0f}°F")
        self.temperature_label.setStyleSheet("font-size: 75px;")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    #static method to get weather emoji
    @staticmethod
    def get_weather_emoji(weather_id):

        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌥"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())