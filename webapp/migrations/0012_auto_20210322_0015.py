# Generated by Django 3.0.10 on 2021-03-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20210322_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='show',
            field=models.BooleanField(),
        ),
    ]
