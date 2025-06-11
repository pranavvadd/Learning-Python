import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("AMEX", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)   
        self.radio3.setGeometry(0, 100, 300, 50)

        self.setStyleSheet("QRadioButton{"
                    "font-size: 40px; "
                    "font-family: Arial; "
                    "padding : 10px;"
                    "}")
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group2.addButton(self.radio3)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")
        else:
            print(f"{radio_button.text()} is deselected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Credit Card Selector")
    window.show()
    sys.exit(app.exec_())