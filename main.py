from PyQt5.QtWidgets import QApplication

from db_connection.connection_pool import ConnectionPool
from ui.mainmenu_ui import mainmenu

if __name__ == '__main__':
    # DB 연결
    pool = ConnectionPool.get_instance()
    connection = pool.get_connection()

    # ui연결
    app = QApplication([])
    w = mainmenu()
    app.exec_()
