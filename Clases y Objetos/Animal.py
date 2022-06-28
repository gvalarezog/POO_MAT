

class Animal:
    """
    Crear objetos de la clase Animal
    """
    def __init__(self, codigo : str, nombre : str = None, numero_patas : int = None, peligro_extinsion : bool = False, ):
        self._nombre = nombre
        self._numero_patas = numero_patas
        self._peligro_extinsion = peligro_extinsion
        self._codigo = codigo

    def __str__(self):
        return f'Animal [codigo: {self._codigo}, nombre: {self._nombre}, numero_patas= {self._numero_patas}, ' \
               f'peligro_extinsion: {self._peligro_extinsion}]'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def numero_patas(self):
        return self._numero_patas

    @numero_patas.setter
    def numero_patas(self, numero_patas):
        self._numero_patas = numero_patas

    @property
    def peligro_extinsion(self):
        return self._peligro_extinsion

    @peligro_extinsion.setter
    def peligro_extinsion(self, peligro_extinsion):
        self._peligro_extinsion = peligro_extinsion

    @property
    def codigo(self):
        return self._codigo

    #solo lectura o read only
    # @codigo.setter
    # def codigo(self, codigo):
    #     self._codigo = codigo


if __name__ == '__main__':
    a1 = Animal(nombre='Perro', numero_patas=4, peligro_extinsion=False, codigo='0002')
    print(a1)
    print(a1.nombre)
    # print(a1._nombre)
    print(a1.numero_patas)
    print(a1.peligro_extinsion)

    a1.nombre = 'Gato'
    print(a1.nombre)

    #a1._nombre = 'Iguana'
    a1.nombre = 'Iguana'
    print(a1.nombre)


    a2 = Animal(nombre="Gallina", codigo='0003')
    print(a2)

    a3 = Animal(codigo='0001')
    print(a3)
    a3.nombre = 'Pez'
    a3.numero_patas = 0
    a3.peligro_extinsion = False
    # a3.codigo = '0001'
    # a3.__codigo = '0025'
    # a3.codigo = '0025'
    print(a3)

    # print(f'El nombre del animal es: {a3.nombre} tiene {a3.numero_patas} y esta en peligro de extsinsion? {a3.peligro_extinsion}')

    a4 = Animal(codigo=400, nombre='Tortuga', numero_patas='Cuatro', peligro_extinsion='False')
    print(a4)
    print(type(a4.codigo))


