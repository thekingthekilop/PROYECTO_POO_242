class Almacen:
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.secciones = []

    def agregar_seccion(self, seccion):
        self.secciones.append(seccion)

    def eliminar_seccion(self, id_seccion):
        self.secciones = [sec for sec in self.secciones if sec.id != id_seccion]

    def buscar_seccion_por_nombre(self, nombre):
        for seccion in self.secciones:
            if seccion.nombre == nombre:
                return seccion
        return None

    def buscar_seccion_por_id(self, id_seccion):
        for seccion in self.secciones:
            if seccion.id == id_seccion:
                return seccion
        return None

    def listar_secciones(self):
        return [sec.nombre for sec in self.secciones]

