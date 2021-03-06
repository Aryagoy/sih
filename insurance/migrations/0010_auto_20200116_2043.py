# Generated by Django 3.0.2 on 2020-01-16 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0009_auto_20200116_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='accident_insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('x_ray', models.CharField(max_length=100)),
                ('ct_scan', models.CharField(max_length=100)),
                ('mri', models.CharField(max_length=100)),
                ('others', models.CharField(max_length=100)),
                ('accident_insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.general_details')),
            ],
        ),
        migrations.CreateModel(
            name='chronic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ckd_test', models.FloatField(max_length=10)),
                ('egfr', models.FloatField(max_length=10)),
                ('creatinine', models.FloatField(max_length=10)),
                ('uric_acid', models.FloatField(max_length=10)),
                ('Urea', models.FloatField(max_length=10)),
                ('ecg', models.FloatField(max_length=10)),
                ('emg_test', models.FloatField(max_length=10)),
                ('chronics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.general_details')),
            ],
        ),
        migrations.CreateModel(
            name='vital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sugar', models.FloatField(max_length=10)),
                ('mcv', models.FloatField(max_length=10)),
                ('haemoglobin', models.FloatField(max_length=10)),
                ('cholestrol', models.FloatField(max_length=10)),
                ('bp', models.FloatField(max_length=10)),
                ('pulse_rate', models.FloatField(max_length=10)),
                ('total_rbc', models.FloatField(max_length=10)),
                ('pcv', models.FloatField(max_length=10)),
                ('platelet_count', models.FloatField(max_length=10)),
                ('leucocytes_count', models.FloatField(max_length=10)),
                ('tsh', models.FloatField(max_length=10)),
                ('glucose_content', models.FloatField(max_length=10)),
                ('bilirubin', models.FloatField(max_length=10)),
                ('ph', models.FloatField(max_length=10)),
                ('wbc_count', models.FloatField(max_length=10)),
                ('vitals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.general_details')),
            ],
        ),
        migrations.DeleteModel(
            name='accident_insurances',
        ),
        migrations.DeleteModel(
            name='chronicss',
        ),
        migrations.DeleteModel(
            name='vitalss',
        ),
    ]
