# Generated by Django 4.1.2 on 2022-11-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0016_dressingroom_actor_dressing'),
    ]

    operations = [
        migrations.AddField(
            model_name='dressingroom',
            name='floor',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dressingroom',
            name='number',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
