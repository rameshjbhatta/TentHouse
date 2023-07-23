# Generated by Django 4.2 on 2023-07-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('feedback', models.CharField(max_length=400)),
            ],
        ),
    ]
