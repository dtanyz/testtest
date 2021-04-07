# Generated by Django 3.1.7 on 2021-03-21 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0017_auto_20210321_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absentee',
            name='absent_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.bfuser'),
        ),
        migrations.AlterField(
            model_name='absentee',
            name='minutes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.opsbriefminutes'),
        ),
    ]