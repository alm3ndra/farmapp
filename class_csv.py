#!/usr/bin/python3

# IMPORT CSV Y SE GENERA UNA CLASE PARA ATRAPAR LOS CAMPOS DEL ARCHIVO "DB"
import csv
def genera_clase(nombre_archivo):
    class Csv:
        def __init__ (self, cliente, codigo, producto, cantidad, precio):
            self.cliente = cliente
            self.codigo = codigo
            self.producto = producto
            self.cantidad = cantidad
            self.precio = precio
        def __str__ (self):
            return '{}, {}, {}, {}, {}'.format(self.cliente, self.codigo, self.producto, self.cantidad, self.precio)
        def __repr__ (self):
            return '{}, {}, {}, {}, {}'.format(self.cliente, self.codigo, self.producto, self.cantidad, self.precio)
        def __gt__ (self, otro):
            return self.cantidad > otro.cantidad
        def compra (self):
            return self.cantidad * self.precio

    col_cliente = 0
    col_codigo = 0
    col_producto = 0
    col_cantidad = 0
    col_precio = 0
    col_detec_campo = 0
    registros = []

    with open(nombre_archivo, 'r', encoding = 'latin-1') as archivo:
        archivo_csv = csv.reader(archivo)
        a = 0
        for linea in archivo_csv:
            if a == 0:
                b = 0
                for b in range(5):
                    detec_campo = linea[b].strip(' ')
                    detec_campo = detec_campo.upper()
                    if detec_campo == 'CLIENTE':
                        col_cliente = b
                    elif detec_campo == 'CODIGO':
                        col_codigo = b
                    elif detec_campo == 'PRODUCTO':
                        col_producto = b
                    elif detec_campo == 'CANTIDAD':
                        col_cantidad = b
                    else:
                        col_precio = b
                    b = b + 1
                a = a + 1

            else:
                registros.append(Csv(cliente = linea[col_cliente].strip(' ').upper(), codigo = linea[col_codigo].strip(' '), producto = linea[col_producto].strip(' ').upper(), cantidad = float(linea[col_cantidad].strip(' ')), precio = float(linea[col_precio].strip(' '))))
    return (registros)

                

            
    

