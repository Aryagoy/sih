# Generated by Django 3.0.2 on 2020-01-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chronic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abc', models.FloatField(max_length=10)),
                ('defg', models.FloatField(max_length=10)),
            ],
        ),
    ]