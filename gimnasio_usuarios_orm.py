#!/usr/bin/env python

import os
import sqlite3

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    #Crea la clase usuario
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    lastname = db.Column(db.String)
    document = db.column(db.String )
    mail = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

def create_schema():
    db.drop_all()
    #Creamos la base de datos
    db.create_all()

def insert_user(name, lastname,document , mail, password):

    user = User.query.filter_by(mail=mail).first()
    if user:
        return None

    new_user = User(name=name, lastname=lastname ,document=document, mail=mail , password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()


def check_password(mail,password):

    user = User.query.filter_by(mail=mail).first()
    if not user:
        return False
    
    if check_password_hash(user.password, password):
        return True
    else:
        return False



