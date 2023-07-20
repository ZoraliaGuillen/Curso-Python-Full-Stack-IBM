# Zoralia Guillen
# Curso Python Full Stack IBM - Caso Práctico Final 

import random

def create_matriz(number):
    matriz = []
    for i in range(number):
        row = []
        for j in range(number):
            row.append(random.randint(0, 9))
        matriz.append(row)
    return matriz

def print_matriz(matriz):
    for i in range(len(matriz)):
        print("|", end='')
        for j in range(len(matriz[i])):
            number = matriz[i][j]
            print(f" {number} ", end = '')
        print("|")
    print()

def sum_rows(matriz):
    sum_rows = []
    for row in range(len(matriz)):
        sum_rows.append(sum(matriz[row]))
    return sum_rows

def total_rows(list):
    total_rows = sum(list)
    return total_rows

def sum_columns(matriz):
    sum_columns = []
    for column in range(len(matriz)):
        sums = sum(matriz[row][column] for row in range(len(matriz)))
        sum_columns.append(sums)
    return sum_columns

def total_columns(list):
    total_columns = sum(list)
    return total_columns

if __name__ == "__main__":
    
    while True:
        try:
            cadena = input("Ingresa un número para crear la matriz: ")
            number = int(cadena)
            if (isinstance(number, int) == False) or (number < 1):
                raise ValueError("")
            break
        except ValueError:
            print("El número ingresado debe ser un entero y mayor a cero. Ingresa de nuevo un número.")

    print(f"La matriz a crear será de {number}x{number}.")

    matriz = create_matriz(number)

    print_matriz(matriz)

    sumRows = []

    sumRows = sum_rows(matriz)

    print(f"\nEl resultado de la suma de cada fila es:\n")

    for number in sumRows:
        print(f"{number}")

    sumColumns = []

    sumColumns = sum_columns(matriz)

    print(f"\nEl resultado de la suma de cada columna es:\n")

    for number in sumColumns:
        print(f"{number}")

    totalRows = total_rows(sumRows)

    print(f"\nEl resultado total de cada fila es: {totalRows}\n")

    totalColumns = total_columns(sumColumns)

    print(f"\nEl resultado total de cada columna es: {totalColumns}\n")