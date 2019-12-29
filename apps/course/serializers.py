from rest_framework import serializers

from apps.course.models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'teacher', 'students']
