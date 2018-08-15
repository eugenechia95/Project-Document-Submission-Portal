# Generated by Django 2.0.7 on 2018-08-15 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0033_templateinstance_refdoc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.City'),
        ),
        migrations.AlterField(
            model_name='project',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.Country'),
        ),
    ]
