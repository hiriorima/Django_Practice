# Generated by Django 2.1.2 on 2018-10-25 05:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300000)])),
                ('progress_prepare', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HopeCareer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desire', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('region', models.CharField(max_length=32)),
                ('job_category', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='StudyArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='StudyTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=32)),
                ('body', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='hope_career',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hope_career', to='survey.HopeCareer'),
        ),
        migrations.AddField(
            model_name='entry',
            name='study_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_area', to='survey.StudyArea'),
        ),
        migrations.AddField(
            model_name='entry',
            name='study_theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_theme', to='survey.StudyTheme'),
        ),
    ]
