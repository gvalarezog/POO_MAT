

class Estudiante:
    def __init__(self, nombre, nivel, carrera):
        self._nombre = nombre
        self._nivel = nivel
        self._carrera = carrera

    def __str__(self):
        return f'Estudiante [nombre: {self._nombre}, nivel: {self._nivel}, carrera: {self._carrera}]'

    def obtener_nombre(self):
        return self._nombre

    def modifcar_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre


# probar la clase
e1 = Estudiante('Luis', 3, 'LGIG')
print(e1)
