import json
from flask import Blueprint, request
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from core.apis.assignments.principal import principal_assignments_resources
from .schema import TeacherSchema


@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def principal_list_teachers ():
    """Returns list of assignments principal"""
    list_teachers = Teacher.list_all_teachers()
    list_teachers_dump = TeacherSchema ().dump (list_teachers, many=True)
    return APIResponse.respond (data=list_teachers_dump)