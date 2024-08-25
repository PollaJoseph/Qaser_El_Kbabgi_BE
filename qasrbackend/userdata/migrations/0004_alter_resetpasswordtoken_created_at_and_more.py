# Generated by Django 5.1 on 2024-08-25 18:41

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_alter_resetpasswordtoken_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpasswordtoken',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='resetpasswordtoken',
            name='token',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='resetpasswordtoken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
