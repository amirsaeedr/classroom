# Generated by Django 3.0.1 on 2019-12-29 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Role'),
        ),
    ]
