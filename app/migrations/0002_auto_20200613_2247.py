# Generated by Django 3.0.5 on 2020-06-13 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlecomment',
            old_name='username',
            new_name='user',
        ),
    ]