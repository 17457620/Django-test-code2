# Generated by Django 5.0.6 on 2024-05-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performancereview', '0009_alter_branch_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performancereview',
            name='dateOfReview',
            field=models.DateField(max_length=30),
        ),
        migrations.AlterField(
            model_name='performancereview',
            name='timeOfReview',
            field=models.TimeField(max_length=30),
        ),
    ]
