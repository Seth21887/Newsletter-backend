# Generated by Django 4.1.1 on 2022-09-19 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_alter_campaign_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='logo',
        ),
    ]
