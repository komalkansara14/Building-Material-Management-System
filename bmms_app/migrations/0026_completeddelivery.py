# Generated by Django 3.2 on 2021-05-12 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmms_app', '0025_paidorder_pay_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Delivery Completed', max_length=20)),
                ('delivered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmms_app.paidorder')),
            ],
        ),
    ]