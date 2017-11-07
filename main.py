#!/usr/bin/env python


# CSV----------------------
import csv
import validate
import class_csv

# DATETIME
from datetime import datetime

#MODULO DE FUNCIONES------
import listados_module

#FLASK FRAMEWORK (WEB APP)
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager

# FORMULARIOS -----------
from forms import FLogin, FProductos, FClientes

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

# CSV Y VALIDACION
nombre_de_archivo = 'farmacia.csv'
validate.validar(nombre_de_archivo)
registros = class_csv.genera_clase(nombre_de_archivo)

# LOCAL BOOTSTRAP FRAMEWORK (CSS)
app.config['SECRET_KEY'] = 'llaves'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

# ERRORES POSIBLES
@app.errorhandler(404)
def no_encontrado(e):
    if 'username' in session:
        return render_template('404.html'), 404
    else:
        flash('NO SE ENCONTRARON COINCIDENCIAS.')
        return redirect(url_for('ingresar'))

@app.errorhandler(500)
def error_interno(e):
    if 'username' in session:
        return render_template('500.html'), 500
    else:
        flash('OCURRIO UN ERROR EN EL SERVIDOR')
        return redirect(url_for('ingresar'))


# WEBPAGES

#INDEX
@app.route('/')
def index():
    return render_template('index.html')


#INTRO BIENVENIDA
@app.route('/farmapp')
def indexB():
    if 'username' in session:
        return render_template('indexB.html')
    else:
        flash('DEBE LOGUEARSE')
        return redirect(url_for('ingresar'))

# LOG IN
@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    formulario = FLogin()
    if formulario.validate_on_submit():
        with open('usuarios') as archivo:
            archivo_csv = csv.reader(archivo)
            register = next(archivo_csv)
            while register:
                if formulario.usuario.data == register[0] and formulario.password.data == register[1]:
                    flash('BIENVENIDO '+ formulario.usuario.data)
                    session['username'] = formulario.usuario.data
                    return redirect(url_for('ultimas'))
                register = next(archivo_csv, None)
            else:
                flash('USUARIO O CONTRASEÑA INVALIDOS, VUELVA A INTENTARLO.')
                return redirect(url_for('ingresar'))
    return render_template('login.html', formulario=formulario)


# LOGOUT
@app.route('/logout', methods=['GET'])
def logout():
    if 'username' in session:
        session.pop('username')
        return render_template('logout.html')
    else:
        return redirect(url_for('index'))

# ULTIMOS MOVIMIENTOS DE VENTA
@app.route('/ultimas', methods=['GET', 'POST'])
def ultimas():
    if 'username' in session:   
        ultimos = 10
        last_s = []
        last_s=listados_module.listar_ventas(registros, ultimos)
        return render_template('last.html',last_s=last_s)
    else:
        flash('DEBE LOGUEARSE PARA PODER INGRESAR')
        return redirect(url_for('ingresar'))


# BUSQUEDA POR CLIENTE----------
@app.route('/prod_clientes', methods=['GET', 'POST'])
def prod_clientes():
    if 'username' in session:
        formulario = FClientes()
        if formulario.validate_on_submit():
            cliente = formulario.cliente.data.upper()
            if len(cliente) < 3:
                flash('DEBE INGRESAR UN MINIMO DE 3 CARACTERES')
                return render_template('prod_clientes.html', form = formulario)
            else:
                val = listados_module.encontrar_clientes(registros,cliente)#llama a funcion para validar si exiten los clientes
                if len(val) == 0:
                    flash('NO SE ENCONTRARON COINCIDENCIAS EN EL REGISTRO')
                elif len(val) == 1:
                    listar = listados_module.listar_productos_cliente(registros,cliente)
                    return render_template('prod_clientes.html', form = formulario, listar = listar, cliente= formulario.cliente.data.upper())
                else:
                    flash('SE ENCONTRARON COINCIDENCIAS, SELECCIONE UNA.')
                    return render_template('prod_clientes.html', form = formulario, clientes = val)
        return render_template('prod_clientes.html', form = formulario)
    else:
        flash('DEBE ESTAR LOGUEADO PARA ACCEDER')
        return redirect(url_for('ingresar'))


