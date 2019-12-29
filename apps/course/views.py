from rest_framework import viewsets

from apps.course.models import Course
from apps.course.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
