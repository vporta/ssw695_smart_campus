# Generated by Django 2.1.1 on 2018-10-06 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20181006_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleboardcomputer',
            name='single_board_computer_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Singleboardcomputertype'),
        ),
    ]
