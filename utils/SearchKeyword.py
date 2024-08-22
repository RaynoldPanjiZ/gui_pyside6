from PySide6 import QtWidgets


class SearchKeyword(QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        QtWidgets.QLineEdit.__init__(self, *args, **kwargs)
        self.multipleCompleter = None

    def keyPressEvent(self, event):
        QtWidgets.QLineEdit.keyPressEvent(self, event)
        if not self.multipleCompleter:
            return
        c = self.multipleCompleter
        if self.text() == "":
            return
        c.setCompletionPrefix(self.cursorWord(self.text()))
        if len(c.completionPrefix()) < 1:
            c.popup().hide()
            return
        c.complete()

    def cursorWord(self, sentence):
        p = sentence.rfind(" ")
        if p == -1:
            return sentence
        return sentence[p + 1:]

    def insertCompletion(self, text):
        p = self.text().rfind(" ")
        if p == -1:
            self.setText(text)
        else:
            self.setText(self.text()[:p+1]+ text)

    def setMultipleCompleter(self, completer):
        self.multipleCompleter = completer
        self.multipleCompleter.setWidget(self)
        completer.activated.connect(self.insertCompletion)