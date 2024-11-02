almacen = Almacen(1, "Almacén Principal", "Calle Falsa 123")

seccion_alimentos = Seccion(1, "Alimentos")
seccion_tecnologia = Seccion(2, "Tecnología")
seccion_ropa = Seccion(3, "Ropa")

almacen.agregar_seccion(seccion_alimentos)
almacen.agregar_seccion(seccion_tecnologia)
almacen.agregar_seccion(seccion_ropa)

producto1 = Alimento(101, "Pan", 1.5, "Pan fresco", "2024-12-01")
producto2 = Tecnologia(102, "Teléfono", 299.99, "Smartphone 4G", 2)
producto3 = Ropa(103, "Camiseta", 19.99, "Camiseta de algodón", "L")

seccion_alimentos.agregar_producto(producto1)
seccion_tecnologia.agregar_producto(producto2)
seccion_ropa.agregar_producto(producto3)

print("Productos en la sección Alimentos:")
print("\n".join(seccion_alimentos.listar_productos()))

print("\nProductos en la sección Tecnología:")
print("\n".join(seccion_tecnologia.listar_productos()))

print("\nProductos en la sección Ropa:")
print("\n".join(seccion_ropa.listar_productos()))

# Listar secciones en el almacén
print("\nSecciones en el almacén:")
print("\n".join(almacen.listar_secciones()))

