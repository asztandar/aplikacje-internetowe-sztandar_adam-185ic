# Generated by Django 3.1.5 on 2021-01-07 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210107_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='addTime',
            field=models.DateField(),
        ),
    ]
