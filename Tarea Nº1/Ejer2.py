#En una tienda se ofrece un descuento del 15% sobre el total de la compra y
# un cliente desea saber cuánto deberá pagar finalmente por su compra.
"""Ejercicio2 """

class descuento:
    
    def __init__(self):
        pass
    
    def ejecutar():
        TotalComp = float(input("Ingrese total de la compra: "))
        Desc = TotalComp*0.15
        TotalPagar = TotalComp - Desc
        print("El valor final que debe pagar es:",TotalPagar,"$")

    ejecutar()
     
    