# Generated by Django 3.0.8 on 2020-07-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_auto_20200721_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.DeleteModel(
            name='Follower',
        ),
    ]
