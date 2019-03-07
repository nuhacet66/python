import MySQLdb


db = MySQLdb.connect("localhost","root","1234","crud" )


cursor = db.cursor()

sql = "SELECT * FROM customers> '%d'"
try:

   cursor.execute(sql)

   results = cursor.fetchall()
   for row in results:
      name = row[0]
      email = row[1]
      mobile = row[2]


      print "name=%s,email=%s,mobile=%d" % \
             (name, email, mobile )
except:
   print "Error: unable to fecth data"

db.close()