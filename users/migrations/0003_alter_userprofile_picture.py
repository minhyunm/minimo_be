# Generated by Django 3.2.6 on 2021-10-23 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Profile Picture'),
        ),
    ]
