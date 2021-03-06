# Generated by Django 3.0.10 on 2021-03-22 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20210322_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='faculty_name',
            field=models.CharField(default='Name', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='table2',
            name='faculty_name1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fac1', to='webapp.faculty'),
        ),
        migrations.AlterField(
            model_name='table2',
            name='faculty_name2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fac2', to='webapp.faculty'),
        ),
        migrations.AlterField(
            model_name='table2',
            name='faculty_name3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fac3', to='webapp.faculty'),
        ),
        migrations.AlterField(
            model_name='table2',
            name='faculty_name4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fac4', to='webapp.faculty'),
        ),
    ]
