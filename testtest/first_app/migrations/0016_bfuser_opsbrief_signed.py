# Generated by Django 3.1.7 on 2021-03-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0015_minutes_opsbriefminutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='bfuser',
            name='opsbrief_signed',
            field=models.BooleanField(default=False),
        ),
    ]
