from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .forms import *
# Create your views here.



@api_view(['GET'])
def EmployeeList(request):
    emp = Employee.objects.all()
    serializer = EmployeeSerializer(emp,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Employeedetail(request,pk):
    emp = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(emp,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def EmployeeCreate(request):
    form = EmployeeForm(data=request.POST)
    if form.is_valid():
        serializer = EmployeeSerializer(data=form.cleaned_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'successfully created'}, status=status.HTTP_201_CREATED)
        else:
           data = {"data": "Invaild Data"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    data = {'data': form._errors}
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def EmployeeUpdate(request,pk):
    emp = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=emp, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def EmployeeDelete(request,pk):
    art = Employee.objects.get(id=pk)
    art.delete()
    return Response('Deleted')

