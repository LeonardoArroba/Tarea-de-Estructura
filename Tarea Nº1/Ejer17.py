#Calcular el factorial de N números enteros leídos de teclado.
#El problema consistirá en realizar una estructura de N iteraciones aplicando el factorial de un número
"""Ejercicio 17"""

class EstrucIterativa:
    def __init__(self):
        pass
    def bucleAni(self):
        num1 = int(input('Ingrese numero: '))
        fact1 = 1
        for i in range(1, num1+1):
            fact1 *= i
        print('El factorial del numero {} es: {} '.format(num1, fact1)) 

calculo = EstrucIterativa()
calculo.bucleAni()
