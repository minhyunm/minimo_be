# Generated by Django 3.2.6 on 2021-11-05 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_alert_unread'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='unread',
        ),
        migrations.AddField(
            model_name='alert',
            name='read',
            field=models.IntegerField(default=0, verbose_name='Read'),
        ),
    ]