# Generated by Django 3.0.4 on 2020-05-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20200504_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='module1_advantages',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='module1_obstacles',
            field=models.CharField(max_length=300),
        ),
    ]
