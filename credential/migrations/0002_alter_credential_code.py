# Generated by Django 5.1.5 on 2025-02-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credential', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='code',
            field=models.CharField(max_length=50),
        ),
    ]
