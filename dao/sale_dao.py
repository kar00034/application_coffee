import inspect

from mysql.connector import Error

from dao.abs_das import Dao

insert_sql = "insert into sale values(null,%s,%s,%s,%s)"
update_sql = "update sale set code=%s, price=%s, salecnt=%s, marginrate=%s where no=%s"
delete_sql = "delete from sale where no = %s"
select_sql = "select no, code, price, salecnt, marginrate from sale"
select_sql_where = select_sql + " where no = %s"

class SaleDao(Dao):
    def insert_item(self, code=None, price=None, saleCnt=None, marginRate=None):
        print("\n_______ {}() _______".format(inspect.stack()[0][3]))
        args = (code, price, saleCnt, marginRate)
        try:
            super().do_query(query=insert_sql, kwargs=args)
            return True
        except Error:
            return False

    def update_item(self, **kwargs):
        def update_item(self, code=None, price=None, saleCnt=None, marginRate=None):
            print("\n_______ {}() _______".format(inspect.stack()[0][3]))
            args = (code, price, saleCnt, marginRate)
            try:
                super().do_query(query=insert_sql, kwargs=args)
                return True
            except Error:
                return False

    def delete_item(self, **kwargs):
        def delete_item(self, no=None):
            print("\n_______ {}() _______".format(inspect.stack()[0][3]))
            args = (no)
            try:
                super().do_query(query=insert_sql, kwargs=args)
                return True
            except Error:
                return False

    def select_item(self, **kwargs):
        def select_item(self, code=None, price=None, saleCnt=None, marginRate=None):
            print("\n_______ {}() _______".format(inspect.stack()[0][3]))
            args = (code, price, saleCnt, marginRate)
            try:
                super().do_query(query=insert_sql, kwargs=args)
                return True
            except Error:
                return False