from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from dao.sale_detail_dao import SaleDetailDao
from ui.table import create_table


class Sale_Detail_form(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/sale_detail.ui")

        self.sd_table = create_table(table=self.ui.sd_table,
                                     data=['rank', 'code', 'name', 'price', 'salecnt', 'supply_price', 'addtax',
                                           'sale_price',
                                           'marginrate(%)', 'marginprice'])

        self.ui.rb_margin.pressed.connect(self.margin_rank)
        self.ui.rb_sale.pressed.connect(self.sale_rank)
        self.ui.btn_exit.clicked.connect(self.call_exit)
        self.ui.show()

    def saledetail_load_data(self, rank):
        sd = SaleDetailDao()
        res = sd.select_item(rank)
        self.ui.sd_table.setRowCount(0)
        for idx, (
                rank, code, name, price, salecnt, supply_price, addtax, sale_price, marginrate,
                marginprice) in enumerate(res):
            item_code, item_name, item_price, item_salecnt, item_supply_price, item_addtax, item_sale_price, item_marginrate, item_marginprice, item_rank = self.saledetail_create_item(
                code, name, price, salecnt, supply_price, addtax, sale_price, marginrate, marginprice, rank)
            nextIdx = self.ui.sd_table.rowCount()
            self.ui.sd_table.insertRow(nextIdx)
            self.ui.sd_table.setItem(nextIdx, 0, item_rank)
            self.ui.sd_table.setItem(nextIdx, 1, item_code)
            self.ui.sd_table.setItem(nextIdx, 2, item_name)
            self.ui.sd_table.setItem(nextIdx, 3, item_price)
            self.ui.sd_table.setItem(nextIdx, 4, item_salecnt)
            self.ui.sd_table.setItem(nextIdx, 5, item_supply_price)
            self.ui.sd_table.setItem(nextIdx, 6, item_addtax)
            self.ui.sd_table.setItem(nextIdx, 7, item_sale_price)
            self.ui.sd_table.setItem(nextIdx, 8, item_marginrate)
            self.ui.sd_table.setItem(nextIdx, 9, item_marginprice)

    def saledetail_create_item(self, code, name, price, salecnt, supply_price, addtax, sale_price, marginrate,
                               marginprice, rank):
        item_rank = QTableWidgetItem()
        item_rank.setTextAlignment(Qt.AlignHCenter)
        item_rank.setData(Qt.DisplayRole, rank)

        item_code = QTableWidgetItem()
        item_code.setTextAlignment(Qt.AlignHCenter)
        item_code.setData(Qt.DisplayRole, code)

        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignHCenter)
        item_name.setData(Qt.DisplayRole, name)

        item_price = QTableWidgetItem()
        item_price.setTextAlignment(Qt.AlignRight)
        item_price.setData(Qt.DisplayRole, format(int(price), ',d'))

        item_salecnt = QTableWidgetItem()
        item_salecnt.setTextAlignment(Qt.AlignRight)
        item_salecnt.setData(Qt.DisplayRole, salecnt)

        item_supply_price = QTableWidgetItem()
        item_supply_price.setTextAlignment(Qt.AlignRight)
        item_supply_price.setData(Qt.DisplayRole, format(int(supply_price), ',d'))

        item_addtax = QTableWidgetItem()
        item_addtax.setTextAlignment(Qt.AlignRight)
        item_addtax.setData(Qt.DisplayRole, format(int(addtax), ',d'))

        item_sale_price = QTableWidgetItem()
        item_sale_price.setTextAlignment(Qt.AlignRight)
        item_sale_price.setData(Qt.DisplayRole, format(int(sale_price), ',d'))

        item_marginrate = QTableWidgetItem()
        item_marginrate.setTextAlignment(Qt.AlignRight)
        item_marginrate.setData(Qt.DisplayRole, marginrate)

        item_marginprice = QTableWidgetItem()
        item_marginprice.setTextAlignment(Qt.AlignRight)
        item_marginprice.setData(Qt.DisplayRole, format(int(marginprice), ',d'))

        return item_code, item_name, item_price, item_salecnt, item_supply_price, item_addtax, item_sale_price, item_marginrate, item_marginprice, item_rank

    def margin_rank(self):
        self.saledetail_load_data(False)

    def sale_rank(self):
        self.saledetail_load_data(True)

    def call_exit(self):
        self.ui.close()
