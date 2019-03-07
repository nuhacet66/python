import MySQLdb


db = MySQLdb.connect("localhost","root","1234","crud" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE customers SET id = id + 1
                          WHERE name = '%c'" % ("nuha")
try:

   cursor.execute(sql)

   db.commit()
except:

   db.rollback()


db.close()