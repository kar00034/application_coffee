import inspect

from mysql.connector import Error

from dao.abs_das import Dao

insert_sql = "INSERT INTO sale VALUES(NULL, %s, %s, %s, %s)"
update_sql = "update sale set code=%s, price=%s, salecnt=%s, marginrate=%s where no=%s"
delete_sql = "delete from sale where no = %s"
select_sql = "select no, code, price, salecnt, marginrate from sale"
select_sql_where = select_sql + " where no = %s"


class SaleDao(Dao):

    def insert_item(self, code=None, price=None, salecnt=None, marginrate=None):
        # print("\n______ {}:{} ______".format(inspect.stack()[0][3], "sale"))
        args = (code, price, salecnt, marginrate)
        try:
            super().do_query(query=insert_sql, kwargs=args)
            return True
        except Error:
            return False

    def update_item(self, code=None, price=None, saleCnt=None, marginRate=None, no=None):
        # print("\n_______ {}() _______".format(inspect.stack()[0][3]))
        args = (code, price, saleCnt, marginRate, no)
        try:
            super().do_query(query=update_sql, kwargs=args)
            print(update_sql)
            print(args)
            return True
        except Error:
            return False

    def delete_item(self, no=None):
        # print("\n_______ {}() _______".format(inspect.stack()[0][3]))
        args = (no,)
        try:
            super().do_query(query=delete_sql, kwargs=args)
            return True
        except Error:
            return False

    def select_item(self, no=None):
        # print("\n_______ {}() _______".format(inspect.stack()[0][3]))
        try:
            conn = self.connection_Pool.get_connection()
            cursor = conn.cursor()
            cursor.execute(select_sql) if no is None else cursor.execute(select_sql_where, (no,))
            res = []
            [res.append(row) for row in self.iter_row(cursor, 5)]
            return res
        except Error as err:
            print(err)
        finally:
            cursor.close()
            conn.close()

    def iter_row(self, cursor, size=5):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

