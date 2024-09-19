# Diccionario para almacenar productos y sus cantidades
inventario = {}

# Función para agregar un producto al inventario
def agregar_producto(nombre, cantidad):
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad
    print(f'Producto {nombre} agregado con {cantidad} unidades.')
    mostrar_inventario()  # Mostrar el inventario actualizado después de agregar

# Función para eliminar todo un producto o una cantidad específica
def eliminar_producto(nombre, cantidad=None):
    if nombre in inventario:
        if cantidad is None:  # Eliminar todo el producto
            del inventario[nombre]
            print(f'Producto {nombre} eliminado completamente del inventario.')
        else:
            if inventario[nombre] > cantidad:
                inventario[nombre] -= cantidad
                print(f'Se han eliminado {cantidad} unidades de {nombre}.')
            elif inventario[nombre] == cantidad:
                del inventario[nombre]
                print(f'Se han eliminado todas las unidades de {nombre}.')
            else:
                print(f'No hay suficientes unidades para eliminar. {nombre} tiene {inventario[nombre]} unidades.')
    else:
        print(f'Producto {nombre} no encontrado.')

# Función para verificar productos con bajas cantidades
def verificar_bajas(cantidad_minima):
    productos_bajos = {k: v for k, v in inventario.items() if v <= cantidad_minima}
    if productos_bajos:
        print("Productos con bajas cantidades:")
        for producto, cantidad in productos_bajos.items():
            print(f'{producto}: {cantidad} unidades')
    else:
        print('No hay productos con cantidades bajas.')

# Función para mostrar el inventario completo
def mostrar_inventario():
    if inventario:
        print("\n--- Inventario Actual ---")
        for i, (producto, cantidad) in enumerate(inventario.items(), start=1):
            print(f'{i}. {producto}: {cantidad} unidades')
    else:
        print("El inventario está vacío.")

# Función para permitir al usuario seleccionar un producto del inventario para eliminar
def seleccionar_producto():
    mostrar_inventario()
    if inventario:
        try:
            seleccion = int(input("Selecciona el número del producto que deseas eliminar: "))
            producto_seleccionado = list(inventario.keys())[seleccion - 1]
            return producto_seleccionado
        except (ValueError, IndexError):
            print("Selección no válida. Intenta de nuevo.")
            return None
    else:
        print("No hay productos en el inventario.")
        return None

# Función principal del programa
def gestionar_inventario():
    while True:
        print("\n--- Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Verificar productos con cantidades bajas")
        print("4. Mostrar inventario")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre del producto: ")
            cantidad = int(input(f"Cantidad de {nombre}: "))
            agregar_producto(nombre, cantidad)
        
        elif opcion == '2':
            producto_seleccionado = seleccionar_producto()
            if producto_seleccionado:
                print(f'{producto_seleccionado} tiene {inventario[producto_seleccionado]} unidades.')
                eleccion = input(f"¿Deseas eliminar una cantidad específica de {producto_seleccionado}? (s/n): ")
                if eleccion.lower() == 's':
                    cantidad = int(input(f"¿Cuántas unidades de {producto_seleccionado} deseas eliminar?: "))
                    eliminar_producto(producto_seleccionado, cantidad)
                else:
                    eliminar_producto(producto_seleccionado)  # Eliminar todo el producto
        
        elif opcion == '3':
            cantidad_minima = int(input("Introduce la cantidad mínima para verificar productos: "))
            verificar_bajas(cantidad_minima)
        
        elif opcion == '4':
            mostrar_inventario()
        
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

# Ejecutar el programa
gestionar_inventario()
