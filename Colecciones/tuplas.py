#No se puede modificar los elementos insertados,en las listas si se puede
#Mantiene orden

frutas=("Naranja","Manzana",4,True)
print(frutas)
#Forma de modificar tupla
listaAux=list(frutas)
del listaAux[2]
frutasConvert=tuple(listaAux)
print(frutasConvert)