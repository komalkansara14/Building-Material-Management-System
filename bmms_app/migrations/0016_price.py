# Generated by Django 3.2 on 2021-04-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmms_app', '0015_auto_20210420_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cprice', models.IntegerField()),
                ('bprice', models.IntegerField()),
                ('sprice', models.IntegerField()),
            ],
        ),
    ]
