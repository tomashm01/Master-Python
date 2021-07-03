class Persona:
  def __init__(self,nombre,edad,*dni):
      self.nombre=nombre #Atributo publico
      self._edad=edad #Atributo protegido
      self.__dni=dni  #Atributo privado
  def get_nombre(self):
    return self.nombre
  def get_edad(self):
    return self._edad
  def get_dni(self):
    return self.__dni
  def set_nombre(self,nombre):
    self.nombre=nombre
  def set_edad(self,edad):
    self._edad=edad
  def set_dni(self,dni):
    self.__dni=dni

class Empleado(Persona):
  def __init__(self, nombre, edad,sueldo,*dni):
      super().__init__(nombre, edad, *dni)
      self.__sueldo=sueldo
  def get_sueldo(self):
    return self.__sueldo
  def set_sueldo(self,sueldo):
    self.__sueldo=sueldo


p1=Persona("Juan",25,"4564229V")
p2=Persona("Pepe",50)

print(p1.get_dni())
print(p2.get_dni())

e1=Empleado("Tom",50,1000)
print(e1.get_sueldo())