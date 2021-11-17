from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from app_one.models import Student
from app_one.serializers import CreateStudentSerializer, GetStudentSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_students(request):
    qs = Student.objects.all()
    studentLength = qs.__len__()
    serializer = GetStudentSerializer(qs, many=True)
    return Response({'data': serializer.data, 'length': studentLength})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_student(request):
    serializer = CreateStudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400, exception=True)
