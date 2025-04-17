from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="student_list"),
    path("add/", views.add_student, name="add_student"),
    path("view/<slug:slug>/", views.view_student, name="view_student"),  # Correct pattern
    path("edit/<slug:slug>/", views.edit_student, name="edit_student"),
    path("delete/<slug:slug>/", views.delete_student, name="delete_student"),
]
