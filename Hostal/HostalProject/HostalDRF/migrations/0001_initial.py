# Generated by Django 5.1 on 2024-08-13 20:00

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ChosenRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomBlock', models.IntegerField()),
                ('RoomNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=100)),
                ('Password', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Block', models.IntegerField()),
                ('RoomNumber', models.IntegerField()),
                ('Capacity', models.IntegerField()),
                ('NumOfPeopleInRoom', models.IntegerField()),
                ('PricePerDay', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rooms', models.ForeignKey(on_delete=builtins.callable, to='HostalDRF.room')),
            ],
        ),
        migrations.CreateModel(
            name='MathRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rooms', models.ForeignKey(on_delete=builtins.callable, to='HostalDRF.room')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('NumOfGuest', models.IntegerField()),
                ('StartDay', models.DateTimeField()),
                ('EndDay', models.DateTimeField()),
                ('Billing', models.DecimalField(decimal_places=3, max_digits=10)),
                ('RoomChoisen', models.ForeignKey(on_delete=builtins.callable, to='HostalDRF.chosenroom')),
                ('RoomIs', models.ForeignKey(on_delete=builtins.callable, to='HostalDRF.room')),
            ],
        ),
        migrations.CreateModel(
            name='FullRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rooms', models.ForeignKey(on_delete=builtins.callable, to='HostalDRF.room')),
            ],
        ),
        migrations.CreateModel(
            name='EmptyRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rooms', models.ForeignKey(on_delete=builtins.callable, to='HostalDRF.room')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Feild', models.CharField(choices=[('field1', 'Math'), ('feild2', 'Medical')], max_length=100)),
                ('StartDay', models.DateTimeField()),
                ('EndDay', models.DateTimeField()),
                ('Billing', models.DecimalField(decimal_places=3, max_digits=10)),
                ('RoomChoisen', models.ForeignKey(on_delete=builtins.callable, to='HostalDRF.chosenroom')),
                ('RoomIs', models.ForeignKey(on_delete=builtins.callable, to='HostalDRF.room')),
            ],
        ),
    ]
