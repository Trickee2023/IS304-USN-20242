import random
import time

# 1. Implementaciones de los algoritmos de ordenamiento

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# 2. Función para medir tiempos de ejecución

def medir_tiempo(algoritmo, arr):
    inicio = time.time()
    algoritmo(arr.copy())  # Usamos copia para evitar modificar el arreglo original
    fin = time.time()
    return fin - inicio

# 3. Generación de una lista aleatoria con 10,000 elementos
tamano_lista = 10000
lista = random.sample(range(1, tamano_lista + 1), tamano_lista)

# 4. Comparativa de tiempos
tiempo_bubble = medir_tiempo(bubble_sort, lista)
tiempo_selection = medir_tiempo(selection_sort, lista)
tiempo_insertion = medir_tiempo(insertion_sort, lista)
tiempo_merge = medir_tiempo(merge_sort, lista)

# 5. Impresión de resultados
print(f"Bubble Sort: {tiempo_bubble:.2f} segundos")
print(f"Selection Sort: {tiempo_selection:.2f} segundos")
print(f"Insertion Sort: {tiempo_insertion:.2f} segundos")
print(f"Merge Sort: {tiempo_merge:.2f} segundos")
