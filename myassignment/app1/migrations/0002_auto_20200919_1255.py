# Generated by Django 3.1.1 on 2020-09-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='routerdetails',
            name='delete_flag',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='routerdetails',
            name='Loop_back',
            field=models.CharField(default='127.0.1.1', max_length=20),
        ),
    ]
