# Generated by Django 5.0 on 2024-01-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='password',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='admin',
            name='username',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
