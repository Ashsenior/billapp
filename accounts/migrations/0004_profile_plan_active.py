# Generated by Django 3.2.6 on 2022-07-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='plan_active',
            field=models.BooleanField(default=False),
        ),
    ]
