import math
import sys
import re
from mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QListWidgetItem
from PySide6.QtCore import Slot, Signal

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow() 
    window.show()
    sys.exit(app.exec())
    


