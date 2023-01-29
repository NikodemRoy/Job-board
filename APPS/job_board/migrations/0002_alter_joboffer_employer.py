# Generated by Django 4.1.3 on 2023-01-29 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('job_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EmployerProfile', to='profiles.employerprofile'),
        ),
    ]
