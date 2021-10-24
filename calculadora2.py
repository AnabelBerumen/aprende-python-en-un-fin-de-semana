def Sumar():
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))

    print("La Suma es: ", num1 + num2)
def Restar():
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))

    print("La resta es: " , num1 - num2)

def Multiplicar():
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))

    print("La multiplicación es: ", num1 * num2)

def Dividir():
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))

    print("La división es: ", num1 / num2 )

    
def Calculadora():
    fin = False

    while not(fin):
        opc = int(input("Opción: "))
        if (opc == 1):
            Sumar()
        elif (opc == 2):
            Restar()
        elif(opc == 3):
            Multiplicar()
        elif(opc == 4):
            Dividir()
        elif(opc ==5):
            fin = 1

            print("Saliendo...\nFinalizado.")

print("""************
Calculadora
************
Menu
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5)Salir""")

Calculadora()