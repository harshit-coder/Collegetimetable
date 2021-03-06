# Generated by Django 3.0.10 on 2021-03-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_table2_faculty_name2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table2',
            name='paper_code1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='table2',
            name='paper_name1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='table2',
            name='time',
            field=models.CharField(blank=True, choices=[('08.30 TO 09.30', '08.30 TO 09.30'), ('09.30 TO 10.30', '09.30 TO 10.30'), ('10.30 TO 11.30', '10.30 TO 11.30'), ('11.30 TO 12.30', '11.30 TO 12.30'), ('12.30 TO 01.30', '12.30 TO 01.30'), ('01.30 TO 02.30', '01.30 TO 02.30'), ('02.30 TO 03.30', '02.30 TO 03.30'), ('03.30 TO 04.30', '03.30 TO 04.30'), ('04.30 TO 05.30', '04.30 TO 05.30')], max_length=100, null=True),
        ),
    ]
