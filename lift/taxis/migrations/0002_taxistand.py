# Generated by Django 3.1.7 on 2021-05-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taxistand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('location', models.CharField(max_length=64)),
            ],
        ),
    ]
