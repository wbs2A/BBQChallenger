# Generated by Django 3.1.5 on 2021-01-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='guests',
        ),
        migrations.AddField(
            model_name='employee',
            name='guests',
            field=models.ManyToManyField(blank=True, to='coreapi.Guest'),
        ),
    ]
