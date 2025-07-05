from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),

    #web end point 
    path("",include("app.urls")),

   

    #API end point 
    path("api/v1/",include("api.urls")),
   
    ]
