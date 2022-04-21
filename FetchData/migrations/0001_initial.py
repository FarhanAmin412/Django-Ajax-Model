# Generated by Django 4.0.2 on 2022-03-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('Email', models.EmailField(max_length=100)),
                ('DateTime', models.CharField(max_length=70)),
                ('RoomTemp', models.CharField(max_length=50)),
                ('Humidity', models.CharField(max_length=50)),
                ('BodyTemp', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('Email', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=70)),
            ],
        ),
    ]