# Generated by Django 3.2 on 2021-04-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmms_app', '0019_order_material_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
