# Generated by Django 2.0.7 on 2018-08-10 10:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0017_documentinstance_feedback_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='templateinstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular template', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter template instance name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='templateset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular set', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter template set name', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='documentinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular document', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='templateinstance',
            name='templateset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.templateset'),
        ),
    ]