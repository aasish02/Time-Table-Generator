# Generated by Django 4.0.5 on 2023-11-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm1', '0003_course_weight_alter_course_course_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='weight',
        ),
        migrations.AlterField(
            model_name='instructor',
            name='uid',
            field=models.CharField(max_length=6),
        ),
    ]
