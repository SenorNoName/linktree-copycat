# Generated by Django 4.0.6 on 2022-08-09 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linktreeApp', '0005_delete_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='links',
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linktreeApp.profile')),
            ],
        ),
    ]