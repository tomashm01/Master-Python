import pymysql as sql
conexion=sql.connect(host='localhost',user='root',passwd='',db='python')
cursor=conexion.cursor()
cursor.execute("select nombre from persona where id<30")
for nombre in cursor.fetchall():
  print(nombre)
conexion.close()
cursor.close()