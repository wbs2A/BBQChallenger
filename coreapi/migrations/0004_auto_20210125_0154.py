# Generated by Django 3.1.5 on 2021-01-25 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coreapi', '0003_barbeque__date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='guests',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.AddField(
            model_name='employee',
            name='guest',
            field=models.BooleanField(blank=True, default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='guest_drink',
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]
