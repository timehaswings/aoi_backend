# Generated by Django 3.1.4 on 2021-09-03 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210903_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basevideo',
            old_name='m3u8_url',
            new_name='m3u8_path',
        ),
        migrations.RenameField(
            model_name='basevideo',
            old_name='thumb_url',
            new_name='thumb_path',
        ),
    ]