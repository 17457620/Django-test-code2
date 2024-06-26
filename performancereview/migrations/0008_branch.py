# Generated by Django 5.0.6 on 2024-05-20 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performancereview', '0007_employee_hiredate_employee_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('branchID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('branchAddress', models.CharField(max_length=100)),
                ('employeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performancereview.employee')),
            ],
        ),
    ]
