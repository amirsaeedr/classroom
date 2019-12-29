from django.db import models

# Create your models here.
from apps.profiles.models import Profile


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="teacher", default="0")
    students = models.ManyToManyField(Profile, related_query_name="student_course")

    def __str__(self):
        return self.course_name
