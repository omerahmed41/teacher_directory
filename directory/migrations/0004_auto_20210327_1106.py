# Generated by Django 2.2.12 on 2021-03-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_auto_20210326_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='room_number',
            field=models.CharField(max_length=4),
        ),
    ]
