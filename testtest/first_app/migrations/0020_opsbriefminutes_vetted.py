# Generated by Django 3.1.7 on 2021-03-30 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0019_opsbriefminutes_type_of_minutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='opsbriefminutes',
            name='vetted',
            field=models.BooleanField(default=False),
        ),
    ]
