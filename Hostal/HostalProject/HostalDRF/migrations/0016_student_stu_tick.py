# Generated by Django 5.1 on 2024-08-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HostalDRF', '0015_groupstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_tick',
            field=models.BooleanField(default=False),
        ),
    ]
