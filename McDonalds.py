class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad

    def vender(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        else:
            return False

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_producto}) - ${self.precio:.2f} - Cantidad: {self.cantidad}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto

    def obtener_producto(self, id_producto):
        return self.productos.get(id_producto)

    def listar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def vender_producto(self, id_producto, cantidad):
        producto = self.obtener_producto(id_producto)
        if producto:
            if producto.vender(cantidad):
                print(f"Venta exitosa: {cantidad} unidades de '{producto.nombre}'")
            else:
                print(f"No hay suficiente stock para '{producto.nombre}'")
        else:
            print("Producto no encontrado")

def menu():
    print("----- Punto de Venta -----")
    print("1. Listar productos")
    print("2. Vender producto")
    print("3. Agregar producto")
    print("4. Salir")

def main():
    inventario = Inventario()

    # Agregar algunos productos iniciales
    inventario.agregar_producto(Producto(1, "Manzanas", 0.50, 100))
    inventario.agregar_producto(Producto(2, "Pan", 1.00, 50))
    inventario.agregar_producto(Producto(3, "Leche", 1.20, 30))

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            inventario.listar_productos()
        elif opcion == '2':
            id_producto = int(input("Ingrese el ID del producto a vender: "))
            cantidad = int(input("Ingrese la cantidad a vender: "))
            inventario.vender_producto(id_producto, cantidad)
        elif opcion == '3':
            id_producto = int(input("Ingrese el ID del nuevo producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            inventario.agregar_producto(Producto(id_producto, nombre, precio, cantidad))
            print(f"Producto '{nombre}' agregado exitosamente.")
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
