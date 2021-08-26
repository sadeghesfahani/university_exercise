# Generated by Django 3.2.6 on 2021-08-24 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.PositiveSmallIntegerField()),
                ('capacity', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('staff_id', models.PositiveSmallIntegerField(unique=True)),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'teacher'), (2, 'employee'), (3, 'security')])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('student_id', models.PositiveSmallIntegerField(unique=True)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='faculty.faculty')),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='staff',
            field=models.ManyToManyField(to='faculty.Staff'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('capacity', models.PositiveSmallIntegerField()),
                ('classes', models.ManyToManyField(to='faculty.ClassRoom')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='faculty.faculty'),
        ),
    ]
