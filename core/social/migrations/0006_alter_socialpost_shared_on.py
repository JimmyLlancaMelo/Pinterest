# Generated by Django 5.1 on 2024-10-01 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_socialpost_shared_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialpost',
            name='shared_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
