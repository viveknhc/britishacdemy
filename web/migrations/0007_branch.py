# Generated by Django 4.0 on 2022-12-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_course_lessons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('location', models.URLField()),
            ],
        ),
    ]
