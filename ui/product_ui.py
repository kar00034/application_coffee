from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAction
from dao.abs_das import create_table
from dao.product_dao import ProductDao
from dao.sale_dao import SaleDao

class Product_form(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/product.ui")

        pdt = ProductDao()
        res = pdt.select()
        self.load_data(res)

        self.load_data()
        self.table = create_table(table=self.ui.pro_table, data=['code', 'name'])
        self.ui.btn_insert.clicked.connect(self.add_item)
        self.ui.btn_update.clicked.connect(self.update_item)
        self.ui.btn_delete.clicked.connect(self.del_item)
        self.ui.btn_init.clicked.connect(self.init_item)

        # self.ui.sale_btn
        # 마우스 우클릭시 메뉴
        self.set_context_menu(self.ui.pro_table)

        # sale
        # self.sale_table = create_table(table=self.ui.sale_table,
        #                                data=['no', 'code', 'price', 'salecnt', 'marginRate'])
        # self.ui.btn_sale_delete.clicked.connect(self.sale_del_item)
        # self.ui.btn_sale_init.clicked.connect(self.init_item)
        # self.ui.btn_sale_add.clicked.connect(self.sale_add_item)
        # self.ui.btn_sale_update.clicked.connect(self.sale_update_item)
        self.ui.show()

    ###############################sale
    # def sale_load_data(self, data=[]):
    #     self.sale_table.setRowCount(0)
    #     for idx, (no, code, price, salecnt, margin) in enumerate(data):
    #         item_no, item_code, item_price, item_salecnt, item_margin = self.sale_create_item(no, code, price, salecnt,
    #                                                                                           margin)
    #         nextIdx = self.ui.sale_table.rowCount()
    #         self.ui.sale_table.insertRow(nextIdx)
    #         self.ui.sale_table.setItem(nextIdx, 0, item_no)
    #         self.ui.sale_table.setItem(nextIdx, 1, item_code)
    #         self.ui.sale_table.setItem(nextIdx, 2, item_price)
    #         self.ui.sale_table.setItem(nextIdx, 3, item_salecnt)
    #         self.ui.sale_table.setItem(nextIdx, 4, item_margin)
    #
    # def sale_create_item(self, no, code, price, salecnt, marginRate):
    #     item_no = QTableWidgetItem()
    #     item_no.setTextAlignment(Qt.AlignCenter)
    #     item_no.setData(Qt.DisplayRole, no)
    #
    #     item_code = QTableWidgetItem()
    #     item_code.setTextAlignment(Qt.AlignCenter)
    #     item_code.setData(Qt.DisplayRole, code)
    #
    #     item_price = QTableWidgetItem()
    #     item_price.setTextAlignment(Qt.AlignCenter)
    #     item_price.setData(Qt.DisplayRole, price)
    #
    #     item_salecnt = QTableWidgetItem()
    #     item_salecnt.setTextAlignment(Qt.AlignCenter)
    #     item_salecnt.setData(Qt.DisplayRole, salecnt)
    #
    #     item_margin = QTableWidgetItem()
    #     item_margin.setTextAlignment(Qt.AlignCenter)
    #     item_margin.setData(Qt.DisplayRole, marginRate)
    #     SaleDao().select_item()
    #
    #     return item_no, item_code, item_price, item_salecnt, item_margin
    #
    # def sale_get_item_form_le(self):
    #     no = self.ui.sale_table.rowCount()
    #     code = self.ui.le_sale_code.text()
    #     price = self.ui.le_sale_price.text()
    #     marginRate = self.ui.le_sale_marginRate.text()
    #     salecnt = self.ui.le_sale_salecnt.text()
    #
    #     return self.sale_create_item(no,code, price, salecnt, marginRate)
    #
    # def sale_get_item_form_le2(self):
    #     no = self.ui.sale_table.rowCount()
    #     code = self.ui.le_sale_code.text()
    #     price = self.ui.le_sale_price.text()
    #     salecnt = self.ui.le_sale_salecnt.text()
    #     marginRate = self.ui.le_sale_marginRate.text()
    #
    #     return self.sale_create_item(no, code, price, salecnt, marginRate)
    #
    # def sale_del_item(self):
    #     st = SaleDao()
    #     selectionIdxs = self.ui.sale_table.selectedIndexes()[0]
    #     no = self.ui.sale_table.item(selectionIdxs.row(), 0).text()
    #     st.delete_item(no)
    #     self.sale_load_data(st.select_item())
    #
    # def sale_add_item(self):
    #     st = SaleDao()
    #     print(self.ui.le_sale_marginRate.text())
    #     st.insert_item(self.ui.le_sale_code.text(), self.ui.le_sale_price.text(), self.ui.le_sale_salecnt.text(),
    #                    self.ui.le_sale_marginRate.text())
    #     self.init_item()
    #     self.sale_load_data(st.select_item())
    #
    # def sale_update_item(self):
    #     st = SaleDao()
    #     st.update_item(self.ui.le_sale_code.text(), self.ui.le_sale_price.text(), self.ui.le_sale_salecnt.text(), self.ui.le_sale_marginRate.text(), self.ui.le_sale_no.text())
    #
    #     self.init_item()
    #     self.sale_load_data(st.select_item())

    ##########################################pro
    def load_data(self, data=[]):
        for idx, (code, name) in enumerate(data):
            item_code, item_name = self.create_item(code, name)
            nextIdx = self.ui.pro_table.rowCount()
            self.ui.pro_table.insertRow(nextIdx)
            self.ui.pro_table.setItem(nextIdx, 0, item_code)
            self.ui.pro_table.setItem(nextIdx, 1, item_name)

    def create_item(self, code, name):
        item_code = QTableWidgetItem()
        item_code.setTextAlignment(Qt.AlignCenter)
        item_code.setData(Qt.DisplayRole, code)
        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignCenter)
        item_name.setData(Qt.DisplayRole, name)
        return item_code, item_name

    def add_item(self):
        item_code, item_name = self.get_item_form_le()
        currentIdx = self.ui.pro_table.rowCount()
        self.ui.pro_table.insertRow(currentIdx)
        self.ui.pro_table.setItem(currentIdx, 0, item_code)
        self.ui.pro_table.setItem(currentIdx, 1, item_name)
        self.init_item()

    def update_item(self):
        item_code, item_name = self.get_item_form_le2()
        selectionIdxs = self.ui.pro_table.selectedIndexes()[0]
        self.ui.pro_table.setItem(selectionIdxs.row(), 0, item_code)
        self.ui.pro_table.setItem(selectionIdxs.row(), 1, item_name)
        self.init_item()
        self.ui.sale_table.clearSelection()
        QMessageBox.information(self, 'Update', '확인', QMessageBox.Ok)

    def del_item(self):
        pdt = ProductDao()
        selectionIdxs = self.ui.pro_table.selectedIndexes()[0]
        code = self.ui.pro_table.item(selectionIdxs.row(), 0).text()
        pdt.delete_product(code)
        self.ui.pro_table.removeRow(selectionIdxs.row())

    def get_item_form_le(self):
        pdt = ProductDao()
        code = self.ui.le_code.text()
        name = self.ui.le_name.text()
        pdt.insert_product(code, name)
        return self.create_item(code, name)

    def get_item_form_le2(self):
        pdt = ProductDao()
        code = self.ui.le_code.text()
        name = self.ui.le_name.text()
        pdt.update_product(name, code)
        return self.create_item(code, name)

    def __update(self):
        selectionIdxs = self.ui.pro_table.selectedIndexes()[0]
        returnIdxs1 = self.ui.pro_table.item(selectionIdxs.row(), 0).text()
        returnIdxs2 = self.ui.pro_table.item(selectionIdxs.row(), 1).text()
        self.ui.le_code.setText(returnIdxs1)
        self.ui.le_name.setText(returnIdxs2)

    def __delete(self):
        pdt = ProductDao()
        selectionIdxs = self.ui.pro_table.selectedIndexes()[0]
        code = self.ui.pro_table.item(selectionIdxs.row(), 0).text()
        self.ui.pro_table.removeRow(selectionIdxs.row())
        pdt.delete_product(code)
        QMessageBox.information(self, 'Delete', '확인', QMessageBox.Ok)

    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction('수정', tv)
        delete_action = QAction('삭제', tv)
        tv.addAction(update_action)
        tv.addAction(delete_action)
        update_action.triggered.connect(self.__update)
        delete_action.triggered.connect(self.__delete)

    def init_item(self):
        self.ui.le_code.clear()
        self.ui.le_name.clear()
        # self.ui.le_sale_code.clear()
        # self.ui.le_sale_price.clear()
        # self.ui.le_sale_salecnt.clear()
        # self.ui.le_sale_marginRate.clear()
        # self.ui.le_sale_no.clear()
        self.ui.sale_table.clearSelection()
