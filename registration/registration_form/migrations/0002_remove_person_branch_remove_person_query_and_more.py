# Generated by Django 4.0.1 on 2022-03-15 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='person',
            name='query',
        ),
        migrations.RemoveField(
            model_name='person',
            name='year',
        ),
        migrations.AddField(
            model_name='person',
            name='message',
            field=models.TextField(default='Null', max_length=500),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
