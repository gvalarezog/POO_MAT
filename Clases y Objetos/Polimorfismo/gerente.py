from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento: {self.departamento}] {super().__str__()}'

    def mostrar_detalles(self):
        return f'El gerente del departamento {self.departamento} es {self.nombre} con sueldo {self.sueldo}'

if __name__ == '__main__':
    g1 = Gerente(nombre='Maria', sueldo=1000, departamento='TH')
    print(g1)
    print(g1.mostrar_detalles())