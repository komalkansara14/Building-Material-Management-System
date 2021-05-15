# Generated by Django 3.2 on 2021-04-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmms_app', '0008_auto_20210417_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
