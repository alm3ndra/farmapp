#!/usr/bin/python3

# VALIDACION DE ENTRADA DE DATOS APERTURA DE ARCHIVOS
def validar(nombre_archivo):
    import csv
    class RegistroExcede(Exception):
        pass

    class MiError(Exception):
        pass
    CAMPOS = 5 
    try:
        with open(nombre_archivo, 'r', encoding='latin-1') as archivo:
            print('FILE OPENED')
            archivo_csv=csv.reader(archivo)
            registro = 1
            campo = 1
            for linea in archivo_csv:
                if len (linea) != CAMPOS:
                    raise RegistroExcede()
                else:
                    x=0
                    for x in range(CAMPOS):
                        campo = x + 1
                        if linea[x] == '':
                            error= 'EL CAMPO {} SE ENCUENTRA VACIO EN: {}'.format(campo, registro)
                            raise MiError(error)
                        else:
                            pass
                        if registro == 1:
                            w_column = linea[x].strip(' ')
                            w_column = w_column.upper()
                            if w_column == 'PRECIO':
                                colum_precio = x
                            elif w_column =='CANTIDAD':
                                colum_cantidad = x
                            else:
                                pass                 
                        else:
                            if x == colum_cantidad:
                                val_columa=int(float(linea[x]))
                            elif x == colum_precio:
                                w_column = linea[x].strip(' ')
                                if w_column.isdigit() == True:
                                    raise ValueError()
                                else:
                                    f=float(linea[x])                            
                            else:
                                pass
           
                registro = registro + 1
            print('FILE OK')                 
    except FileNotFoundError:
        print('NO SE ENCONTRO EL ARCHIVO')
    except PermissionError:
        print('NO TIENE LOS PERMISOS NECESARIOS')
    except RegistroExcede:
        mensaje='{} LOS CAMPOS NO SON CORRECTOS'.format(linea)
        print(mensaje)
        with open('Error.log','w') as error_file:
            error_file.write(mensaje)
    except ValueError:
        if x == colum_cantidad:
            print('EL REGISTRO {} TIENE UN CALOR INCORRECTO EN "CANTIDAD'.format(registro))
        else:
            print('El Registro {} TIENE UN VALOR INCORRECTO EN "PRECIO"'.format(registro, x))







