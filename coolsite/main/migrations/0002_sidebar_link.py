# Generated by Django 4.0.3 on 2022-04-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebar',
            name='link',
            field=models.CharField(max_length=30, null=True),
        ),
    ]