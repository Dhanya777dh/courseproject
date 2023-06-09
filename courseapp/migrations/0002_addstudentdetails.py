# Generated by Django 3.2.18 on 2023-05-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addstudentdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('studentid', models.IntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('emailid', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=255)),
                ('parentname', models.CharField(max_length=255)),
                ('parentmobile', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('date', models.DateField()),
            ],
        ),
    ]
