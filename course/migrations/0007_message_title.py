# Generated by Django 3.2.9 on 2021-12-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='title'),
        ),
    ]