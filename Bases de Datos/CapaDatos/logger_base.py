#Configuracion general del login
import logging 

logger=logging

logger.basicConfig(level=logger.DEBUG,
                    format="%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s", #Muestra el tiempo y dia y hora,nivel,archivo,numero de linea y mensaje 
                    datefmt='%I:%M:%S', #Muestro solo la hora y no el dia y fecha
                    handlers=[
                      logger.FileHandler('python/CapaDatos/capa_datos.log'), #Almacena datos en un archivo
                      logger.StreamHandler() #Muestra por pantalla errores
                    ]
                    )
if __name__=='__main__':
  logger.warning("Cuidado!")
  logger.info("Información")
  logger.debug("Debug")
  logger.error("Error")
  logger.critical("Error critico")