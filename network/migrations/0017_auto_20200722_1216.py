# Generated by Django 3.0.8 on 2020-07-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_auto_20200722_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.CharField(default=0, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.CharField(default=0, max_length=40, null=True),
        ),
    ]
