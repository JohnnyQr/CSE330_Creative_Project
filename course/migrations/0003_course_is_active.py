# Generated by Django 3.2.9 on 2021-12-05 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
    ]
