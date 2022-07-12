from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):

    contador_cuadrado = 0

    def __init__(self, lado:float=None, activo:bool=True, color:str=None):
        FiguraGeometrica.__init__(self, ancho=lado, alto=lado)
        Color.__init__(self, nombre = color)
        # Cuadrado.contador_cuadrado = Cuadrado.contador_cuadrado + 1
        Cuadrado.contador_cuadrado += 1
        self._id = Cuadrado.contador_cuadrado
        self._activo = activo

    def __str__(self):
        # return f'Cuadrado [lado: {self.ancho}, activo: {self._activo}, color: {self.nombre}]'
        return f'Cuadrado [id: {self._id}, lado: {self.ancho}, activo: {self._activo}] {Color.__str__(self)}'

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, activo):
        self._activo = activo

    @property
    def id(self):
        return self._id

    # @id.setter
    # def id(self, id):
    #     self._id = id

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 4 * self.alto

if __name__ == '__main__':
    c1 = Cuadrado(lado=5, activo=True, color = 'Amarillo')
    print(c1)
    print(f'El area del cuadrado es: {c1.calcular_area()}')
    print(f'El perimetro del cuadrado es: {c1.calcular_perimetro()}')
    print(Cuadrado.mro())
    c2 =  Cuadrado(lado=3, activo=False, color='Rojo')
    print(c2)
    print(Cuadrado.contador_cuadrado)
    c3 =  Cuadrado()
    print(c3)
    c4 = Cuadrado()
    print(c4)
    print(c4.id)