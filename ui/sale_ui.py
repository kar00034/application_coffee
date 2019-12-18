from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QAction, QMessageBox

from dao.sale_dao import SaleDao
from ui.table import create_table


class Sale_form(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/sale.ui")

        st = SaleDao()
        res2 = st.select_item()
        self.sale_load_data(res2)

        self.sale_table = create_table(table=self.ui.sale_table,
                                       data=['no', 'code', 'price', 'salecnt', 'marginRate'])
        self.ui.btn_sale_delete.clicked.connect(self.sale_del_item)
        self.ui.btn_sale_init.clicked.connect(self.init_item)
        self.ui.btn_sale_add.clicked.connect(self.sale_add_item)
        self.ui.btn_sale_update.clicked.connect(self.sale_update_item)
        self.ui.btn_exit.clicked.connect(self.call_exit)

        # 마우스 우클릭시 메뉴
        self.set_context_menu(self.ui.sale_table)

        self.ui.show()

    def sale_load_data(self, data=[]):
        self.ui.sale_table.setRowCount(0)
        for idx, (no, code, price, salecnt, margin) in enumerate(data):
            item_no, item_code, item_price, item_salecnt, item_margin = self.sale_create_item(no, code, price, salecnt,
                                                                                              margin)
            nextIdx = self.ui.sale_table.rowCount()
            self.ui.sale_table.insertRow(nextIdx)
            self.ui.sale_table.setItem(nextIdx, 0, item_no)
            self.ui.sale_table.setItem(nextIdx, 1, item_code)
            self.ui.sale_table.setItem(nextIdx, 2, item_price)
            self.ui.sale_table.setItem(nextIdx, 3, item_salecnt)
            self.ui.sale_table.setItem(nextIdx, 4, item_margin)

    def sale_create_item(self, no, code, price, salecnt, marginRate):
        item_no = QTableWidgetItem()
        item_no.setTextAlignment(Qt.AlignHCenter)
        item_no.setData(Qt.DisplayRole, no)

        item_code = QTableWidgetItem()
        item_code.setTextAlignment(Qt.AlignHCenter)
        item_code.setData(Qt.DisplayRole, code)

        item_price = QTableWidgetItem()
        item_price.setTextAlignment(Qt.AlignRight)
        item_price.setData(Qt.DisplayRole, format(int(price), ',d'))

        item_salecnt = QTableWidgetItem()
        item_salecnt.setTextAlignment(Qt.AlignRight)
        item_salecnt.setData(Qt.DisplayRole, salecnt)

        item_margin = QTableWidgetItem()
        item_margin.setTextAlignment(Qt.AlignRight)
        item_margin.setData(Qt.DisplayRole, str(marginRate)+'%')
        SaleDao().select_item()

        return item_no, item_code, item_price, item_salecnt, item_margin

    def sale_del_item(self):
        st = SaleDao()
        selectionIdxs = self.ui.sale_table.selectedIndexes()[0]
        no = self.ui.sale_table.item(selectionIdxs.row(), 0).text()
        st.delete_item(no)
        self.sale_load_data(st.select_item())
        QMessageBox.information(self, 'Delete', '확인', QMessageBox.Ok)

    def sale_add_item(self):
        st = SaleDao()
        st.insert_item(self.ui.le_sale_code.text(), self.ui.le_sale_price.text(), self.ui.le_sale_salecnt.text(),
                       self.ui.le_sale_marginRate.text())
        self.init_item()
        self.sale_load_data(st.select_item())

    def sale_update_item(self):
        st = SaleDao()
        st.update_item(self.ui.le_sale_code.text(), self.ui.le_sale_price.text(), self.ui.le_sale_salecnt.text(), self.ui.le_sale_marginRate.text(), self.ui.le_sale_no.text())

        self.init_item()
        self.sale_load_data(st.select_item())

        self.ui.btn_sale_update.setEnabled(False)
        self.ui.btn_sale_add.setEnabled(True)
        self.ui.btn_sale_delete.setEnabled(True)
        self.ui.btn_sale_init.setEnabled(True)

    def init_item(self):
        self.ui.le_sale_code.clear()
        self.ui.le_sale_price.clear()
        self.ui.le_sale_salecnt.clear()
        self.ui.le_sale_marginRate.clear()
        self.ui.le_sale_no.clear()
        self.ui.sale_table.clearSelection()

    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction('수정', tv)
        tv.addAction(update_action)
        update_action.triggered.connect(self.__update)

    #업데이트 비활성화
    def __update(self):
        selectionIdxs = self.ui.sale_table.selectedIndexes()[0]
        self.ui.le_sale_no.setText(self.ui.sale_table.item(selectionIdxs.row(), 0).text())
        self.ui.le_sale_code.setText(self.ui.sale_table.item(selectionIdxs.row(), 1).text())
        self.ui.le_sale_price.setText(self.ui.sale_table.item(selectionIdxs.row(), 2).text())
        self.ui.le_sale_salecnt.setText(self.ui.sale_table.item(selectionIdxs.row(), 3).text())
        self.ui.le_sale_marginRate.setText(self.ui.sale_table.item(selectionIdxs.row(), 4).text())

        self.ui.btn_sale_update.setEnabled(True)
        self.ui.btn_sale_add.setEnabled(False)
        self.ui.btn_sale_delete.setEnabled(False)
        self.ui.btn_sale_init.setEnabled(False)

    def call_exit(self):
        self.ui.close()
