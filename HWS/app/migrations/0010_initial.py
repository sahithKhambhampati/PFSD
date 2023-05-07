# Generated by Django 4.1.3 on 2022-12-02 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0009_delete_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalname', models.CharField(max_length=200)),
                ('specialistname', models.CharField(max_length=200)),
                ('pname', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=10)),
            ],
        ),
    ]
