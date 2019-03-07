import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='crud')
	print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)