# Generated by Django 2.0.7 on 2018-08-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_auto_20180810_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentinstance',
            name='dor',
            field=models.DateField(blank=True, null=True),
        ),
    ]