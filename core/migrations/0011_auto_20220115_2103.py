# Generated by Django 3.1.7 on 2022-01-15 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_menu_require_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='require_Login',
            new_name='require_login',
        ),
    ]
