# Generated by Django 4.0.4 on 2022-05-01 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_usersettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useravatar',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usersettings',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserAvatar',
        ),
        migrations.DeleteModel(
            name='UserSettings',
        ),
    ]
