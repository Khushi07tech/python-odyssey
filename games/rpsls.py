from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout, QWidget,
                             QMessageBox)
from PyQt5.QtCore import Qt
import sys
import random

class RPSLS(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPSLS")
        self.welcome_label = QLabel("Welcome to the\nRPSLS Challenge!", self)
        self.user_points_label = QLabel("User Points: ", self)
        self.comp_points_label = QLabel("Computer Points: ", self)
        self.computer_choice_label = QLabel("", self)
        self.winner_displaying_label = QLabel("", self)
        self.rock_push_button = QPushButton("rock", self)
        self.paper_push_button = QPushButton("paper", self)
        self.scissors_push_button = QPushButton("scissors", self)
        self.lizard_push_button = QPushButton("lizard", self)
        self.spock_push_button = QPushButton("spock", self)
        self.show_rules_button = QPushButton("Game Rules", self)

        self.user_points = 0
        self.comp_points = 0

        self.layout()
        self.style()
        self.connecting_buttons()

    def layout(self):
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.computer_choice_label.setAlignment(Qt.AlignCenter)
        self.winner_displaying_label.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()

        vbox.addWidget(self.welcome_label)
        vbox.addWidget(self.user_points_label)
        vbox.addWidget(self.comp_points_label)
        vbox.addWidget(self.computer_choice_label)
        vbox.addWidget(self.winner_displaying_label)

        hbox1 = QHBoxLayout()

        hbox1.addWidget(self.rock_push_button)
        hbox1.addWidget(self.paper_push_button)
        hbox1.addWidget(self.scissors_push_button)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.lizard_push_button)
        hbox2.addWidget(self.spock_push_button)
        hbox2.addWidget(self.show_rules_button)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

    def style(self):
        self.welcome_label.setObjectName("welcome_label")
        self.user_points_label.setObjectName("user_points_label")
        self.comp_points_label.setObjectName("comp_points_label")
        self.computer_choice_label.setObjectName("computer_choice_label")
        self.winner_displaying_label.setObjectName("winner_displaying_label")
        self.show_rules_button.setObjectName("show_rules_button")

        self.setStyleSheet("""
            QLabel#welcome_label{
                color: #6C63FF;         
                font-family: "Quicksand", sans-serif; 
                font-size: 40px;
                font-weight: 600;
                padding: 10px 20px;
                border-radius: 10px;
                background-color: #F5F5FF;   
            }
            QLabel#user_points_label{
                font-size: 15px;
                font-family: calibri;
                color: #4A0082;
            }
            QLabel#comp_points_label{
                font-size: 15px;
                font-family: calibri;
                color: #4B0090;
            }
            QLabel#computer_choice_label{
                font-size: 20px;
                font-family: Comic Sans;
                color: #CC9900; 
                text-shadow: 1px 1px #A67C00;
            }
            QLabel#winner_displaying_label{
                font-size: 20px;
                font-family: Times New Roman;
                color: black;
            }
            QPushButton#show_rules_button{
                background-color: #4F46E5;
                color: #E0E0FF;
                border-radius: 10px;
                border: 1px solid #7FB8C2;
                padding: 20px;
                font-family: calibri;
                font-size: 20px;
            }
            QPushButton:hover#show_rules_button{
                background-color: #6C63FF;
                border-radius: 15px;
                padding: 10px;
                font-family: Times New Roman;
                font-size: 25px;
            }
            QPushButton{
                background-color: #6C63FF;
                color: #E0E0FF;
                border-radius: 10px;
                border: 1px solid #7FB8C2;
                padding: 20px;
                font-family: Times New Roman;
                font-size: 20px;
            }
            QPushButton:hover{
                background-color: #4F46E5;
                border-radius: 15px;
                padding: 10px;
                font-family: calibri;
                font-size: 25px; 
            }
        """)

    def connecting_buttons(self):
        self.rock_push_button.clicked.connect(self.game_logic)
        self.paper_push_button.clicked.connect(self.game_logic)
        self.scissors_push_button.clicked.connect(self.game_logic)
        self.lizard_push_button.clicked.connect(self.game_logic)
        self.spock_push_button.clicked.connect(self.game_logic)
        self.show_rules_button.clicked.connect(self.show_rules)

    def game_logic(self):
        button = self.sender()
        button_text = button.text()
        computer_choice = random.choice(["rock", "paper", "scissors", "lizard", "spock"])
        self.computer_choice_label.setText("Computer Choice: " + computer_choice)


        rules = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["spock", "paper"],
            "spock": ["scissors", "rock"]
        }

        if computer_choice in rules[button_text]:
            self.winner_displaying_label.setText("You win!")
            self.winner_displaying_label.setStyleSheet("color: #4CAF50;")
            self.user_points += 1
            self.user_points_label.setText(f"User Points: {self.user_points}")
        elif button_text == computer_choice:
            self.winner_displaying_label.setText("Tie!")
            self.winner_displaying_label.setStyleSheet("color: #E6B800;")
        else:
            self.winner_displaying_label.setText("You lose!")
            self.winner_displaying_label.setStyleSheet("color: #FF4C4C;")
            self.comp_points += 1
            self.comp_points_label.setText(f"Computer Points: {self.comp_points}")

    def show_rules(self):
        rules = (
            "Scissors cuts Paper\n"
            "Paper covers Rock\n"
            "Rock crushes Lizard\n"
            "Lizard poisons Spock\n"
            "Spock smashes Scissors\n"
            "Scissors decapitates Lizard\n"
            "Lizard eats Paper\n"
            "Paper disproves Spock\n"
            "Spock vaporizes Rock\n"
            "Rock crushes Scissors"
        )
        QMessageBox.information(self, "Rules", rules)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RPSLS()
    window.show()
    sys.exit(app.exec_())