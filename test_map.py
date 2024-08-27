import io
import sys

import folium
from PySide6 import QtWidgets
from PySide6.QtWebEngineWidgets import QWebEngineView


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.resize(600, 500)
        
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        
        self.create_map()
        
    def create_map(self):
        """Create a map of the world and display in browser"""
        
        world_map= folium.Map(tiles="cartodbpositron")
        
        data = io.BytesIO()
        world_map.save(data, close_file=False)
        self.browser.setHtml(data.getvalue().decode())
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    
if __name__ == '__main__':
    main()