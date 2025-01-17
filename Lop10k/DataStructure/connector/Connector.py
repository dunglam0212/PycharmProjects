import traceback

import mysql.connector

class Connector:
    def __init__(self):
        self.server = "localhost" #127.0.0.1
        self.port = 3306
        self.database = "employeemanagement"
        self.username = "root"
        self.password = "dungcute0212"
    def connect(self, server=None, port=None, database=None, username=None, password=None):
        if server!=None:
            self.server=server
            self.port=port
            self.database=database
            self.username=username
            self.password=password
        try:
            self.conn = mysql.connector.connect(
                host=self.server,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password
            )
        except:
            traceback.print_exc()
    def query(self, sql, val_input=None):
        cursor = self.conn.cursor()
        cursor.execute(sql, val_input)
        return cursor
