from django.urls import path
from .views import *


urlpatterns = [
    path("", start, name="start"),
    path("add_group/", add_group, name="add_group"),
    path("add_student/", add_student, name="add_student"),
    path("add_teacher/", add_teacher, name="add_teacher"),
    path("edit_student/<int:pk>", edit_student, name="edit_student"),
    path("edit_teacher/<int:pk>", edit_teacher, name="edit_teacher"),
    path("list_groups/", list_groups, name="list_groups"),
    path("list_students/", list_students, name="list_students"),
    path("list_teachers/", list_teachers, name="list_teachers"),
]
