#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. El vendedor desea 
#saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el
#mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.
"""Ejercicio3"""
class ejercicio3:
    def ventas():
        SuldBase= float(input("Ingrese salario base es: "))
        Vent1= float(input("Ingrese valor venta1: "))
        Vent2= float(input("Ingrese valor venta2: "))
        Vent3= float(input("Ingrese valor venta3: "))
        TotalVentas=Vent1+Vent2+Vent3
        Com=TotalVentas*0.10
        TotalRec= SuldBase+Com
        print("Su total de salario a recibir es: $",TotalRec)

    ventas()      