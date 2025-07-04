from django.urls import path
from . import views

urlpatterns=[
    path("student/",views.student,name="student"),
    path("student/<int:pk>/",views.studentdetail,name="studentdetail"),
]