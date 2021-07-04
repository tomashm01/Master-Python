from figura_geometrica import Figura
from color import Color

class Cuadrado(Figura,Color):
  def __init__(self,lado,color):
    Figura.__init__(self,lado,lado)
    Color.__init__(self,color)
  def area(self):
    return super().__base*super().__altura
