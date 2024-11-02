class Producto:
    def __init__(self, id, nombre, precio, descripcion):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def mostrarDetalles(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}, Descripción: {self.descripcion}"

class Alimento(Producto):
    def __init__(self, id, nombre, precio, descripcion, fecha_vencimiento):
        super().__init__(id, nombre, precio, descripcion)
        self.fecha_vencimiento = fecha_vencimiento

    def mostrarDetalles(self):
        return super().mostrarDetalles() + f", Fecha de Vencimiento: {self.fecha_vencimiento}"

class Tecnologia(Producto):
    def __init__(self, id, nombre, precio, descripcion, garantia):
        super().__init__(id, nombre, precio, descripcion)
        self.garantia = garantia

    def mostrarDetalles(self):
        return super().mostrarDetalles() + f", Garantía: {self.garantia} años"

class Ropa(Producto):
    def __init__(self, id, nombre, precio, descripcion, talla):
        super().__init__(id, nombre, precio, descripcion)
        self.talla = talla

    def mostrarDetalles(self):
        return super().mostrarDetalles() + f", Talla: {self.talla}"