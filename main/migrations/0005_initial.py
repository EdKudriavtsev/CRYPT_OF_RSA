# Generated by Django 4.0.4 on 2022-05-01 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_remove_useravatar_user_remove_usersettings_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyGenHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_key', models.IntegerField()),
                ('public_key', models.IntegerField()),
                ('module_num', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CipherHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_in', models.CharField(max_length=255)),
                ('key', models.IntegerField()),
                ('key2', models.IntegerField()),
                ('result', models.CharField(max_length=511)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
