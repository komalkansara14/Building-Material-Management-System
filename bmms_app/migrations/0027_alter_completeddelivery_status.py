# Generated by Django 3.2 on 2021-05-12 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmms_app', '0026_completeddelivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completeddelivery',
            name='status',
            field=models.CharField(default='Delivery remaining', max_length=20),
        ),
    ]