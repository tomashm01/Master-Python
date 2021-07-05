#No tienen orden y los elementos son unicos(no puede haber elementos duplicados)
#No se puede modificar sus elementos
#Pero si se pueden insertar o eliminar elementos

ejemplo={"Posicion X","Hola",-5,True}
print(ejemplo)
print("Hola" in ejemplo) #True si existe
print("Adios" in ejemplo) #False
ejemplo.add("Adios")
ejemplo.remove("Posicion X")
print(ejemplo)