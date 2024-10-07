# from PySide6 import QtWidgets
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtCore import QFile, QIODevice, Qt, Signal, QObject, QPoint
# from utils import UtilsVariables
# from PySide6.QtGui import QScreen

import PySide6
# import PySide6.QtWidgets

style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()
# qmainwindow = PySide6.QtWidgets.QMainWindow
class ScreenKeyboard(PySide6.QtWidgets.QMainWindow):
    key_pressed = PySide6.QtCore.Signal(str)
    def __init__(self, w, mainwindow):
        super().__init__()
        self.setCentralWidget(w)
        self.setParent(mainwindow.w)

        # # PySide6.QtWidgets.QWidget.__init__(self, parent, PySide6.QtCore.Qt.WindowType.WindowStaysOnTopHint)
        # self.setWindowFlags(PySide6.QtCore.Qt.WindowType.WindowStaysOnTopHint)
        # self.setAttribute(PySide6.QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        # # self.setWindowFlags(self.windowFlags() | PySide6.QtCore.Qt.WindowType.WindowTitleHint \
        # #                     | PySide6.QtCore.Qt.WindowType.WindowMaximizeButtonHint | \
        # #                         PySide6.QtCore.Qt.WindowType.WindowMinimizeButtonHint | \
        # #                             PySide6.QtCore.Qt.WindowType.WindowCloseButtonHint | PySide6.QtCore.Qt.WindowType.Window)
        self.w = w
        # self.setGeometry(100, 60, 60, 60) 
        self.setWindowTitle("Screen Keyboard")
        self.setStyleSheet(style)
        self.w.btn_upper.clicked.connect(self.btn_upper_clicked)
        # self.move_to_center()
        
        self.btn_groups = PySide6.QtWidgets.QButtonGroup()
        self.num_buttons = []
        self.alpha_buttons = []
        self.key_buttons = []
        self.make_btn_grp()

        self.caps_key = []
        self.upper = False



    def make_btn_grp(self):
        self.num_buttons = [self.w.num_layout.itemAt(i).widget() for i in range(self.w.num_layout.count())]
        alpha1 = [self.w.alpha_layout_1.itemAt(i).widget() for i in range(self.w.alpha_layout_1.count())]
        alpha2 = [self.w.alpha_layout_2.itemAt(i).widget() for i in range(self.w.alpha_layout_2.count())]
        alpha3 = [self.w.alpha_layout_3.itemAt(i).widget() for i in range(self.w.alpha_layout_3.count())]
        self.alpha_buttons = alpha1
        self.alpha_buttons.extend(alpha2)
        self.alpha_buttons.extend(alpha3)
        
        self.char_buttons = [self.w.char_layout.itemAt(i).widget() for i in range(self.w.char_layout.count())]

        self.key_buttons = self.num_buttons + self.alpha_buttons + self.char_buttons
        for i, btn in enumerate(self.key_buttons):
            btn.clicked.connect(lambda _, b=btn: self.on_button_click(b))

    def btn_upper_clicked(self):
        self.upper = not self.upper
        if self.upper:
            # self.btn_upper.setStyleSheet(UPPER)
            for btn in self.alpha_buttons:
                k = btn.text().upper()
                btn.setText(k)
                self.caps_key.append(k)
        else:
            # self.btn_upper.setStyleSheet(LOWER)
            for btn in self.alpha_buttons:
                k = btn.text().lower()
                btn.setText(k)
                self.caps_key.append(k)


    def on_button_click(self, buttons):
        # Emit signal with the button text
        button_text = buttons.text()
        if button_text == "CapsLk": 
            pass
        elif button_text == "←":
            self.key_pressed.emit("←")  # Send backspace signal
        elif button_text == "":
            self.key_pressed.emit(" ")  # Send space signal
        else:
            self.key_pressed.emit(button_text)
    
    def move_to_center(self):
        # screen_geometry = PySide6.QtWidgets.QApplication.primaryScreen().geometry()
        screen_geometry = self.screen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        keyboard_size = self.sizeHint()
        keyboard_width = keyboard_size.width()
        keyboard_height = keyboard_size.height()

        x = (screen_width - keyboard_width) // 2
        y = (screen_height - keyboard_height) // 2

        self.move(0, 0)



