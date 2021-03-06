# Generated by Django 3.0.1 on 2019-12-29 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20191229_2130'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_query_name='student_course', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='profiles.Profile'),
        ),
    ]
