# Generated by Django 4.1.3 on 2022-11-08 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='symbol',
            field=models.CharField(max_length=20),
        ),
    ]
