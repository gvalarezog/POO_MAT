from figura_geometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, base:float=None, alto:float=None):
        super(Rectangulo, self).__init__(ancho=base, alto=alto)

    def __str__(self):
        return f'Rectangulo [ancho: {self.ancho}, alto: {self.alto}]'

    def calcular_area(self):
        return self.ancho * self.alto

if __name__ == '__main__':
    r1 =  Rectangulo(base=10, alto=6)
    print(r1)
    print(f'El area es: {r1.calcular_area()}')