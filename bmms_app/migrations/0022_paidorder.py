# Generated by Django 3.2 on 2021-04-28 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmms_app', '0021_delete_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaidOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmms_app.order')),
                ('transporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmms_app.transporterregistration')),
            ],
        ),
    ]
