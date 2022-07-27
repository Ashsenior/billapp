# Generated by Django 3.2.6 on 2022-07-27 05:04

from django.db import migrations, models
import django.db.models.deletion
import plans.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(default=plans.models.generate_code, editable=False, max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=800)),
                ('duration', models.IntegerField(choices=[(30, '1 Month'), (180, '6 Months'), (364, '1 Year')], default=30)),
                ('default_for_customer', models.BooleanField(default=False)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.applists')),
            ],
        ),
    ]
