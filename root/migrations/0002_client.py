# Generated by Django 5.1.4 on 2025-01-08 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clients', models.IntegerField(default=1)),
                ('project', models.IntegerField(default=1)),
                ('support', models.IntegerField(default=1)),
                ('workers', models.IntegerField(default=1)),
            ],
        ),
    ]
