# Generated by Django 4.1.3 on 2023-09-10 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_employerprofile_id_alter_workerprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employerprofile',
            name='address',
            field=models.CharField(blank=True, db_column='address', max_length=96),
        ),
    ]
