key_widget = None
keyboard_active = False

def key_widget_func(arg):
    global key_widget
    key_widget = arg

def keyboard_active_func(arg: bool):
    global keyboard_active
    keyboard_active = arg