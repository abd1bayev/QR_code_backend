# Generated by Django 4.0.5 on 2022-07-03 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcodes', '0007_remove_qrcode_file_name_qrcode_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='file',
            field=models.ImageField(upload_to='media/qrcodes/'),
        ),
    ]
