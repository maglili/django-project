# Generated by Django 2.2.16 on 2020-09-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Full_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=128)),
                ('feture_name', models.CharField(max_length=128)),
            ],
        ),
    ]
