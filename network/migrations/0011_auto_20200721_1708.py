# Generated by Django 3.0.8 on 2020-07-22 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_auto_20200721_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Follower',
        ),
    ]
