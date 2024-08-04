from marshmallow import Schema, EXCLUDE, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_enum import EnumField
from core.models.assignments import Teacher
from core.libs.helpers import GeneralObject


class TeacherSchema (SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE
        include_relationships = True
        load_instance = True