# Generated by Django 4.1.3 on 2022-12-01 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='a1',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='hdate',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='dep',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='doc',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='hname',
            new_name='mail',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='m1',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='t1',
            new_name='time',
        ),
    ]