# Generated by Django 2.2.4 on 2019-11-03 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_asignation_project_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignation',
            name='project_fk',
        ),
        migrations.AddField(
            model_name='asignation',
            name='project_fk_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='asignations', to='api.Project'),
            preserve_default=False,
        ),
    ]