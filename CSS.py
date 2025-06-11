import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.button3 = QPushButton("Button 3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        # Set ObjectName for all buttons
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # Apply CSS styles to buttons
        self.setStyleSheet("""
            QPushButton{ 
                    font-size: 40px;
                    font-family: Arial;
                    padding: 15px 75px;
                    margin: 25px;
                    border: 3px solid;
                    border-radius: 15px;
                }
                QPushButton#button1{
                    background-color: #ff0000; /* Red */
                }
                QPushButton#button2{
                    background-color: green;
                }
                QPushButton#button3{
                    background-color: blue;
                }          
            """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("CSS Example")
    window.show()
    sys.exit(app.exec_())