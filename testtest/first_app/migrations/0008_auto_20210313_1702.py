# Generated by Django 3.1.7 on 2021-03-13 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_allaboldface'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='egressbf',
            name='bf_user',
        ),
        migrations.DeleteModel(
            name='AbortBF',
        ),
        migrations.DeleteModel(
            name='EgressBF',
        ),
    ]
