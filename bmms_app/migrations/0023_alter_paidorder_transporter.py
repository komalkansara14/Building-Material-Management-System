# Generated by Django 3.2 on 2021-04-28 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmms_app', '0022_paidorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paidorder',
            name='transporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bmms_app.transporterregistration'),
        ),
    ]
