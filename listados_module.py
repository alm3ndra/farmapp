#!/usr/bin/python3

# LISTA DE ULTIMOS MOVIMIENTOS DE VENTA
def listar_ventas(registros, ultimos):
    ventas = []
    registros_reverse = registros.reverse()
    while ultimos > len(registros):
        ultimos -= 1
    for x in range(ultimos):
        ventas.append(registros[x])
    return ventas


# BUSCA CLIENTES POR CARACTERES DE ENTRADA DE USUARIO
def encontrar_clientes(registros, nombre_cliente):
    cliente = []
    for x in range(len(registros)):
        if nombre_cliente in registros[x].cliente:
            if registros[x].cliente in cliente:
                pass
            else:
                cliente.append(registros[x].cliente)
        else:
            pass
    return cliente

# LISTADO DE CLIENTES SEGUN LOS PRODUCTOS COMPRADOS
def listar_productos_cliente(registros, cliente):

    nombre_cliente = cliente.upper()
    productos = []

    for x in range(len(registros)):
        if nombre_cliente in registros[x].cliente:
            productos.append(registros[x])
    return productos


# LISTADO COMO RESULTADO DE UNA BUSQUEDA DE PRODUCTOS
def encontrar_productos(registros, nombre_producto):
    producto = []
    for x in range(len(registros)):
        if nombre_producto in registros[x].producto:
            if registros[x].producto in producto:
                pass
            else:
                producto.append(registros[x].producto)
        else:
            pass
    return producto

# LISTADO DE CLIENTES SEGUN PRODUCTO
def listar_clientes_producto(registros, producto):

    nombre_producto = producto.upper()
    cliente = []

    for x in range(len(registros)):
        if nombre_producto in registros[x].producto:
            cliente.append(registros[x])
    return cliente

# PRODUCTOS MAS VENDIDOS
def prod_vendidos(registros, cantidad):
    producto = []
    cant_producto = []
    colunna=0

    for x in range(len(registros)):
        if x == 0:
            producto.append(registros[x].producto)
            cant_producto.append([])
            cant_producto[colunna]= [0, registros[x]]
        else:
            if registros[x].producto in producto:
                pass
            else:
                colunna = colunna + 1
                producto.append(registros[x].producto)
                cant_producto.append([])
                cant_producto[colunna]= [0, registros[x]]

    for x in range(len(producto)):
        for y in range(len(registros)):
            if producto[x] in registros[y].producto:
                cant_producto[x][0]= cant_producto[x][0] + registros[y].cantidad
            else:
                pass

    cant_producto.sort(reverse=True)#

    while cantidad > len(producto):
        cantidad -= 1
    list_cant = []
    for x in range(cantidad):
        list_cant.append([0]*2)
        list_cant[x][0] = cant_producto[x][0]
        list_cant[x][1] = cant_producto[x][1]
    return list_cant


# CLIENTES QUE MAS GASTARON
def clientes_gastadores(registros, cantidad):
    clientes = []
    cant_cliente = []
    colunna=0

    for x in range(len(registros)):
        if x == 0:
            clientes.append(registros[x].cliente)
            cant_cliente.append([])
            cant_cliente[colunna]=[0, registros[x]]
        else:
            if registros[x].cliente in clientes:
                pass
            else:
                clientes.append(registros[x].cliente)
                colunna = colunna + 1
                cant_cliente.append([])
                cant_cliente[colunna]=[0, registros[x]]


    for x in range(len(clientes)):
        for y in range(len(registros)):
            if clientes[x] in registros[y].cliente:
                cant_cliente[x][0]= cant_cliente[x][0] + (registros[y].cantidad * registros[y].precio)
            else:
                pass

    cant_cliente.sort(reverse=True)

    while cantidad > len(clientes):
        cantidad -= 1
    list_cant = []
    for x in range(cantidad):
        list_cant.append([0]*2)
        list_cant[x][0] = cant_cliente[x][0]
        list_cant[x][1] = cant_cliente[x][1]
    return list_cant



