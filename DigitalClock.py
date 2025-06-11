import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("12:00:00", self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(600, 400, 600, 200)  # Adjusted size for better visibility

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: #26ff00;"
                                      "font-family: 'Courier New', Courier, monospace;")
        self.setStyleSheet("background-color: black;")

        self.timer = QTimer(self)  # Ensure the timer is initialized
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second
        self.update_time()
    
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss A")  # Corrected format
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())