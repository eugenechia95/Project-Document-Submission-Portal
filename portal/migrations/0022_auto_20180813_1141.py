# Generated by Django 2.0.7 on 2018-08-13 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0021_auto_20180813_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templateinstance',
            name='templateset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toset', to='portal.templateset'),
        ),
    ]