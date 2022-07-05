from figura_geometrica import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, base:float=None, altura:float=None):
        super(Triangulo, self).__init__(ancho=base, alto=altura)

    def calcular_area(self):
        return (self.ancho * self.alto)/2

if __name__ == '__main__':
    t1 = Triangulo(base=10, altura=30)
    print(t1)
    print(f'El area de la triangulo es: {t1.calcular_area()}')