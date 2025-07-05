from django.urls import path
from . import views

urlpatterns=[
    path("student/",views.student,name="student"),
    # function based url
    path("student/<int:pk>/",views.studentdetail,name="studentdetail"),
    #path("emply/", views.employee_detail,name="employee"), function based view 

    #class based url 
    path("employee/",views.Employees.as_view()),
    path("employees/<int:pk>/",views.Employeedetail.as_view()),
    path("employees/",views.Employeedetail.as_view()),

]