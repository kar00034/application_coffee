from PyQt5 import uic
from PyQt5.QtWidgets import *

from ui.product_ui import Product_form
from ui.sale_detail_ui import Sale_Detail_form
from ui.sale_ui import Sale_form


class mainmenu(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/main.ui")

        self.ui.btn_pro.clicked.connect(self.call_pro)
        self.ui.btn_sale.clicked.connect(self.call_sale)
        self.ui.btn_sale_d.clicked.connect(self.call_sale_d)

        self.ui.show()

    def call_pro(self):
        self.pf = Product_form()

    def call_sale(self):
        self.sale = Sale_form()

    def call_sale_d(self):
        self.sale_d = Sale_Detail_form()