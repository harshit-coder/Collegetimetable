# Generated by Django 3.0.10 on 2021-03-19 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20210319_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='sem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th')], default='1st', max_length=100, null=True)),
                ('show1', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='off_day',
            field=models.CharField(choices=[('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], default='MONDAY', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='room_no',
            name='room',
            field=models.CharField(default='1', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='part1',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th')], default='1st', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='sem1',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th')], default='1st', max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_name', models.CharField(default='Science', max_length=200)),
                ('paper_code', models.CharField(default='0123', max_length=30)),
                ('duration', models.PositiveIntegerField(default=1)),
                ('Course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Course')),
            ],
        ),
    ]