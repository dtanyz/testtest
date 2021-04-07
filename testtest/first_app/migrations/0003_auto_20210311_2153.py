# Generated by Django 3.1.7 on 2021-03-11 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boldface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boldface_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='boldface',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='first_app.boldface'),
        ),
    ]
