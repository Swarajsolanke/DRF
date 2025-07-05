from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from app.models import Student
from . serializers import StudentSerializer,EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from employee.models import Employee
from rest_framework.views import APIView #creating class based view 
from django.http import Http404
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
        #print(f"queryset:{students.values()}")
        serializer=StudentSerializer(students,many=True)
        #print(f"serilizer object :{serializer}")
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print(f"post data: {serializer.data}")
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        #print(serializer.error)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PUT":
        return JsonResponse()
    elif request.method=="PATCH":
        return JsonResponse()
    elif request.method=="Delete":
        return JsonResponse()
    else:
        return HttpResponse()
    
@api_view(["GET","POST","PUT","PATCH","DELETE"])   
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
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PUT":
        serilizer=StudentSerializer(student,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            print(f"serilizer data:{serilizer.data}")
            return Response(serilizer.data, status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PATCH":
        serilize=StudentSerializer(student,data=request.data)
        if serilize.is_valid():
            serilize.save()
            print(f"serilizer data:{serilize.data}")
            return Response(serilize.data,status=status.HTTP_200_OK)
        print(serilize.errors)
        
        return Response(serilize.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#without using serilization module 
""""
@api_view(["GET"])    
def employee_detail(request):
    if request.method=="GET":
        employees=Employee.objects.all()
        print(f"employees deatails:{employees.values()}")
        employe_details=list(employees.values())
        return JsonResponse(employe_details,safe=False)
   """

""""
function based view 
@api_view(["GET"])      #for rendering rest_framework api 
def employee_detail(request):
    if request.method=="GET":
        employees=Employee.objects.all()
        print(employees.values())
        serialize=EmployeeSerializer(employees,many=True)
        return Response(serialize.data,status=status.HTTP_200_OK) 
      
    elif request.method=="POST":
        pass
"""

#class based view
class Employees(APIView):
    #instance method 
    def get(self,request):
        employ=Employee.objects.all()
        serilizer=EmployeeSerializer(employ, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serilizer=EmployeeSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            print(f"serilizer object:{serilizer.data}")
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


class Employeedetail(APIView):
    def get_object(self, pk):
        try:
            
            employ=Employee.objects.get(pk=pk)
            return employ
        except Employee.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        employ=self.get_object(pk)
        serilizer=EmployeeSerializer(employ)
        return Response(serilizer.data,status=status.HTTP_200_OK)
    def get_all(self, request):
        employ=Employee.objects.all()
        serilizer=EmployeeSerializer(employ, many=True)
        return Response(serilizer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        serilizer=EmployeeSerializer(self.get_object(pk),data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_200_OK)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        serilizer=EmployeeSerializer(data=self.data.request)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    


        

