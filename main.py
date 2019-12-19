from PyQt5.QtWidgets import QApplication

from ui.mainmenu_ui import mainmenu

if __name__ == '__main__':
    app = QApplication([])
    w = mainmenu()
    app.exec_()