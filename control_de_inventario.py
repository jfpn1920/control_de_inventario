inventario = {
    "laptop": 10,
    "mouse": 25,
    "teclado": 15
}
LIMITE_BAJO_STOCK = 5
def mostrar_inventario():
    print("\ninventario actual")
    if not inventario:
        print("el inventario esta vacio.")
        return
    for producto, cantidad in inventario.items():
        alerta = "bajo stock" if cantidad <= LIMITE_BAJO_STOCK else ""
        print(f"- {producto}: {cantidad} unidades{alerta}")
def actualizar_stock():
    producto = input("ingrese el nombre del producto: ").capitalize()
    if producto in inventario:
        try:
            cambio = int(input("ingrese la cantidad a agregar (+) o quitar (-): "))
            inventario[producto] += cambio
            if inventario[producto] < 0:
                inventario[producto] = 0
                print("el stock no puede ser negativo, se ajusto a 0.")
            print(f"stock actualizado, nuevo stock de {producto}: {inventario[producto]} unidades")
        except ValueError:
            print("debe ingresar un numero entero valido.")
    else:
        print("el producto no existe en el inventario.")
def agregar_producto():
    producto = input("ingrese el nombre del nuevo producto: ").capitalize()
    if producto in inventario:
        print("el producto ya existe en el inventario.")
    else:
        try:
            cantidad = int(input("ingrese la cantidad inicial: "))
            if cantidad < 0:
                print("la cantidad no puede ser negativa.")
                return
            inventario[producto] = cantidad
            print(f"producto '{producto}' agregado correctamente.")
        except ValueError:
            print("debe ingresar un numero entero valido.")
def menu():
    while True:
        print("\n control de inventario ")
        print("1. mostrar inventario")
        print("2. actualizar stock")
        print("3. agregar producto")
        print("4. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            actualizar_stock()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            print("saliendo del sistema de inventario.")
            break
        else:
            print("opcion invalida, intente nuevamente.")
menu()