# CLIENTES MULTIPLES-----------------------
@app.route('/prod_clientes/<clientes>', methods=['GET', 'POST'])
def prod_clientes2(clientes):
    if 'username' in session:
        formulario = FClientes()
        if formulario.validate_on_submit():
            cliente = formulario.cliente.data.upper()
            if len(cliente) < 3:
                flash('SON NECESARIOS AL MENOS 3 CARACTERES EN EL CAMPO DE BUSQUEDA')
                return redirect(url_for('prod_clientes'))
            else:
                val = listados_module.encontrar_clientes(registros,cliente)
                if len(val) == 0:
                    flash('NO SE ENCONRARON COINCIDENCIAS EN EL REGISTRO')
                    return redirect(url_for('prod_clientes'))                   
                elif len(val) == 1:
                    listar = listados_module.listar_productos_cliente(registros,cliente)
                    return render_template('prod_clientes.html', form = formulario, listar = listar, cliente= formulario.cliente.data.upper())
                else:
                    flash('SE ENCONRARON COINCIDENCIAS, SELECCIONE UNA POR FAVOR')
                    return render_template('prod_clientes.html', form = formulario, clientes = val)
        else:
            cliente = clientes
            val = listados_module.encontrar_clientes(registros,cliente)
            listar = listados_module.listar_productos_cliente(registros,cliente)
            return render_template('prod_clientes.html', form = formulario, listar = listar, cliente= cliente)
    else:
        flash('Para Acceder debe Loguearse')
        return redirect(url_for('ingresar'))

# CLIENTES CON HISTORIAL DE COMPRA
@app.route('/clientes_prod', methods=['GET', 'POST'])
def clientes_prod():
    if 'username' in session:
        formulario = FProductos()
        if formulario.validate_on_submit():
            producto = formulario.producto.data.upper()
            if len(producto) < 3:
                flash('SE REQUIEREN AL MENOS 3 CARACTERES EN EL CAMPO DE BUSQUEDA.')
                return render_template('clientes_prod.html', form=formulario)
            else:
                val = listados_module.encontrar_productos(registros, producto)
                if len(val) == 0:
                    flash('NO SE ENCONTRARON COINCIDENCIAS EN EL REGISTRO.')
                elif len(val) == 1:
                    listar = listados_module.listar_clientes_producto(registros,producto)
                    return render_template('clientes_prod.html', form = formulario, listar = listar, producto= formulario.producto.data.upper())
                else:
                    flash('SE ENCONTRARON COINCIDENCIAS, SELECCIONE UNA.')
                    return render_template('clientes_prod.html', form = formulario, productos = val)
        return render_template('clientes_prod.html', form=formulario)
    else:
        flash('DEBE LOGUEARSE PARA PODER ACCEDER AL SISTEMA')
        return redirect(url_for('ingresar'))

# CLIENTES MULTIPLES
@app.route('/clientes_prod/<productos>', methods=['GET', 'POST'])
def cliente_prod2(productos):
    if 'username' in session:
        formulario = FProductos()
        if formulario.validate_on_submit():
            producto = formulario.producto.data.upper()
            if len(producto) < 3:
                flash('SE REQUIEREN AL MENOS 3 CARACTERES EN EL CAMPO DE BUSQUEDA')
                return redirect(url_for('clientes_prod'))
            else:
                val = listados_module.encontrar_productos(registros,producto)
                if len(val) == 0:
                    flash('NO SE ENCONTRARON COINCIDENCIAS EN EL REGISTRO.')
                    return redirect(url_for('clientes_prod'))                   
                elif len(val) == 1:
                    listar = listados_module.listar_clientes_producto(registros,producto)
                    return render_template('clientes_prod.html', form = formulario, listar = listar, producto= formulario.producto.data.upper())
                else:
                    flash('SE ENCONTRARON COINCIDENCIAS, SELECCIONE UNA.')
                    return render_template('clientes_prod.html', form = formulario, productos = val)
        else:
            producto = productos
            val = listados_module.encontrar_productos(registros,producto)
            listar = listados_module.listar_clientes_producto(registros,producto)
            return render_template('clientes_prod.html', form = formulario, listar = listar, producto = producto)
    else:
        flash('DEBE LOGUEARSE PARA PODER ACCEDER AL SISTEMA')
        return redirect(url_for('ingresar'))



# LISTA PRODUCTOS VENDIDOS
@app.route('/prod_vendidos', methods=['GET', 'POST'])
def prod_vendidos():
    if 'username' in session:
        produc = []
        cantidad = 10
        produc = listados_module.prod_vendidos(registros = registros, cantidad=cantidad)
        return render_template('prod_vendidos.html', produc = produc)
    else:
        flash('DEBE LOGUEARSE PARA PODER ACCEDER AL SISTEMA')
        return redirect(url_for('ingresar'))


# LISTA DE CLIENTES QUE MAS GASTARON
@app.route('/mej_clientes', methods=['GET', 'POST'])
def mej_clientes():
    if 'username' in session:
        produc = []
        cantidad = 10
        produc = listados_module.clientes_gastadores(registros = registros, cantidad=cantidad)
        return render_template('mej_clientes.html', produc = produc)
    else:
        flash('DEBE LOGUEARSE PARA PODER ACCEDER AL SISTEMA')
        return redirect(url_for('ingresar'))


# MAIN LOOP
if __name__ == "__main__":
    manager.run()
