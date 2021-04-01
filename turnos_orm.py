#!/usr/bin/env python

import os
import sqlite3

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import calendar


def Calendario(db.Model):

    calendario = calendar.TextCalendar(calendar.MONDAY)
    print(calendario.formatyear(2021))
    __tablename__ "calendario"
    id =  db.Column(db.integer,primary_key=True)
def create_schema():
    if counter = 1:
        pass
    if counter = 0:
        db.drop_all()
        db.create_all()
        counter += 1

    
