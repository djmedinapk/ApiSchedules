# Generated by Django 2.2.4 on 2019-11-03 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_asignation_classroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignation',
            name='project_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Project'),
            preserve_default=False,
        ),
    ]