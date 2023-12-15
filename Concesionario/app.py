from flask import Flask
from flask import render_template
from flask import send_from_directory #Para obtener informacion de una imagen
import os


app=Flask(__name__)
app.secret_key="develoteca"

#----Sitio raiz
@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/img/<imagen>')
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join('templates/sitio/img/'), imagen)

#----automoviles ruta view
@app.route('/autos')
def autos():
    return render_template('sitio/autos.html')

#----Nosotros ruta view
@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')


#----ruta para el admin
@app.route('/admin')
def admin():
    return render_template('admin/index.html')

#---------------------------Login---------------------------------
@app.route('/admin/login2')
def admin_login2():
    return render_template('admin/login2.html')

@app.route('/admin/login2')
def admin_login_post2():
    return render_template('admin/login2.html')
#---------------------------Login---------------------------------

#---------------------------Registro---------------------------------
@app.route('/admin/register')
def admin_register():
    return render_template('admin/register.html')

@app.route('/admin/register/guardar')
def admin_register_guardar():
    return render_template('admin/login2.html')
#--------------------------------------------------------------------

#----ruta para cerrar el admin
@app.route('/admin/cerrar')
def admin_login_cerrar():
    session.clear()
    return redirect('/')

#----ruta para el admin
@app.route('/admin/autos')
def admin_autos():
    return render_template('admin/autos.html')

#----ruta para recepcionar los datos del /admin/autos.html  -----------------------
@app.route('/admin/autos/guardar')
def admin_autos_guardar():
    return redirect('/admin/autos')

@app.route('/admin/autos/borrar')
def admin_autos_borrar():
    return redirect('/admin/autos')


#---------------------------------------------------Carrito de compras--------------------------------
#----carrito ruta view
@app.route('/carrito')
def carrito():
    return render_template('sitio/carrito.html')


#--------------Carrito de compras---------------

@app.route('/guardar_card')
def guardar_card():
        return redirect('/autos')
    
#--------------Eliminar producto en carrito de compras------------
@app.route('/carrito/borrar')
def carrito_borrar():
    return redirect('/carrito')


#----------ERRORES--------
@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('/errores/404.html',error=error)
    
if __name__ =='__main__':
    app.run(debug=True)