# Generated by Django 3.2 on 2021-04-19 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmms_app', '0011_godownstock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transporterregistration',
            name='cpassword',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='cpassword',
        ),
    ]