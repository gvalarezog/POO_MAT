from figura_geometrica import FiguraGeometrica
import math

class Circunferencia(FiguraGeometrica):
    def __init__(self, radio:float=None):
        super(Circunferencia, self).__init__(ancho=radio, alto=0)

    def __str__(self):
        return f'Circunferencia [radio: {self.ancho}]'

    def calcular_area(self):
        return math.pi * self.ancho * self.ancho

if __name__ == '__main__':
    ci1 = Circunferencia(radio=10)
    print(ci1)
    print(f'El area de la circunferencia es: {ci1.calcular_area()}')