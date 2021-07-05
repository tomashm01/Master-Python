from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao: #DAO:Data Access Object, CRUD:create-read-update-delete sobre Persona
  __SELECCIONAR='SELECT * FROM persona order by id'
  __INSERTAR='INSERT INTO persona(nombre,id) values(%s,%s)'
  __ACTUALIZAR='UPDATE persona set nombre=%s where id=%s'
  __ELIMINAR='DELETE FROM persona where id=%s'

  @classmethod
  def seleccionar(cls):
    cursor=Conexion.getCursor()
    logger.debug(cursor.mogrify(cls.__SELECCIONAR))
    cursor.execute(cls.__SELECCIONAR)
    registros=cursor.fetchall()
    personas=[]
    for registro in registros:
      persona=Persona(registro[0],registro[1])
      personas.append(persona)
    Conexion.cerrar()
    return personas
  
  @classmethod
  def insertar(cls,persona):
    try:
      conexion=Conexion.obtenerConexion()
      cursor=Conexion.getCursor()
      logger.debug(cursor.mogrify(cls.__INSERTAR))
      logger.debug(f'Persona a insertar: {persona.__str__()}')
      valores=(persona.getNombre(),persona.getId())
      cursor.execute(cls.__INSERTAR,valores)
      conexion.commit()
      return cursor.rowcount
    except Exception as e:
      conexion.rollback()
      logger.error(f'Excepcion al insertar persona{e}')
    finally:
      Conexion.cerrar()

  @classmethod
  def actualizar(cls,persona):
    try:
      conexion=Conexion.obtenerConexion()
      cursor=Conexion.getCursor()
      logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
      logger.debug(f'Persona a actualizar: {persona}')
      valores=(persona.getNombre(),persona.getId())
      cursor.execute(cls.__ACTUALIZAR,valores)
      conexion.commit()
      return cursor.rowcount
    except Exception as e:
      conexion.rollback()
      logger.error(f'Excepcion al actualizar persona{e}')
    finally:
      Conexion.cerrar()
  @classmethod
  def eliminar(cls,persona):
    try:
      conexion=Conexion.obtenerConexion()
      cursor=Conexion.getCursor()
      logger.debug(cursor.mogrify(cls.__ELIMINAR))
      logger.debug(f'Persona a eliminar: {persona}')
      valores=(persona.getId())
      cursor.execute(cls.__ELIMINAR,valores)
      conexion.commit()
      return cursor.rowcount
    except Exception as e:
      conexion.rollback()
      logger.error(f'Excepcion al eliminar persona{e}')
    finally:
      Conexion.cerrar()

if __name__=='__main__':

  #Metodo seleccionar
  '''personas=PersonaDao.seleccionar()
  for persona in personas:
    logger.debug(persona)
    logger.debug(persona.getId())'''

  #Metodo insertar
  persona=Persona('Juan Pedro',15)
  registros=PersonaDao.actualizar(persona)
  logger.debug(f'Numero de registros insertados:{registros}')

  #Metodo actualizar
  persona=Persona('Juan',2)
  registros=PersonaDao.eliminar(persona)
  logger.debug(f'Numero de registros actualizados:{registros}')