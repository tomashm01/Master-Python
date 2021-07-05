class Persona:
  def __init__(self,nombre):
    self.__nombre=nombre
  #Sobreescribo el metodo
  def __add__(self,otro):
    return self.__nombre+" "+otro.__nombre
  #Resta
  def __sub__(self,otro):
    return "Operacion no soportada"
p1=Persona("Juan")
p2=Persona("Karla")

print(p1+p2)

print(p1-p2)

'''
Operador +: metodo __add__(self,other)
Operador -: metodo __sub__(self,other)
Operador *:metodo __mul__(self,other)
Operador /: metodo __truediv__(self,other)
Operador //:metodo __floordiv__(self,other)
Operador %: metodo __mod__(self,other)
Operador **: metodo __pow__(self,other)

Operador <: __lt__(self,other)
Operador >: __gt__(self,other)
Operador <=: __le__(self,other)
Operador >=: __ge__(self,other)
Operador ==: __eq__(self,other)
Operador !=: __ne__(self,other)
'''