import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import QSize

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('PyQt6 Simple Window')

        # Set fixed size of the window to 500x500
        self.setFixedSize(QSize(500, 500))

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add a button to the layout
        button = QPushButton('Click Me')
        layout.addWidget(button)

        # Set the layout to the window
        self.setLayout(layout)

# Main function
def main():
    app = QApplication(sys.argv)

    # Create an instance of the window
    window = SimpleWindow()

    # Show the window
    window.show()

    # Execute the application
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
