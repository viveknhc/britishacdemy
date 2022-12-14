# Generated by Django 4.0 on 2022-02-14 12:20

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('icon', versatileimagefield.fields.VersatileImageField(upload_to='category/')),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Course Categories',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=128)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('summary', models.CharField(max_length=250)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='courses/')),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('students', models.IntegerField()),
                ('length', models.CharField(max_length=128)),
                ('effort', models.CharField(max_length=128)),
                ('institution', models.CharField(max_length=128)),
                ('subject', models.CharField(max_length=128)),
                ('language', models.CharField(max_length=128)),
                ('certificate', models.CharField(choices=[('yes', 'yes'), ('No', 'No')], max_length=128)),
                ('price', models.CharField(max_length=8)),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=350)),
                ('date', models.DateField()),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='events/')),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('description', models.CharField(max_length=350)),
                ('designation', models.CharField(max_length=350)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='testimonial/')),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350)),
                ('summary', models.CharField(max_length=555)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Blogs/')),
                ('date', models.DateField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='instructor/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.course')),
            ],
        ),
    ]
