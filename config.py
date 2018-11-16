#encoding: utf-8

import os
from datetime import timedelta

DEBUG = True
SECRET_KEY=os.urandom(24)
PERMANENT_SESSION_LIFETIME=timedelta(days=7)

#dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
# DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'wdy159'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'fuli'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
            DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
