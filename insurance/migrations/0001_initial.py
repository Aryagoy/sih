# Generated by Django 3.0.2 on 2020-01-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugar', models.FloatField(max_length=10)),
                ('haemoglobin', models.FloatField(max_length=10)),
                ('cholestrol', models.FloatField(max_length=10)),
            ],
        ),
    ]