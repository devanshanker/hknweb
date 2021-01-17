# Generated by Django 2.2.8 on 2020-11-13 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_auto_20190421_2337_squashed_0012_auto_20191001_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='department',
            old_name='subject',
            new_name='long_name',
        ),
        migrations.RemoveField(
            model_name='department',
            name='name',
        ),
        migrations.AddField(
            model_name='department',
            name='abbreviated_name',
            field=models.CharField(max_length=8, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='coursesemester',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Semester'),
        ),
    ]
