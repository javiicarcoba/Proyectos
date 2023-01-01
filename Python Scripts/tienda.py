producto = input("Que producto es? ")
precio = float(input("Su precio? "))
cant = int(input("Cantidad de este producto? "))

print("Producto: {}\nCantidad: {}\nPrecio unitario: {:.2f}\nPrecio total: {:.2f}".format(producto,cant,precio,precio*cant))