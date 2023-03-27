from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import *
from . serializers import *
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.


class Student_view(generics.ListCreateAPIView):
    queryset= MemberCommunicationType.objects.all()
    serializer_class= MemberCommunicationTypeSerializeres

# @api_view(['GET'])
# def std(request):
#      students_obj=student.objects.all()
#      serializer= StudentSerializeres(students_obj,many = True)
#      return Response({'status':200, 'payload':serializer.data})
    
# class StudentApi(APIView) :
#     def get(self,request):
#         students_obj=student.objects.all()
#         serializer= StudentSerializeres(students_obj,many = True)
#         return Response({'status':200, 'payload':serializer.data})

#         pass
    # def post(self,request):
    #   data=request.data
    #   serializer= StudentSerializeres(data=request.data)

    #   if not serializer.is_valid() :
    #       print(serializer.errors)
    #       return Response({'status':403,'errors': serializer.errors, 'message' : 'something  is wrong'})
    
    #   serializer.save()
    #   return Response({'status':200,'payload': serializer.data,'message':'yousent the data'})
    #   pass
    # def put(self,request):
    #     pass
    # def patch(self,request):
    #     pass
    # def delete(self,request):
    #     pass 
       

# @api_view(['POST'])
# def post_data(request):
#     data=request.data
#     serializer= StudentSerializeres(data=request.data)

#     if not serializer.is_valid() :
#         print(serializer.errors)
#         return Response({'status':403,'errors': serializer.errors, 'message' : 'something  is wrong'})
    
#     serializer.save()
#     return Response({'status':200,'payload': serializer.data,'message':'yousent the data'})

# @api_view(['PATCH'])
# def update_student(request,id):
#     try :
#         student_obj= student.objects.get(id=id)
#         serializer= StudentSerializeres(student_obj,data=request.data,partial=True)

#         if not serializer.is_valid() :
#             print(serializer.errors)
#             return Response({'status':403,'errors': serializer.errors, 'message' : 'something  is wrong'})
    
#         serializer.save()
#         return Response({'status':200,'payload': serializer.data,'message':'yousent the data'})
#     except  Exception as e :
#         return Response({'status':403,'message':'invalid id'})
         