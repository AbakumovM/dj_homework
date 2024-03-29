from django.forms import ValidationError
from rest_framework import serializers

from students.models import Course, Student
from django.conf import settings

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")


