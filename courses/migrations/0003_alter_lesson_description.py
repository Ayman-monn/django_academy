# Generated by Django 5.0.3 on 2024-03-05 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_description_alter_course_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
