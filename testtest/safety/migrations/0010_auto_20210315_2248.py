# Generated by Django 3.1.7 on 2021-03-15 21:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety', '0009_auto_20210315_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safetyalertmsg',
            name='sam_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]