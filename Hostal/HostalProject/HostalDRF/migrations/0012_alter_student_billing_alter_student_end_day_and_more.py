# Generated by Django 5.1 on 2024-08-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HostalDRF', '0011_alter_student_billing_alter_student_end_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='billing',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='end_day',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='start_day',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
