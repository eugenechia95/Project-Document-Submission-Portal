# Generated by Django 2.0.7 on 2018-08-08 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_project_personnel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='personnel',
        ),
    ]