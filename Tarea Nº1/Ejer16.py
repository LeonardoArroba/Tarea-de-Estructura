#Aplicar los pasos de la metodología para la solución de un problema para
#leer un número entero N y calcular el resultado de la siguiente serie:
"""Ejercicio 16"""

class NunEntero:
    def __init__(self):
        pass
    
    def bucle(self):
        I=1
        serie=0
        numero= int(input("Ingrese un numero: "))
        band=True
        while band:
            if band == True:
                serie=serie+(1/I)
                band=False
            else:
                serie=serie-(1/I)
                band=True
            I+=1
            if I>numero:
                break
            print("El resultado de a serie es: {}" .format(serie))
            
calculo = NunEntero()
calculo.bucle()        

            