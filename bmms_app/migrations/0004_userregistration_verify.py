# Generated by Django 3.2 on 2021-04-16 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmms_app', '0003_transporterregistration_verify'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='verify',
            field=models.BooleanField(default=False),
        ),
    ]