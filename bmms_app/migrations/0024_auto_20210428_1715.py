# Generated by Django 3.2 on 2021-04-28 11:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bmms_app', '0023_alter_paidorder_transporter'),
    ]

    operations = [
        migrations.AddField(
            model_name='paidorder',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paidorder',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
