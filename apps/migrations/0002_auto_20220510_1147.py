# Generated by Django 3.1.4 on 2022-05-10 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applists',
            name='createddata',
        ),
        migrations.RemoveField(
            model_name='applists',
            name='lastdate',
        ),
        migrations.AddField(
            model_name='applists',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='applists',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
