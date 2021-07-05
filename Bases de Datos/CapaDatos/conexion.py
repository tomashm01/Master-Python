from logger_base import logger
import pymysql as sql
import sys

class Conexion:
  __DATABASE='python'
  __USERNAME='root'
  __PASSWORD=''
  __HOST='127.0.0.1'
  __conexion=None
  __cursor=None

  @classmethod
  def obtenerConexion(cls):
    if cls.__conexion is None:
      try:
        cls.__conexion=sql.connect(host=cls.__HOST,user=cls.__USERNAME,passwd=cls.__PASSWORD,database=cls.__DATABASE)
        logger.debug(f'Conexion exitosa: {cls.__conexion}')
        return cls.__conexion
      except Exception as e:
        logger.error(f'Error al conectar a la bbdd: {e}')
        sys.exit()
    else:
      return cls.__conexion
  
  @classmethod
  def getCursor(cls):
    if cls.__cursor is None:
      try:
        cls.__cursor=cls.obtenerConexion().cursor()
        logger.debug(f'Se abrio el cursor: {cls.__cursor}')
        return cls.__cursor
      except Exception as e:
        logger.error(f'Error al obtener cursor: {e}')
        sys.exit()
    else:
      return cls.__cursor

  @classmethod
  def cerrar(cls):
    if cls.__cursor is not None:
      try:
        cls.__cursor.close()
        logger.debug(f'Se cerro el cursor: {cls.__cursor}')
      except Exception as e:
        logger.error(f'Error al cerrar cursor: {e}')
        sys.exit()
    if cls.__conexion is not None:
      try:
        cls.__cursor.close()
        logger.debug(f'Se cerro el conexion: {cls.__cursor}')
      except Exception as e:
        logger.error(f'Error al cerrar conexion: {e}')
        sys.exit()   
    logger.debug('Se han cerrado los objetos de conexion y cursor')
