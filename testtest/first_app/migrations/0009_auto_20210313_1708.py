# Generated by Django 3.1.7 on 2021-03-13 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_auto_20210313_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bfuser',
            name='bfa_score',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Boldface',
        ),
    ]