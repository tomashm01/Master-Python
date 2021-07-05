class Rectangulo:
  def __init__(self,base,altura):
      self.base=base
      self.altura=altura
  def area(self):
    return self.base*self.altura
  def perimetro(self):
    return self.base*2 + self.altura*2

base=int(input("Introduce la base :"))
altura=int(input("Introduce la altura: "))

rectangulo=Rectangulo(base,altura)

print(rectangulo.area())
print(rectangulo.perimetro())