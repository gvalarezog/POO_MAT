from figura_geometrica import FiguraGeometrica
from color import Color

class Rectangulo(Color, FiguraGeometrica ):
    def __init__(self, base:float=None, alto:float=None, color:str=None):
        # super(Rectangulo, self).__init__(ancho=base, alto=alto)
        FiguraGeometrica.__init__(ancho=base, alto=alto, self=self)
        Color.__init__(self, nombre=color)

    def __str__(self):
        return f'Rectangulo [ancho: {self.ancho}, alto: {self.alto}] {Color.__str__(self)} ' \
               f'{FiguraGeometrica.__str__(self)}'


    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return self.alto * 2 + self.ancho * 2

if __name__ == '__main__':
    r1 =  Rectangulo(base=10, alto=6, color='Negro')
    print(r1)
    print(f'El area es: {r1.calcular_area()}')
    print(f'El perimetro es: {r1.calcular_perimetro()}')
    print(Rectangulo.mro())