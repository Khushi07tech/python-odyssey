#Imports
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import(
QAction,
QApplication,
QCheckBox,
QLabel,
QLineEdit,
QMainWindow,
QMessageBox,
QPushButton,
QVBoxLayout,
QWidget
)
import sys
import resources_rc
import re

#Checking validation using Regex
class AuthValidator:
    @staticmethod
    def validate_name(name):
        return re.match (r"^[a-zA-Z\s\-\']{2,30}$", name) is not None

    @staticmethod
    def validate_email(email):
        return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email) is not None

    @staticmethod
    def validate_pwd(password):
        return re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9])\S{7,15}$", password) is not None

#Main Block
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon(":/login_icon.webp"))

        #Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setMinimumWidth(450)
        self.resize(450, 500)

        #Call other functions
        self.init_widgets()
        self.set_layout()
        self.apply_styles()

    #Initialize Widgets (labels, buttons, line edits, checkbox etc)
    def init_widgets(self):
        self.login_label = QLabel("LOGIN")
        self.error_label = QLabel("")
        self.error_label.setWordWrap(True)

        self.name_label = QLabel("Name")
        self.name_line = QLineEdit()
        self.name_line.setPlaceholderText("James Clear")
        self.name_line.setToolTip("•2 to 30 characters\n•Letters, spaces, hyphens, and ' allowed")
        self.name_line.setClearButtonEnabled(True)

        self.email_label = QLabel("Email")
        self.email_line = QLineEdit()
        self.email_line.setPlaceholderText("example@gmail.com")
        self.email_line.setClearButtonEnabled(True)


        self.password_label = QLabel("Password")
        self.password_line = QLineEdit()
        self.password_line.setPlaceholderText("Lilyblossom#23")
        self.password_line.setEchoMode(QLineEdit.Password)
        self.password_line.setToolTip("•7-15 characters\n•Must include:Upper, Lower, Number, & Special (@$!%*?&)")
        self.password_line.setClearButtonEnabled(True)

        self.toggle_pwd = QAction(QIcon(":/eye_icon.jfif"), "", self)
        self.toggle_pwd.setCheckable(True)
        self.password_line.addAction(self.toggle_pwd, QLineEdit.TrailingPosition)
        self.toggle_pwd.toggled.connect(self.toggle_pwd_visibility)


        self.agree_checkbox = QCheckBox("I agree to the terms and services")

        self.submit_button = QPushButton("Submit", self.central_widget)
        self.submit_button.clicked.connect(self.handle_submit)

    #Set the Layout (Vertical)
    def set_layout(self):
        vbox = QVBoxLayout()

        self.login_label.setAlignment(Qt.AlignCenter)
        self.error_label.setAlignment(Qt.AlignCenter)
        self.name_line.setAlignment(Qt.AlignCenter)
        self.email_line.setAlignment(Qt.AlignCenter)
        self.password_line.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.login_label)
        vbox.addWidget(self.error_label)
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.name_line)
        vbox.addWidget(self.email_label)
        vbox.addWidget(self.email_line)
        vbox.addWidget(self.password_label)
        vbox.addWidget(self.password_line)
        vbox.addWidget(self.agree_checkbox)
        vbox.addWidget(self.submit_button)

        self.central_widget.setLayout(vbox)

        vbox.setContentsMargins(40, 40, 40, 40)
        vbox.setSpacing(10)

        vbox.addStretch()

    #Apply a consistent and harmonic style and theme
    def apply_styles(self):
        self.login_label.setObjectName("login_label")
        self.error_label.setObjectName("error_label")
        self.name_label.setObjectName("header")
        self.email_label.setObjectName("header")
        self.password_label.setObjectName("header")

        self.setStyleSheet("""
            QLabel#login_label{
                color: #CC9900;         
                font-family: Quicksand; 
                font-size: 50px;
                font-weight: 600;
                padding: 5px 10px;
            }
            QLabel#error_label{
                font-family: Open Sans;
                font-size: 14px;
                color: #B00020;
            }
            QLabel#header{
                font-weight: bold; 
                color: #5A4A00; 
                font-size: 14px; 
                margin-top: 6px;
            }
            QLineEdit{
                font-size: 20px;
                font-family: Lato;
                background-color: #FFFDF5;
                color: #5A4A00;
                border-radius: 5px;
                border: 2px solid #E6D8A8;
                padding: 2px;
            }
            QLineEdit:focus{
                border: 2px solid #CC9900;
            }
            QLineEdit::placeholder{
                color: #B8A870;
            }
            QPushButton{
                font-size: 23px;
                font-family: Quicksand;
                background-color: #FFF4D6;
                color: #CC9900;
                border-radius: 5px;
                border: 1px solid #7FB8C2;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover{
                background-color: #FFE8A3;
                border-radius: 15px;
                padding: 10px;
            }
            QCheckBox{
                color: #B8A870;
                font-family: Lato;
                font-size: 16px;
            }
        """)

    def toggle_pwd_visibility(self, checked):
        if checked:
            self.password_line.setEchoMode(QLineEdit.Normal)
        else:
            self.password_line.setEchoMode(QLineEdit.Password)

    def handle_submit(self):
        name = self.name_line.text().strip()
        email = self.email_line.text().strip()
        password = self.password_line.text().strip()

        if not name or not email or not password:
            self.error_label.setText("All fields are required")
            return
        if not AuthValidator.validate_name(name):
            self.error_label.setText("Invalid name format\n•2 to 30 characters\n•Letters, spaces, hyphens, and ' allowed")
            return
        if not AuthValidator.validate_email(email):
            self.error_label.setText("Invalid email format")
            return
        if not AuthValidator.validate_pwd(password):
            self.error_label.setText("Invalid Password\n•7-15 characters\n•Must include:Upper, Lower, Number, & Special (@$!%*?&)")
            return
        if not self.agree_checkbox.isChecked():
            self.error_label.setText("Checkbox must be checked")
            return

        self.error_label.setText("")
        self.name_line.clear()
        self.email_line.clear()
        self.password_line.clear()
        self.submit_button.setEnabled(False)
        self.submit_button.setText("Logged in ✓")
        QMessageBox.information(self, "Success", "Login successful")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()