# Este es Mi primer intento de calculadora en Python.
# Mi meta es llegar a ser programador.
# Me Llamo Johan Rosales.
# Este mundillo me atrapo desde muy joven. 
# Hace aproxidamente 2 semanas empecé un curso de Python y HTML.
# Pienso hacer otra calculadora usando while para hacer bien el bucle.



var1= 0
var2= 0
resultado = 0
ed = """El resultado es:"""
operacion = " "


    
def bienvenida():
    print("Bienvenido a la Calculadora")
    print('''
Escriba "suma" para sumar.
Escriba "resta" para restar.
Escriba "multi" para multiplicar.
Escriba "div" para dividir.
''')
    global operacion 
    operacion = input("Inserte Una Operación")

def suma():
    var1 = int(input("Ingrese un Número"))
    var2 = int(input("Ingrese otro número"))
    resultado = var1 + var2
    print(ed)
    print(resultado)
    bienvenida()
    
    
def resta():
    var1 = int(input("Ingrese un número"))
    var2 = int(input("Ingrese otro número"))
    resultado = var1 - var2
    print(ed)
    print(resultado)
    bienvenida()
    
    

def multi():
    var1 = int(input("Ingrese un número"))
    var2 = int(input("Ingrese otro número"))
    resultado = var1 * var2
    print(ed)
    print(resultado)
    bienvenida()
    
    

def div():
    var1 = int(input("Ingrese un número"))
    var2 = int(input("Ingrese otro número"))
    resultado = var1 / var2
    print(ed)
    print(resultado)
    bienvenida()

bienvenida()

if operacion.lower() == "suma":
    suma()
elif operacion.lower() == "resta":
    resta()
elif operacion.lower() == "multi":
    multi()
elif operacion.lower() == "div":
    div()
else:
    print("""Inserte una Operación válida
          
          """)
    bienvenida()

       




