# Generated by Django 2.1.7 on 2019-03-14 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(choices=[('!', 'Low'), ('!!', 'Medium'), ('!!!', 'High')], default='!', max_length=3)),
                ('work', models.CharField(blank=True, max_length=100, null=True)),
                ('created_time', models.DateTimeField(default=datetime.datetime.now)),
                ('due_time', models.DateTimeField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]