# Generated by Django 4.0 on 2022-12-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_seat', models.IntegerField()),
            ],
        ),
    ]
