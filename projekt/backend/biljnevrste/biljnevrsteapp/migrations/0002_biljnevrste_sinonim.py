# Generated by Django 2.2 on 2019-04-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biljnevrsteapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biljnevrste',
            name='sinonim',
            field=models.CharField(default='nesto', max_length=100),
            preserve_default=False,
        ),
    ]
