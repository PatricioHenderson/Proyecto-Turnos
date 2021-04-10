#!/usr/bin/env python

__author__ = "Inove Coding School"
__email__ = "INFO@INOVE.COM.AR"
__version__ = "1.0"

import traceback
import io
import sys
import os
import base64
import json
import sqlite3
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for, session


from gimnasio_usuarios_orm import db
import gimnasio_usuarios_orm as gimnasio

from config import config

app = Flask(__name__)
# Clave que utilizaremos para encriptar los datos
app.secret_key = "flask_session_key_inventada"

# Obtener la path de ejecución actual del script
script_path = os.path.dirname(os.path.realpath(__file__))

# Obtener los parámetros del archivo de configuración
config_path_name = os.path.join(script_path, 'config.ini')
db_config = config('db', config_path_name)
server_config = config('server', config_path_name)

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_config['database']}"
# Asociamos nuestro controlador de la base de datos con la aplicacion
db.init_app(app)
gimnasio.db.init_app(app)

@app.route("/")
def initial():
    try:
        return redirect(url_for('show_signup'))
    except:
        return jsonify({'trace': traceback.format_exc()})    

@app.route("/reset")
def reset():
    try:
        # Borrar y crear la base de datos
        gimnasio.create_schema()
        result = "<h3>Base de datos re-generada!</h3>"
        return (result)
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/index")
def index():
    try:
        result = "<h3> Index </h3>"
        return result
    except:
        return jsonify({'trace': traceback.format_exc()})



@app.route("/signup", methods=['GET', 'POST'])
def show_signup():
    
    if request.method == 'GET':
        try:
            return render_template('signup.html')
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == 'POST':
        try:
            name = str(request.form.get('name'))
            lastname = str(request.form.get('lastname'))
            mail = request.form.get('mail')
            document = request.form.get('document')
            password = request.form.get('password')
            password2  = request.form.get('password2')
            if (password != password2):
                impresion = "<h3>Error en la contraseña</h3>"
                return impresion
            else:
                gimnasio.insert_user(name, lastname,document, mail , password)
            
                return redirect(url_for('agendar_turno'))

        except:
            return jsonify({'trace': traceback.format_exc()})

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # Si entré por "GET" es porque acabo de cargar la página
        try:
            return render_template('login.html')
        except:
            return jsonify({'trace': traceback.format_exc()})
    

    if request.method == 'POST':
        
        mail = request.form.get('mail')
        password = request.form.get('password')

        user_validated = gimnasio.check_password(mail,password)
        
        if user_validated is False:
            # Datos ingresados incorrectos
            return render_template('login.html')

        session['user'] = mail
        if user_validated is True:
            
            return redirect(url_for('agendar_turno'))

            



@app.route("/logout")
def logout():
    try:
        session.clear()
        return redirect(url_for('login'))
    
    except:
        
        return jsonify({'trace': traceback.format_exc()})



@app.route("/turnos", methods=['GET', 'POST'])
def agendar_turno():
    
    if (session.get('user') is None):
            return redirect(url_for('login'))  

    
    if request.method == 'GET':
        try:
            mail = session['user'] 
            return render_template('calendario.html' , mail=mail )
        
        except:
            return jsonify({'trace':traceback.format_exc()})    
            
    if request.method == 'POST':     

         
        
        
        try:
            mail = session['user'] 
            date = request.form.get('date')
            
            
        
            events = [{
            'mail' : mail,
            'date' : date,
            }]
        
            return render_template('calendario.html' , events=events , mail = mail )
        
        except:
            return jsonify({'trace':traceback.format_exc()})
    

if __name__ == '__main__':
    print('Servidor arriba!')

    app.run(host=server_config['host'],
            port=server_config['port'],
            debug=True)
