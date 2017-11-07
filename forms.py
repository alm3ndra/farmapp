from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required


class FLogin(FlaskForm):
    usuario = StringField('NOMBRE DE USUARIO', validators=[Required()])
    password = PasswordField('CONTRASEÑA', validators=[Required()])
    enviar = SubmitField('INGRESAR')


class FProductos(FlaskForm):
    producto = StringField('INGRESE EL NOMBRE DEL PRODUCTO', validators=[Required()])
    enviar = SubmitField('BUSCAR')

class FClientes(FlaskForm):
    cliente = StringField('INGRESE EL NOMBRE DEL CLIENTE', validators=[Required()])
    enviar = SubmitField('BUSCAR')


