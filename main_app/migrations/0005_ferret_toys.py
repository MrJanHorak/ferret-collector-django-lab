# Generated by Django 3.2.7 on 2021-11-21 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_toy'),
    ]

    operations = [
        migrations.AddField(
            model_name='ferret',
            name='toys',
            field=models.ManyToManyField(to='main_app.Toy'),
        ),
    ]
