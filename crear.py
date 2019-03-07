import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='crud')
	try:
		with conexion.cursor() as cursor:
			consulta = "INSERT INTO customers(name, email,mobile) VALUES (%s, %s,%s);"
			#Podemos llamar muchas veces a .execute con datos distintos
		cursor.execute(consulta, ("prueba","ni@ni.com",688))
		conexion.commit()
	finally:
		conexion.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)