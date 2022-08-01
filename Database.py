
import sqlite3 as sl
qb_conn = sl.connect('cw_bank.db')


def simple_print(result):
    for r in result:
        none_cleaned = [x for x in r if x is not None]
        print(none_cleaned)



class Module:
    def __init__(self, module_code, module_name):
        self.module_code = module_code
        self.module_name = module_name
        self.sql = "INSERT INTO modules (module_code, module_name) values "
        self.sql += "(" + str(self.module_code) + ", '" + str(self.module_name) + "')"
        self.db()

    def db(self, show=False):
        with qb_conn:
            if show:
                print(self.sql)
            result = qb_conn.execute(self.sql)
            return [r for r in result]

    @classmethod
    def show_modules(self):
        sql = "SELECT * FROM modules"
        with qb_conn:
            result = qb_conn.execute(sql)
            return [r for r in result]

    def update_module(self, new_module_name):
        self.module_name = new_module_name
        self.sql = "UPDATE modules SET module_name = '"+ self.module_name + "' WHERE module_code = " + str(self.module_code)
        return self.db() + self.show_modules()

        #returns the set of new rows. and in here python goes from left to right

    def delete_module(self):
        self.sql = "DELETE FROM modules WHERE module_code = " + str(self.module_code)
        self.module_name = "DELETED_MODULE"
        return self.db() + self.show_modules()


def create_tables():

    with qb_conn:
        # can only execute one command at a time
        sql = """CREATE TABLE modules
                (module_code INTEGER NOT NULL PRIMARY KEY,
                module_name TEXT);
                """
        try:
            qb_conn.execute(sql)
        except sl.OperationalError:
            print("Couldn't create modules")  #table already there




def delete_tables():

    with qb_conn:

        sql = "DROP TABLE modules"
        try:
            qb_conn.execute(sql)
        except:
            print("Couldn't execute ",sql)



def display_table(table_name):
    with qb_conn:
        rows = qb_conn.execute("SELECT * FROM "+table_name)
        for row in rows:
            print(row)

