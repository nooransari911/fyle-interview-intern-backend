from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from core.models.users import User
from core.models.teachers import Teacher
from core.models.students import Student
from core.models.principals import Principal
from marshmallow import Schema, EXCLUDE, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field


class UserSchema (SQLAlchemyAutoSchema):
    class Meta:
        model = User
        unknown = EXCLUDE
        include_relationships = True
        load_instance = True

class StudentSchema (SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        unknown = EXCLUDE
        include_relationships = True
        load_instance = True


class TeacherSchema (SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE
        include_relationships = True
        load_instance = True


class PrincipalSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Principal
        unknown = EXCLUDE
        include_relationships = True
        load_instance = True