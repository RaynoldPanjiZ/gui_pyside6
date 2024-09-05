from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, Signal

# print(os.getcwd())
style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()



# loader = QUiLoader()
# ui_file = QFile("ui/admgui/all_ui/keyboard.ui")
# if not ui_file.open(QIODevice.ReadOnly):
#     print(f"Cannot open UI file: {ui_file.errorString()}")
# ui = loader.load(ui_file)
# ui_file.close()

class ScreenKeyboard2(QtWidgets.QWidget):
    key_pressed = Signal(str)  # Signal to emit the key pressed

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Virtual Keyboard")

        # Create layout
        layout = QtWidgets.QGridLayout()

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
                btn = QtWidgets.QPushButton(" ")
                btn.clicked.connect(lambda _, b=button: self.on_button_click(b))
                layout.addWidget(btn, 4, 0, 1, 10)
            elif button == "Backspace":
                btn = QtWidgets.QPushButton("Backspace")
                btn.clicked.connect(lambda _, b=button: self.on_button_click(b))
                layout.addWidget(btn, 5, 8, 1, 2)
            else:
                btn = QtWidgets.QPushButton(button)
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


class ScreenKeyboard(QtWidgets.QMainWindow):
    key_pressed = Signal(str)
    def __init__(self, w):
        super().__init__()
        # QtWidgets.QWidget.__init__(self, parent, Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        # self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowTitleHint \
        #                     | Qt.WindowType.WindowMaximizeButtonHint | \
        #                         Qt.WindowType.WindowMinimizeButtonHint | \
        #                             Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.Window)
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("Screen Keyboard")
        self.setStyleSheet(style)
        # self.btn_grp_num = QtWidgets.QButtonGroup()
        # self.btn_grp_alpha = QtWidgets.QButtonGroup()
        # self.btn_grp_char = QtWidgets.QButtonGroup()
        self.btn_groups = QtWidgets.QButtonGroup()
        self.num_buttons = []
        self.alpha_buttons = []
        self.key_buttons = []
        self.make_btn_grp()

        self.upper = False
        self.w.btn_upper.clicked.connect(self.btn_upper_clicked)

        # self.show()

    def make_btn_grp(self):
        self.num_buttons = [self.w.num_layout.itemAt(i).widget() for i in range(self.w.num_layout.count())]
        # for i, btn in enumerate(self.num_buttons):
        #     self.btn_grp_num.addButton(btn)
        
        alpha1 = [self.w.alpha_layout_1.itemAt(i).widget() for i in range(self.w.alpha_layout_1.count())]
        alpha2 = [self.w.alpha_layout_2.itemAt(i).widget() for i in range(self.w.alpha_layout_2.count())]
        alpha3 = [self.w.alpha_layout_3.itemAt(i).widget() for i in range(self.w.alpha_layout_3.count())]
        self.alpha_buttons = alpha1
        self.alpha_buttons.extend(alpha2)
        self.alpha_buttons.extend(alpha3)
        # for i, btn in enumerate(self.alpha_buttons):
        #     self.btn_grp_alpha.addButton(btn)
        
        self.char_buttons = [self.w.char_layout.itemAt(i).widget() for i in range(self.w.char_layout.count())]
        # for i, btn in enumerate(self.char_buttons):
        #     self.btn_grp_char.addButton(btn)

        self.key_buttons = self.num_buttons + self.alpha_buttons + self.char_buttons
        for i, btn in enumerate(self.key_buttons):
            if btn.text() == "CapsLk": continue
            # self.btn_groups.addButton(btn)
            btn.clicked.connect(lambda _, b=btn.text(): self.on_button_click(b))
            # self.key_pressed.emit(btn.text())

    def btn_upper_clicked(self):
        self.upper = not self.upper
        if self.upper:
            # self.btn_upper.setStyleSheet(UPPER)
            for btn in self.alpha_buttons:
                btn.setText(btn.text().upper())
                # self.key_pressed.emit(btn.text().upper())
        else:
            # self.btn_upper.setStyleSheet(LOWER)
            for btn in self.alpha_buttons:
                btn.setText(btn.text().lower())
                # self.key_pressed.emit(btn.text().lower())


    def on_button_click(self, button_text):
        # Emit signal with the button text
        if button_text == "←":
            self.key_pressed.emit("←")  # Send backspace signal
        elif button_text == "":
            self.key_pressed.emit(" ")  # Send space signal
        else:
            self.key_pressed.emit(button_text)