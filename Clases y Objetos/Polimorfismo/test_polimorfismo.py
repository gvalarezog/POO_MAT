from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto.mostrar_detalles())

e1 = Empleado(nombre='Luis', sueldo=500)
g1 = Gerente(nombre='Maria', sueldo=1000, departamento='TH')

imprimir_detalles(e1)
imprimir_detalles(g1)
