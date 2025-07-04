from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from app.models import Student
from . serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

"""# manually serilization of query set 
def student(request):
    student=(Student.objects.all())  #this response is coming in queryset which is not a dict object for json response
    student_list=(list(student.values())) #converted that in list and then returning in jsonResponse
    print(student_list)
    return JsonResponse(student_list,safe=False)
"""
@api_view(["GET","POST"])
def student(request):
    if request.method=="GET":
        students=Student.objects.all()
        print(f"queryset:{students.values()}")
        serializer=StudentSerializer(students,many=True)
        print(f"serilizer object :{serializer}")
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(f"post data: {serializer.data}")
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.error)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PUT":
        return JsonResponse()
    elif request.method=="PATCH":
        return JsonResponse()
    elif request.method=="Delete":
        return JsonResponse()
    else:
        return HttpResponse()
    
@api_view(["GET","POST"])   
def studentdetail(request, pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method=="GET":
        serilize=StudentSerializer(student)
        return Response(serilize.data,status=status.HTTP_200_OK)
    
    elif request.method=="POST":
        serilizer=StudentSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.error, status=status.HTTP_400_BAD_REQUEST)
    
    
        

