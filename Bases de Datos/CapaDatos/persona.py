class Persona:
  def __init__(self,nombre,id):
    self.__nombre=nombre
    self.__id=id 

  def getNombre(self):
    return self.__nombre
  def getId(self):
    return self.__id

  def setNombre(self,nombre):
    self.__nombre=nombre
  def setId(self,id):
    self.__id=id

  def __str__(self) -> str:
      return "Nombre: ",self.getNombre()," con id: ",self.getId()