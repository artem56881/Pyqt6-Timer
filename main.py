import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timer Example")
        self.setGeometry(100, 100, 300, 200)

        # Create central widget and set it as the central widget of the window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout()

        # Create a label to display the elapsed time
        self.time_label = QLabel("Time: 0 seconds")
        layout.addWidget(self.time_label)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

        # Initialize the timer
        self.elapsed_time = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

    def update_time(self):
        self.elapsed_time += 1
        self.time_label.setText(f"Time: {self.elapsed_time} seconds")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
