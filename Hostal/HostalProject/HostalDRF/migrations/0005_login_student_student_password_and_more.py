# Generated by Django 5.1 on 2024-08-14 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HostalDRF', '0004_remove_reservestudent_room_chocen_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='student_password',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_user',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
