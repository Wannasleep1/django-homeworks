from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django_testing.settings import MAX_STUDENTS_PER_COURSE
from students.models import Course, Student


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, value):
        if len(value) > MAX_STUDENTS_PER_COURSE:
            raise ValidationError("Quantity of students on the course limited by "
                                   f"{MAX_STUDENTS_PER_COURSE}.")

        return value
