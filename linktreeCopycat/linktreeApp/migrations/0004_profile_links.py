# Generated by Django 4.0.6 on 2022-07-21 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linktreeApp', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='links',
            field=models.CharField(default='https://www.google.com/', max_length=500),
        ),
    ]
