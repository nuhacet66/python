
import MySQLdb

db = MySQLdb.connect("localhost","root","1234","crud" )



cursor = db.cursor()

sql = "DELETE FROM customers WHERE id > '%d'" % (20)
try:

   cursor.execute(sql)

   db.commit()
except:

   db.rollback()


db.close()