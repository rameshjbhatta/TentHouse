# Generated by Django 4.2 on 2023-07-22 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prasad', '0006_alter_contactinfo_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='address',
        ),
    ]
