# Generated by Django 2.2.4 on 2019-08-14 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes_pk', models.IntegerField()),
                ('classes_int', models.IntegerField()),
                ('Group_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Group')),
                ('Teacher_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Teacher')),
                ('project_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project')),
            ],
        ),
    ]
