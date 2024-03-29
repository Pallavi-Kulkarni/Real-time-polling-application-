# Generated by Django 5.0.2 on 2024-03-01 04:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='Poll Question')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200, verbose_name='Choice text')),
                ('votes', models.IntegerField(default=0, verbose_name='Number of votes')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polling.poll', verbose_name='Related poll')),
            ],
        ),
    ]
