#14) Codifique un programa de consola que permita realizar las siguientes
#acciones:
#Generar un número aleatorio entre 0 y 100, para ello use la siguiente función: random.randint(0, 100)
#Una vez generado el número codifique la lógica necesaria para encontrar el número
#aleatorio ayudando al usuario informando al mismo si el número ingresado es mayor o
#menor al número aleatorio buscado. Una vez encontrado el número muestre la
#cantidad de intentos necesarios para lograrlo. 
import random
numAzar= random.randint(0,100)
num=0
intentos= 0
while num != numAzar:
    num = int(input("Ingrese un numero entre 0 y 100: "))
    intentos= intentos + 1
    if num > numAzar:
        print("El numero buscado es menor que: ",num)  
    elif num < numAzar:
         print("El numero buscado es mayor que: ",num)
    else:
        print("CORRECTO el numero era: ",numAzar)
        print("Intentos realizados: ",intentos)