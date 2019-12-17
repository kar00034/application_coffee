import sys
from PyQt5 import QtWidgets
from dao.product_dao import ProductDao
from dao.sale_dao import SaleDao
from db_connection.connection_pool import ConnectionPool
from ui.main_ui import mainmenu
from ui.sale_ui import Sale_form

if __name__ == '__main__':
    st = SaleDao()
    res2 = st.select_item()

    #연결
    pool = ConnectionPool.get_instance()
    connection = pool.get_connection()

    #ui연결
    app = QtWidgets.QApplication(sys.argv)
    pdt = ProductDao()
    # res = pdt.select()
    # p = Sale_form()
    # p.load_data(res)
    # p.sale_load_data(res2)
    w = Sale_form()
    # w.show()
    sys.exit(app.exec_())
