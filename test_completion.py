import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QTextEdit, QSpinBox, QVBoxLayout, QPushButton, QGridLayout
from PySide6.QtCore import Signal, Qt, QObject


class VirtualKeyboard(QWidget):
    key_pressed = Signal(str)  # Signal to emit the key pressed

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Virtual Keyboard")

        # Create layout
        layout = QGridLayout()

        # Define buttons for the virtual keyboard
        buttons = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M',
            'Space', 'Backspace'
        ]

        # Add buttons to layout
        for i, button in enumerate(buttons):
            if button == "Space":
                btn = QPushButton(" ")
                btn.clicked.connect(lambda _, b=button: self.on_button_click(b))
                layout.addWidget(btn, 4, 0, 1, 10)
            elif button == "Backspace":
                btn = QPushButton("Backspace")
                btn.clicked.connect(lambda _, b=button: self.on_button_click(b))
                layout.addWidget(btn, 5, 8, 1, 2)
            else:
                btn = QPushButton(button)
                btn.clicked.connect(lambda _, b=button: self.on_button_click(b))
                row, col = divmod(i, 10)
                layout.addWidget(btn, row, col)

        self.setLayout(layout)

    def on_button_click(self, button_text):
        # Emit signal with the button text
        if button_text == "Backspace":
            self.key_pressed.emit("\b")  # Send backspace signal
        elif button_text == "Space":
            self.key_pressed.emit(" ")  # Send space signal
        else:
            self.key_pressed.emit(button_text)


class InputHandler(QObject):
    def __init__(self, keyboard, parent=None):
        super().__init__()
        self.keyboard = keyboard
        self.current_input_widget = None

    def eventFilter(self, source, event):
        if event.type() == event.Type.MouseButtonPress:
            if isinstance(source, (QLineEdit, QTextEdit, QSpinBox)):
                self.current_input_widget = source  # Update focused widget
                self.keyboard.activateWindow()  # Bring keyboard to the front
                self.keyboard.raise_()  # Make sure it's on top
        return False  # Ensure other events proceed as usual

    def on_key_pressed(self, key):
        # Handle key press and update the currently focused input widget
        if self.current_input_widget:
            if isinstance(self.current_input_widget, QLineEdit):
                current_text = self.current_input_widget.text()
                if key == "\b":  # Backspace
                    current_text = current_text[:-1]
                else:
                    current_text += key
                self.current_input_widget.setText(current_text)

            elif isinstance(self.current_input_widget, QTextEdit):
                if key == "\b":  # Backspace
                    cursor = self.current_input_widget.textCursor()
                    cursor.deletePreviousChar()
                else:
                    self.current_input_widget.insertPlainText(key)

            elif isinstance(self.current_input_widget, QSpinBox):
                # Handle numeric input for QSpinBox
                if key.isdigit():
                    current_value = str(self.current_input_widget.value())
                    new_value = current_value + key if current_value != "0" else key
                    self.current_input_widget.setValue(int(new_value))
                elif key == "\b":
                    current_value = str(self.current_input_widget.value())
                    new_value = current_value[:-1] if len(current_value) > 1 else "0"
                    self.current_input_widget.setValue(int(new_value))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Form")

        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create layout
        layout = QVBoxLayout()

        # Create multiple input widgets
        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit3 = QLineEdit()
        self.text_edit = QTextEdit()
        self.spin_box = QSpinBox()

        layout.addWidget(self.line_edit1)
        layout.addWidget(self.line_edit2)
        layout.addWidget(self.line_edit3)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.spin_box)

        central_widget.setLayout(layout)

        # Create an instance of the virtual keyboard
        self.keyboard = VirtualKeyboard()
        self.keyboard.show()  # Show the keyboard window

        # Create InputHandler
        self.input_handler = InputHandler(self.keyboard)

        # Connect the keyboard signal to the handler
        self.keyboard.key_pressed.connect(self.input_handler.on_key_pressed)

        # Install event filters for all input widgets
        self.line_edit1.installEventFilter(self.input_handler)
        self.line_edit2.installEventFilter(self.input_handler)
        self.line_edit3.installEventFilter(self.input_handler)
        self.text_edit.installEventFilter(self.input_handler)
        self.spin_box.installEventFilter(self.input_handler)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the main window and show it
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
