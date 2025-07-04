from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def student(request):
    data =[
        {"name":"john",
        "age":20,
        "city":"new york",
    }]
    return HttpResponse(data)
