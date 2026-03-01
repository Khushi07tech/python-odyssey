from PyQt5.QtWidgets import (QApplication, QVBoxLayout,QHBoxLayout,
                             QLineEdit, QPushButton, QWidget)
import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.tokens = []
        self.setWindowTitle("Calculator")

        self.user_input_line = QLineEdit(self)
        self.user_input_line.setPlaceholderText("Enter here...")

        # Vertical line # 1:
        self.digit7_button = QPushButton("7", self)
        self.digit4_button = QPushButton("4", self)
        self.digit3_button = QPushButton("3", self)
        self.digit0_button = QPushButton("0", self)

        # Vertical line # 2:
        self.digit8_button = QPushButton("8", self)
        self.digit5_button = QPushButton("5", self)
        self.digit2_button = QPushButton("2", self)
        self.decimal_button = QPushButton(".", self)

        # Vertical line # 3:
        self.digit9_button = QPushButton("9", self)
        self.digit6_button = QPushButton("6", self)
        self.digit1_button = QPushButton("1", self)
        self.equal_button = QPushButton("=", self)

        # vertical line # 4:
        self.oper_divide_button = QPushButton("/", self)
        self.oper_multiply_button = QPushButton("*", self)
        self.oper_subtract_button = QPushButton("-", self)
        self.oper_add_button = QPushButton("+", self)

        self.init_ui()
        self.styling()

    def init_ui(self):

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.user_input_line)

        hbox = QHBoxLayout()

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.digit7_button)
        vbox1.addWidget(self.digit4_button)
        vbox1.addWidget(self.digit3_button)
        vbox1.addWidget(self.digit0_button)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.digit8_button)
        vbox2.addWidget(self.digit5_button)
        vbox2.addWidget(self.digit2_button)
        vbox2.addWidget(self.decimal_button)

        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.digit9_button)
        vbox3.addWidget(self.digit6_button)
        vbox3.addWidget(self.digit1_button)
        vbox3.addWidget(self.equal_button)

        vbox4 = QVBoxLayout()
        vbox4.addWidget(self.oper_divide_button)
        vbox4.addWidget(self.oper_multiply_button)
        vbox4.addWidget(self.oper_subtract_button)
        vbox4.addWidget(self.oper_add_button)

        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)
        hbox.addLayout(vbox3)
        hbox.addLayout(vbox4)

        main_layout.addLayout(hbox)

        self.setLayout(main_layout)

        self.digit0_button.clicked.connect(self.send_digits)
        self.digit1_button.clicked.connect(self.send_digits)
        self.digit2_button.clicked.connect(self.send_digits)
        self.digit3_button.clicked.connect(self.send_digits)
        self.digit4_button.clicked.connect(self.send_digits)
        self.digit5_button.clicked.connect(self.send_digits)
        self.digit6_button.clicked.connect(self.send_digits)
        self.digit7_button.clicked.connect(self.send_digits)
        self.digit8_button.clicked.connect(self.send_digits)
        self.digit9_button.clicked.connect(self.send_digits)
        self.decimal_button.clicked.connect(self.send_digits)
        self.oper_divide_button.clicked.connect(self.send_digits)
        self.oper_multiply_button.clicked.connect(self.send_digits)
        self.oper_subtract_button.clicked.connect(self.send_digits)
        self.oper_add_button.clicked.connect(self.send_digits)

        self.equal_button.clicked.connect(self.split)
        self.user_input_line.returnPressed.connect(self.split)

    def styling(self):

        for btn in [self.digit0_button, self.digit1_button,
                    self.digit2_button, self.digit3_button,
                    self.digit4_button, self.digit5_button,
                    self.digit6_button, self.digit7_button,
                    self.digit8_button, self.digit9_button]:

            btn.setStyleSheet("""
            QPushButton{
                background-color: #A8DADC;
                color: black;
                border-radius: 10px;
                border: 1px solid #7FB8C2;
                padding: 20px;
                font-family: Times New Roman;
                font-size: 20px; 
            }
    
            QPushButton:hover{
                background-color: #7FB8C2;
                border-radius: 15px;
                padding: 15px;
                font-family: Times New Roman;
                font-size: 30px; 
            }
            """)

        for oper_btn in [self.oper_divide_button, self.oper_multiply_button,
                         self.oper_add_button, self.oper_subtract_button,
                         self.equal_button, self.decimal_button]:
            oper_btn.setStyleSheet("""
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

        self.user_input_line.setStyleSheet("""
            background-color: #FAFAFA;
            color: #333333;
            border-radius: 10px;
            border: 1px solid #CCCCCC;
            padding: 20px;
            font-family: Comic Sans;
            font-size: 20px;                 
            """)


    def send_digits(self):
        current_text = self.user_input_line.text()
        button = self.sender()
        button_text = button.text()
        append_text = current_text + button_text
        self.user_input_line.setText(append_text)

    def split(self):
        self.tokens = []
        number = ""

        line_text = self.user_input_line.text()

        for char in line_text:
            if char.isdigit() or char == ".":
                number += char
            else:
                self.tokens.append(number)
                self.tokens.append(char)
                number = ""
        self.tokens.append(number)

        try:
            self.calc()
        except ValueError:
            self.user_input_line.setText("Value Error")
        except TypeError:
            self.user_input_line.setText("Type Error")
        except AttributeError:
            self.user_input_line.setText("Attribute Error")
        except NameError:
            self.user_input_line.setText("Name Error")
        except ZeroDivisionError:
            self.user_input_line.setText("Zero Division Error")
        except FloatingPointError:
            self.user_input_line.setText("Floating Point Error")
        except OverflowError:
            self.user_input_line.setText("Overflow Error")
        except MemoryError:
            self.user_input_line.setText("Memory Error")
        except Exception as e:
            self.user_input_line.setText(f"{e}")

    def calc(self):
        i = 0
        while i < len(self.tokens):
            if self.tokens[i] == "/":
                divide = float(self.tokens[i - 1]) / float(self.tokens[i + 1])
                self.tokens[i - 1:i + 2] = [str(divide)]
                i = 0
            elif self.tokens[i] == "*":
                multiply = float(self.tokens[i - 1]) * float(self.tokens[i + 1])
                self.tokens[i - 1:i + 2] = [str(multiply)]
                i = 0
            else:
                i += 1

        i = 0
        while i < len(self.tokens):
            if self.tokens[i] == "+":
                add = float(self.tokens[i - 1]) + float(self.tokens[i + 1])
                self.tokens[i - 1:i + 2] = [str(add)]
                i = 0
            elif self.tokens[i] == "-":
                subtract = float(self.tokens[i - 1]) - float(self.tokens[i + 1])
                self.tokens[i - 1:i + 2] = [str(subtract)]
                i = 0
            else:
                i += 1

        self.user_input_line.setText(self.tokens[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
