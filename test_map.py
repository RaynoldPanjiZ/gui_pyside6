import io
import sys

import folium
import PySide6


class MainWindow(PySide6.QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.resize(600, 500)
        
        self.browser = PySide6.QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.browser)
        
        self.create_map()
        
    def create_map(self):
        """Create a map of the world and display in browser"""
        
        world_map= folium.Map(tiles="cartodbpositron")
        
        data = io.BytesIO()
        world_map.save(data, close_file=False)
        self.browser.setHtml(data.getvalue().decode())
        
def main():
    app = PySide6.QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    
if __name__ == '__main__':
    main()