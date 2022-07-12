
class Empleado:
    """
    Docuemntacion de la clase empleado
    """
    contador_empleado = 0
    def __init__(self, nombre:str=None, sueldo:float=None):
        Empleado.contador_empleado += 1
        self._id =  Empleado.contador_empleado
        self._nombre = nombre
        self._sueldo = sueldo

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [id: {self._id}, Nombre: {self._nombre}, Sueldo: {self._sueldo}]'

    def mostrar_detalles(self):
        return f'El nombre del empleado es {self._nombre} y su sueldo es {self._sueldo}'

if __name__ == '__main__':
    e1 = Empleado(nombre='Luis', sueldo=500)
    print(e1)
    print(e1.mostrar_detalles())