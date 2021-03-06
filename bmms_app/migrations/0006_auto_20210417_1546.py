# Generated by Django 3.2 on 2021-04-17 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmms_app', '0005_auto_20210417_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bricks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_amount', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('qty', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_amount', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('qty', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_amount', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('qty', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='transporterregistration',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='transporterregistration',
            name='phone_no',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='transporterregistration',
            name='vehicle_no',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='phone_no',
            field=models.IntegerField(unique=True),
        ),
        migrations.CreateModel(
            name='GoDownStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bricks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmms_app.bricks')),
                ('cement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmms_app.cement')),
                ('sand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmms_app.sand')),
            ],
        ),
    ]
