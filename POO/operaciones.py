class Operaciones:
  def __init__(self,valor1,valor2):
      self.valor1=valor1
      self.valor2=valor2
  def sumar(self):
    return self.valor1+self.valor2
  def restar(self):
    return self.valor1-self.valor2

miOperacion=Operaciones(15,20)

print(miOperacion.restar())
print(miOperacion.sumar())