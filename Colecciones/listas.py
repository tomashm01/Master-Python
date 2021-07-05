#Imprime elementos de manera ordenada
#Mantiene el orden de insercion de elementos

lista=["Juan","Karla","Ricardo",3,True]
print(lista)
print(len(lista))
print(lista[-1])
print(lista[0:2]) #No incluye el elemento 2
print(lista[:3]) #No incluye el elemento 3
print(lista[2:]) #No incluye los 2 primeros
lista.append("Hola") #Introducir elemento
print(lista)
lista.insert(1,"Posicion 1")
print(lista)
lista.pop() #Remover ultimo elemento
print(lista)
del lista[4] #Elimina elemento en una posicion
print(lista)