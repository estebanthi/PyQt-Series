import sys

from PyQt5.QtWidgets import QApplication

from main_window import MainWindow


class App:

    def __init__(self):
        qapp = QApplication(sys.argv)

        window = MainWindow()

        window.show()
        sys.exit(qapp.exec())


if __name__ == '__main__':
    app = App()
