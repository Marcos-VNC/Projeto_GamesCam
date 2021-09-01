# Generated by Django 3.2.6 on 2021-09-01 14:09

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210901_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='dataLançamento',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 1, 14, 9, 37, 101353, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='ImagesGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img01', models.ImageField(blank=True, upload_to='imagesGame/%y/%m/%d/')),
                ('img02', models.ImageField(blank=True, upload_to='imagesGame/%y/%m/%d/')),
                ('img03', models.ImageField(blank=True, upload_to='imagesGame/%y/%m/%d/')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.game')),
            ],
        ),
    ]
