from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()   #created the object Default routers 
router.register("employees",views.EmployeeViewSet,basename="employee") #register this router 

urlpatterns=[
   # path("student/",views.student,name="student"),
    # function based url
    #path("student/<int:pk>/",views.studentdetail,name="studentdetail"),
    #path("emply/", views.employee_detail,name="employee"), function based view 

    #class based url 
   # path("employee/",views.Employees.as_view()),
    #path("employees/<int:pk>/",views.Employeedetail.as_view()),
    #path("employees/",views.Employeedetail.as_view()),

  # include the router urls 
    path("",include(router.urls)),
    path("blog/",views.Blogview.as_view()),
    path("comment/",views.Commentview.as_view()),

]