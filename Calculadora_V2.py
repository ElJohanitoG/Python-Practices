"""Calculadora V2"""

#Variables

operacion = ""



#operaciones

def suma():
    var1 = int(input("Ingrese un número"))
    var2 = int(input("Ingrese otro número"))
    suma = var1 + var2 
    print("El resultado es")
    print(suma)
def resta():
    var1 = int(input("Ingrese un número"))
    var2 = int(input("Ingrese otro número"))
    resta = var1 - var2 
    print("El resultado es")
    print(resta)
def multi():
    var1 = int(input("Ingrese un número"))
    var2 = int(input("Ingrese otro número"))
    multi = var1 * var2 
    print("El resultado es")
    print(multi)
def div():
    var1 = int(input("Ingrese un número"))
    var2 = int(input("Ingrese otro número"))
    div = var1 / var2 
    print("El resultado es")
    print(div)



while True:
    print("Bienvenido a Calculadora")
    print('Escriba "salir" para salir')
    print('Escriba "1" para sumar')
    print('Escriba "2" para restar')
    print('escriba "3" para multiplicar')
    print('Escriba "4" para dividir')
    operacion = input("Ingrese Su operacíon")
    
    if operacion.lower().strip() == "salir":
        break
    elif operacion.lower().strip() == "1":
        suma()
    elif operacion.lower().strip() == "2":
        resta()
    elif operacion.lower().strip() == "3":
        multi()
    elif operacion.lower().strip() == "4":
        div()
    else:
        print("Ingrese una Operación valida")    