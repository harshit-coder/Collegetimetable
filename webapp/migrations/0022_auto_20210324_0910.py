# Generated by Django 3.0.10 on 2021-03-24 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_auto_20210323_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table2',
            name='room1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rom1', to='webapp.room_no', verbose_name='Choose the room'),
        ),
    ]