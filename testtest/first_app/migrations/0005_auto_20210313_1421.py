# Generated by Django 3.1.7 on 2021-03-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_bfuser_egressbf'),
    ]

    operations = [
        migrations.AddField(
            model_name='egressbf',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='egressbf',
            name='bf1',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='egressbf',
            name='bf2',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='egressbf',
            name='bf3',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='egressbf',
            name='bf4',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='egressbf',
            name='bf5',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='egressbf',
            name='bf6',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]