# Generated by Django 5.1 on 2024-10-01 20:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_socialpost_shared_body_socialpost_shared_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialpost',
            name='shared_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
