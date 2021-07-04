from Pelicula import Pelicula
import CatalogoPeliculas
opcion=0
catalogo=CatalogoPeliculas.Catalogo
while opcion!=5:
  print()
  print("1.Agregar pelicula")
  print("2.Lista peliculas")
  print("3.Eliminar peliculas")
  print("4.Eliminar pelicula por titulo")
  print("5.Salir")
  opcion=int(input("Valor: "))

  if opcion==1:
    nombre=input("Introduce un nombre: ")
    peli=Pelicula(nombre)
    catalogo.agregar_pelicula(peli)
  elif opcion==2:
    catalogo.listar_peliculas()
  elif opcion==3:
    catalogo.eliminar_peliculas()
  elif opcion==4:
    nombre=input("Introduce un nombre: ")
    catalogo.eliminar(nombre)
  else:
    print("Opcion inválida")
else:
  print("Hasta luego!")