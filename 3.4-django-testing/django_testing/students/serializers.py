from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.conf import settings
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, value):
        if len(value) > settings.MAX_STUDENTS_PER_COURSE:
            raise ValidationError("Quantity of students on the course limited by "
                                  f"{settings.MAX_STUDENTS_PER_COURSE}.")

        return value
