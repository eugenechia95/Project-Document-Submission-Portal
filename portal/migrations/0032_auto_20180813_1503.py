# Generated by Django 2.0.7 on 2018-08-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0031_auto_20180813_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templateinstance',
            name='title',
        ),
        migrations.AddField(
            model_name='templateinstance',
            name='name',
            field=models.CharField(default='NIL', help_text='Enter phase name', max_length=200),
        ),
    ]
