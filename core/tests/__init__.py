import core.models.users
from core import app, db
app.testing = True
import core.models.assignments as moss
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection

db.drop_all()
db.create_all()