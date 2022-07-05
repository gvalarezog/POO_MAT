from figura_geometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado:float=None, activo:bool=True):
        super(Cuadrado, self).__init__(ancho=lado, alto=lado)
        self._activo = activo

    def __str__(self):
        return f'Cuadrado [lado: {self.ancho}, activo: {self._activo}]'

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, activo):
        self._activo = activo

    def calcular_area(self):
        return self.ancho * self.alto

if __name__ == '__main__':
    c1 = Cuadrado(lado=5, activo=True)
    print(c1)
    print(f'El area del cuadrado es: {c1.calcular_area()}')
    # print(__name__)