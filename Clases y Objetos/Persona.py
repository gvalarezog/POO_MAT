

class Persona:
    def __init__(self, nombre, genero, ocupacion, mail):
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion
        self._mail = mail

    def __str__(self):
        return f'Persona [nombre: {self._nombre}, genero: {self._genero}, ' \
               f'ocupacion: {self._ocupacion}, mail: {self._mail}]'

    def obtenerNombre(self):
        return self._nombre

    def modificarNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def obtenerGenero(self):
        return self._genero

    def modificarGenero(self, nuevoGenero):
        self._genero = nuevoGenero

    def obtenerOcupacion(self):
        return self._ocupacion

    def modificarOcupacion(self, nuevaOcupacion):
        self._ocupacion = nuevaOcupacion

    def obtenerMail(self):
        return self._mail

    def modificarMail(self, nuevoMail):
        self._mail = nuevoMail

    '''
    Metodo para que la persona se presente en el sistema
    '''
    def presentarse(self):
        print(f'El nombre de la persona es: {self.obtenerNombre()}, su ocupacion es: {self.obtenerOcupacion()}')
        if self.obtenerGenero() == 'M':
            print(f'El genero es: Masculino')
        else:
            print(f'El genero es: Femenino')

    def presentarse2(self):
        genero = None
        if self.obtenerGenero() == 'M':
            genero = 'Masculino'
        else:
            genero = 'Femenino'
        return f'El nombre de la persona es: {self.obtenerNombre()}, su ocupacion es: {self.obtenerOcupacion()}' \
               f'su genero es: {genero}'




'''
Pruebas de la clase Persona
'''
# objP1 = Persona()
objP1 = Persona('Luis', 'M', 'Estudiante', 'luis@mail.com')
print(type (objP1))
# print(objP1._nombre)
print(objP1.obtenerNombre())
print(objP1._genero)
print(objP1._ocupacion)
print(objP1)
objP1.presentarse()
objP1.modificarMail('luis@mail.com.ec')
print(objP1)
print('******************')
objP2 = Persona('Maria', 'F', 'Docente', 'maria@mail.com')
print(objP2._nombre)
print(objP2._genero)
print(objP2._ocupacion)
print(objP2.__str__())
objP2.presentarse()

