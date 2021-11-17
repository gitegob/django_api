from rest_framework import serializers
from app_one.models import Student


class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'age')


class GetStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')
