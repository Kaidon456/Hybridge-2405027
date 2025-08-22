from sumar import sum
from resta import res
from multiplicacion import multi
from dividir import div
from suma_avanzada import sumAdv

while True:
    print("""
    Ingrese su opcion
    1.- Sumar
    2.- Resta
    3.- Multiplicacion
    4.- Dividir
    5.- Suma avanzada
    6.- Salir
    """)
    opc = int(input("Que elije? "))
    if opc == 6:
        print("SALIENDO...")
        break
    elif opc in [1,2,3,4,5]:
        if opc == 5:
            #Iba a ser un codigo mas sencillo y eficiente, pero medio flojera xDD
        else:
            a = int(input("Ingrese el numero A: "))
            b = int(input("Ingrese el numero B: "))
            if opc == 1:
                resultado = sum(a,b)
            if opc == 2:
                resultado = res(a,b)
            if opc == 3:
                resultado = multi(a,b)
            if opc == 4:
                resultado = div(a,b)
            print(f"El resultado de la operacion es {resultado}")
    else:
        print(f"No existe la opcion {opc}.")