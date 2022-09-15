from PyQt5.QtWidgets import QMainWindow
from ui.main_window_ui import Ui_LoginForm


class MainWindow(QMainWindow, Ui_LoginForm):

        def __init__(self, parent=None):
            super().__init__(parent)
            self.setupUi(self)
