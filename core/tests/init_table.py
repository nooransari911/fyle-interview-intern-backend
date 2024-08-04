from marshmallow import Schema, EXCLUDE, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

import core.models.users
from core.models.autoschema import UserSchema, StudentSchema, TeacherSchema, PrincipalSchema
from core import db
from core.models.users import User

usx = [
    {
    "id": 1,
    "username": "/st1",
    "email": "@st1"
    },
    {
    "id": 2,
    "username": "/st2",
    "email": "@st2"
    },

    {
    "id": 3,
    "username": "/te1",
    "email": "@te1"
    },
    {
    "id": 4,
    "username": "/te2",
    "email": "@te2"
    },

    {
    "id": 5,
    "username": "/pr1",
    "email": "@pr1"
    }
]


stx = [
    {
        "id": 1,
        "user_id": 1
    },
    {
        "id": 2,
        "user_id": 2
    }
]

tex = [
    {
        "id": 1,
        "user_id": 3
    },
    {
        "id": 2,
        "user_id": 4
    }
]

prx = [
    {
        "id": 1,
        "user_id": 5
    }
]


def init_table ():
    db.create_all()

    usxload = UserSchema (many=True)
    us = usxload.load (usx, session=db.session)
    [db.session.add(x) for x in us]

    stxload = StudentSchema (many=True)
    st = stxload.load(stx, session=db.session)
    [db.session.add(x) for x in st]

    texload = TeacherSchema(many=True)
    te = texload.load(stx, session=db.session)
    [db.session.add(x) for x in te]

    prxload = PrincipalSchema (many=True)
    pr = prxload.load(stx, session=db.session)
    [db.session.add(x) for x in pr]
    
    db.session.commit()