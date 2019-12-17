from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAction
from dao.abs_das import create_table
from dao.product_dao import ProductDao

class Product_form(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/product.ui")

        pdt = ProductDao()
        res = pdt.select()
        self.load_data(res)

        self.table = create_table(table=self.ui.pro_table, data=['code', 'name'])
        self.ui.btn_insert.clicked.connect(self.add_item)
        self.ui.btn_update.clicked.connect(self.update_item)
        self.ui.btn_delete.clicked.connect(self.del_item)
        self.ui.btn_init.clicked.connect(self.init_item)
        self.ui.btn_update.setEnabled(False)

        # 마우스 우클릭시 메뉴
        self.set_context_menu(self.ui.pro_table)

        self.ui.show()

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
        self.ui.btn_delete.setEnabled(True)
        self.ui.btn_init.setEnabled(True)
        self.ui.btn_insert.setEnabled(True)
        self.ui.btn_update.setEnabled(False)
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

        self.ui.btn_update.setEnabled(True)
        self.ui.btn_delete.setEnabled(False)
        self.ui.btn_init.setEnabled(False)
        self.ui.btn_insert.setEnabled(False)

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
