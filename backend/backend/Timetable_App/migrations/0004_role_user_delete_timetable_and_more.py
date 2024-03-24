# Generated by Django 5.0.3 on 2024-03-24 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timetable_App', '0003_classroom_timetable_remove_section_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Timetable_App.role')),
            ],
        ),
        migrations.DeleteModel(
            name='Timetable',
        ),
        migrations.RemoveField(
            model_name='course',
            name='max_students',
        ),
        migrations.RemoveField(
            model_name='course',
            name='preferred_day',
        ),
        migrations.RemoveField(
            model_name='course',
            name='preferred_end_time',
        ),
        migrations.RemoveField(
            model_name='course',
            name='preferred_start_time',
        ),
    ]
