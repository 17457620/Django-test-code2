# Generated by Django 5.0.6 on 2024-05-20 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performancereview', '0004_alter_employee_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='image',
        ),
    ]