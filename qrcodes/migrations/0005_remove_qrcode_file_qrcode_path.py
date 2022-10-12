# Generated by Django 4.0.5 on 2022-07-03 15:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qrcodes', '0004_remove_qrcode_image_qrcode_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcode',
            name='file',
        ),
        migrations.AddField(
            model_name='qrcode',
            name='path',
            field=models.CharField(default=datetime.datetime(2022, 7, 3, 15, 43, 45, 664492, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
