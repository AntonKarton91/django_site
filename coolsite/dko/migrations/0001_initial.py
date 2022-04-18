# Generated by Django 4.0.4 on 2022-04-18 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articul', models.CharField(max_length=20, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('photo', models.ImageField(null=True, upload_to='photo/%Y/%m/%d/')),
                ('size_length', models.IntegerField(max_length=5)),
                ('size_width', models.IntegerField(max_length=5)),
                ('size_height', models.IntegerField(max_length=5)),
                ('directory', models.CharField(max_length=255, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dko.client')),
                ('package_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dko.package')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dko.equipment_type')),
            ],
        ),
    ]