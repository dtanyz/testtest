# Generated by Django 3.1.7 on 2021-03-15 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety', '0006_remove_safetyalertmsg_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='safetyalertmsg',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]
