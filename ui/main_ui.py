import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget

from ui.product_ui import Product_form


class mainmenu(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/main.ui")
        self.ui.show()

        self.ui.btn_pro.clicked.connect(self.call_pro)

    def call_pro(self):
        app = QtWidgets.QApplication(sys.argv)
        p = Product_form()
        p.show()

        print('click')