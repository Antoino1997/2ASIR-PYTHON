"""
Script match-case en el que recoge dos números
Y un operador pasados por teclado.
"""
num_1 = int(input('Número 1: ')) #Número 1
num_2 = int(input('Número 2: ')) #Número 2
oper = (input('Escoge un operador (suma, resta, multiplicacion, division): ')) #Operador

if oper == "suma": #Suma
    print(num_1 + num_2)
elif oper == "resta": #Resta
    print(num_1 - num_2)
elif oper == "multiplicacion": #Multiplicación
    print(num_1 * num_2)
elif oper == "division": #División
    print(num_1 / num_2)
else: #En caso de error
    print("Escoge un operador valido")
