# Generated by Django 2.0.7 on 2018-08-13 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0028_auto_20180813_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familymember',
            name='profile',
        ),
        migrations.DeleteModel(
            name='FamilyMember',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]