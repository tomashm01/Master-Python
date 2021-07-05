import pymysql as sql

conexion=sql.connect(host='localhost',user='root',passwd='',db='python')
cursor=conexion.cursor()

#Consulta sobre bbdd
cursor.execute("select nombre from persona where id=120")

#Insertar datos
inserts='insert into persona(id,nombre)values(%s,%s)'
valores=(
  ('200','Karol'),
  ('206','Pedro')
)
cursor.executemany(inserts,valores)
#Guardamos info al insertar datos
conexion.commit()

#Modificar datos de varias tablas
consultaModificar='update persona set nombre=%s where id=%s'
modificarValores=(
  ('Juan Carlos','1'),
  ('Elena Maria','120')
)
cursor.executemany(consultaModificar,modificarValores)
conexion.commit()

#Eliminar registros
consultaEliminar='delete from persona where id=%s'
valoresEliminar=(
  ('1'),
  ('120')
)
cursor.executemany(consultaEliminar,valoresEliminar)
conexion.commit()

#Cerrar conexion y cursor
conexion.close()
cursor.close()