class InputHandler(PySide6.QtCore.QObject):
    virtual_key = ""
    def __init__(self, keyboard, parent=None):
        super().__init__()
        self.keyboard = keyboard
        self.current_input_widget = None
        self.cursor_position = ""
        # self.showed = False
        self.cursor_inwg = False

    def eventFilter(self, source, event):       ## https://stackoverflow.com/questions/66235661/qevent-mousebuttonpress-enum-type-missing-in-pyqt6
        # print(event.type())
        
        # if event.type() == event.Type.MouseButtonPress:
        if event.type() == event.Type.Paint:
            self.current_input_widget = source  # Update focused line edit
            self.keyboard.activateWindow()  
            self.keyboard.raise_()  
            if isinstance(source, PySide6.QtWidgets.QLineEdit):
                self.virtual_key = self.current_input_widget.text()
            elif isinstance(source, PySide6.QtWidgets.QSpinBox):
                self.virtual_key = str(self.current_input_widget.value())
            elif isinstance(source, PySide6.QtWidgets.QTextEdit):
                self.virtual_key = self.current_input_widget.toPlainText()
            elif isinstance(source, PySide6.QtWidgets.QDateEdit):
                self.cursor_position = self.current_input_widget.lineEdit().cursorPosition()
                self.virtual_key = self.current_input_widget.text()
                # print(self.virtual_key)
                print(self.cursor_position)
                # self.virtual_key = self.current_input_widget.date().toString("yyyy-MM-dd")
            elif isinstance(source, PySide6.QtWidgets.QTimeEdit):
                self.cursor_position = self.current_input_widget.lineEdit().cursorPosition()
                self.virtual_key = self.current_input_widget.text()
                # print(self.virtual_key)
                print(self.cursor_position)
                # self.virtual_key = self.current_input_widget.time().toString("HH:mm:ss AP")
        # print(self.keyboard.isActiveWindow())
        if self.current_input_widget is not None and event.type() == event.Type.MouseButtonPress:
        # event.Type.FocusIn and self.current_input_widget is not None and self.cursor_inwg is False :
            if self.cursor_inwg is False: 
                # PySide6.QtCore.Qt.WindowType.SubWindow |
                self.keyboard.setWindowFlags( PySide6.QtCore.Qt.WindowType.WindowStaysOnTopHint | PySide6.QtCore.Qt.WindowType.Tool)
                
                print("keyboard on top")

                keyboard_width = 560
                keyboard_height = 220
                keyboard_posx = (PySide6.QtGui.QScreen.availableGeometry(PySide6.QtWidgets.QApplication.primaryScreen()).width()  // 2 ) - (keyboard_width // 2)
                keyboard_posy = (PySide6.QtGui.QScreen.availableGeometry(PySide6.QtWidgets.QApplication.primaryScreen()).height()) - (keyboard_height + 15)
                self.keyboard.setGeometry(keyboard_posx, keyboard_posy, keyboard_width, keyboard_height) 
                self.keyboard.move(keyboard_posx, keyboard_posy)
                
                # pos = self.keyboard.pos()
                # pos.setX(keyboard_posx)
                # pos.setY(keyboard_posy)
                # self.keyboard.move(pos)

                
                self.keyboard.show()
        return False

    def on_key_pressed(self, key):
        if self.current_input_widget is not None:
            if isinstance(self.current_input_widget, PySide6.QtWidgets.QLineEdit):
                if key == '': 
                    self.virtual_key += ' '
                elif key == '←': 
                    self.virtual_key = self.virtual_key[:-1]
                elif key == 'ENTER':
                    pass
                else:
                    self.virtual_key += key
                # print(self.virtual_key)
                self.keyboard.w.edit_text.setText(self.virtual_key)
                self.current_input_widget.setText(self.virtual_key)
            elif isinstance(self.current_input_widget, PySide6.QtWidgets.QSpinBox):
                if key.isdigit():
                    new_key = self.virtual_key + key if self.virtual_key != "0" else key
                    # new_key = str(self.virtual_key) + str(key)
                    self.virtual_key = new_key if int(self.virtual_key) < int(self.current_input_widget.maximum()) else self.virtual_key
                elif key == "←":
                    print(int(self.virtual_key), ">", int(self.current_input_widget.minimum()))
                    self.virtual_key = self.virtual_key[:-1] if len(str(self.virtual_key)) > 1 else "0"
                elif key == 'ENTER': 
                    pass
                elif key == '': 
                    pass
                else:
                    self.virtual_key += ''
                # print(self.virtual_key)
                self.keyboard.w.edit_text.setText(self.virtual_key)
                self.current_input_widget.setValue(int(self.virtual_key))
            elif isinstance(self.current_input_widget, PySide6.QtWidgets.QTextEdit):
                if key == '': 
                    self.virtual_key += ' '
                elif key == "←": # Backspace
                    self.virtual_key = self.virtual_key[:-1]
                elif key == 'ENTER':
                    self.virtual_key += '\n'
                else:
                    self.virtual_key += key
                self.keyboard.w.edit_text.setText(self.virtual_key)
                self.current_input_widget.setPlainText(self.virtual_key)
            elif isinstance(self.current_input_widget, PySide6.QtWidgets.QDateEdit):
                # Handle numeric input for QDateEdit
                datepart = self.virtual_key.split('-')
                print(datepart)
                new_year, new_month, new_day = datepart[0], datepart[1], datepart[2]
                if key.isdigit():
                    if self.cursor_position <= 4:
                        print(self.virtual_key)
                        if len(str(datepart[0])) > 4:
                            new_year = datepart[0]
                        else:
                            new_year = datepart[0] + key
                    elif 5 <= self.cursor_position <= 7:
                        if len(str(datepart[1])) > 2:
                            new_month = datepart[1]
                        else:
                            new_month = datepart[1] + key
                    elif 8 <= self.cursor_position <= 10:
                        if len(str(datepart[2])) > 2:
                            new_day = datepart[2]
                        else:
                            new_day = datepart[2] + key
                    # new_text = self.virtual_key + key
                    self.virtual_key = f"{new_year}-{new_month}-{new_day}"
                elif key == "←":                    
                    if self.cursor_position <= 4:
                        if len(str(datepart[0])) <= 0:
                            new_year = '1'
                        else:
                            new_year = datepart[0][:-1]
                    elif 5 <= self.cursor_position <= 7:
                        if len(str(datepart[1])) <= 0:
                            new_month = '1'
                        else:
                            new_month = datepart[1][:-1]
                    elif 8 <= self.cursor_position <= 10:
                        if len(str(datepart[2])) <= 0:
                            new_day = '1'
                        else:
                            new_day = datepart[2][:-1]
                    self.virtual_key = f"{new_year}-{new_month}-{new_day}"
                    pass  
                elif key == 'ENTER': 
                    pass
                elif key == '': 
                    pass
                self.keyboard.w.edit_text.setText(self.virtual_key)
                self.current_input_widget.setDate(self.current_input_widget.date().fromString(self.virtual_key, "yyyy-MM-dd"))
            elif isinstance(self.current_input_widget, PySide6.QtWidgets.QTimeEdit):
                # Handle numeric input for QTimeEdit
                timepart = self.virtual_key.split(':')
                new_hour, new_minute, new_second = timepart
                new_second, ap = new_second.split(" ")
                print(new_hour, new_minute, new_second, ap)
                if key.isdigit():
                    if self.cursor_position <= 2:
                        print(self.virtual_key)
                        if len(str(new_hour)) > 2:
                            new_hour = new_hour
                        else:
                            new_hour = new_hour + key
                    elif 3 <= self.cursor_position <= 5:
                        if len(str(new_minute)) > 2:
                            new_minute = new_minute
                        else:
                            new_minute = new_minute + key
                    elif 6 <= self.cursor_position <= 8:
                        if len(str(new_second)) > 2:
                            new_second = new_second
                        else:
                            new_second = new_second + key
                    # new_text = self.virtual_key + key
                    self.virtual_key = f"{new_hour}:{new_minute}:{new_second} {ap}"
                # elif key.isalpha():
                #     if 9 <= self.cursor_position <= 11:
                #         if len(str(ap)) > 2:
                #             ap = ap
                #         else:
                #             ap = ap + key
                elif key == "←":
                    if self.cursor_position <= 4:
                        if len(str(new_hour)) <= 0:
                            new_hour = '1'
                        else:
                            new_hour = new_hour[:-1]
                    elif 3 <= self.cursor_position <= 5:
                        if len(str(new_hour)) <= 0:
                            new_minute = '1'
                        else:
                            new_minute = new_hour[:-1]
                    elif 6 <= self.cursor_position <= 8:
                        if len(str(new_second)) <= 0:
                            new_second = '1'
                        else:
                            new_second = new_second[:-1]
                    self.virtual_key = f"{new_hour}:{new_minute}:{new_second} {ap}"
                    pass  
                elif key == 'ENTER': 
                    pass
                elif key == '': 
                    pass
                self.keyboard.w.edit_text.setText(self.virtual_key)
                self.current_input_widget.setTime(self.current_input_widget.time().fromString(self.virtual_key, "HH:mm:ss AP"))
                
