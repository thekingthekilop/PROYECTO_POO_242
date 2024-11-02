class Seccion:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, id_producto):
        self.productos = [prod for prod in self.productos if prod.id != id_producto]

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def buscar_producto_por_id(self, id_producto):
        for producto in self.productos:
            if producto.id == id_producto:
                return producto
        return None

    def listar_productos(self):
        return [prod.mostrarDetalles() for prod in self.productos]
        