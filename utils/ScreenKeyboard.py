from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, Signal, QObject

style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()

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



virtual_key = ""
class InputHandler(QObject):
    def __init__(self, keyboard, parent=None):
        super().__init__()
        self.keyboard = keyboard
        self.current_input_widget = None

    def eventFilter(self, source, event):       ## https://stackoverflow.com/questions/66235661/qevent-mousebuttonpress-enum-type-missing-in-pyqt6
        global virtual_key
        # print(event.type())
        if event.type() == event.Type.MouseButtonPress:
            self.current_input_widget = source  # Update focused line edit
            self.keyboard.activateWindow()  
            self.keyboard.raise_()  
            if isinstance(source, QtWidgets.QLineEdit):
                virtual_key = self.current_input_widget.text()
            elif isinstance(source, QtWidgets.QSpinBox):
                virtual_key = str(self.current_input_widget.value())
            elif isinstance(source, QtWidgets.QTextEdit):
                virtual_key = self.current_input_widget.textCursor()
        # return super().eventFilter(source, event)
        return False

    def on_key_pressed(self, key):
        global virtual_key
        if self.current_input_widget is not None:
            if isinstance(self.current_input_widget, QtWidgets.QLineEdit):
                if key == '': 
                    virtual_key += ' '
                elif key == '←': 
                    virtual_key = virtual_key[:-1]
                elif key == 'ENTER':
                    pass
                else:
                    virtual_key += key
                # print(virtual_key)
                self.keyboard.w.edit_text.setText(virtual_key)
                self.current_input_widget.setText(virtual_key)
            elif isinstance(self.current_input_widget, QtWidgets.QSpinBox):
                if key.isdigit():
                    new_key = virtual_key + key if virtual_key != "0" else key
                    # new_key = str(virtual_key) + str(key)
                    virtual_key = new_key if int(virtual_key) < int(self.current_input_widget.maximum()) else virtual_key
                elif key == "←":
                    print(int(virtual_key), ">", int(self.current_input_widget.minimum()))
                    virtual_key = virtual_key[:-1] if len(str(virtual_key)) > 1 else "0"
                elif key == 'ENTER': 
                    pass
                elif key == '': 
                    pass
                print(virtual_key)
                self.keyboard.w.edit_text.setText(virtual_key)
                self.current_input_widget.setValue(int(virtual_key))
