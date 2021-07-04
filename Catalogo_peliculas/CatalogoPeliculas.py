from typing import List
from Pelicula import Pelicula
import os 

from Pelicula import Pelicula

class Catalogo(Pelicula):
  ruta="peliculas.txt"

  @staticmethod
  def agregar_pelicula(pelicula):
    try:
      archivo=open(Catalogo.ruta,"a")
      archivo.write(pelicula.get_nombre()+'\n')
    except Exception as e:
      print(e)
    finally:
      archivo.close()

  @staticmethod
  def listar_peliculas():
    try:
      archivo=open(Catalogo.ruta,"r")
      print("Catálogo:")
      print(archivo.read())
    except Exception as e:
      print(e)
    finally:
      archivo.close()

  @staticmethod
  def eliminar_peliculas():
    try:
      os.remove(Catalogo.ruta)
      print("Archivo eliminado")
    except Exception as e:
      print(e)

  @staticmethod
  def eliminar(nombre):
    try:
      archivo=open(Catalogo.ruta,"r")
      lineas=archivo.readlines()
      archivo=open(Catalogo.ruta,"w")
      for linea in lineas:
        if linea!=nombre+"\n":
          archivo.write(linea)      

    except Exception as e:
      print(e)
    finally:
      archivo.close()
  
