# Generated by Django 5.1.2 on 2024-10-26 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLiftLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lifted_at', models.DateTimeField(auto_now_add=True)),
                ('lift_until', models.DateTimeField()),
                ('lift_days_of_week', models.CharField(max_length=50)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
