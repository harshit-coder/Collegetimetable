# Generated by Django 3.0.10 on 2021-03-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20210319_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='part1',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th')], default='1st', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='sem1',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th')], default='1st', max_length=100, null=True),
        ),
    ]
