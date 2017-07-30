
import mysql.connector

class Add_ids:
    def __init__(self,database,table):
        self.connection = mysql.connector.connect(host="localhost", user='root', passwd='', db=database,
                                                  charset='utf8')
        self.cursor = self.connection.cursor(buffered=True)
        self.table = table

    def addtable(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `{0}` (
	`id` INTEGER(200) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	`user_n` VARCHAR(400),
	`phone_n` VARCHAR(400))""".format(self.table, ))

    def addid(self,user_rr,phone):
        self.cursor.execute("INSERT INTO `{0}` (`user_n`,`phone_n`) VALUES (%s,%s)".format(self.table,),(user_rr,phone))
        self.cursor.fetchone()
        self.connection.commit()


    def close(self):
        self.connection.close()
