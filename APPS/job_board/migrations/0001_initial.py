# Generated by Django 4.1.3 on 2023-01-29 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=20000)),
                ('city', models.CharField(max_length=300)),
                ('post_code', models.CharField(max_length=300)),
                ('addres', models.CharField(max_length=300)),
                ('job_type', models.CharField(choices=[('Full time', 'Full time'), ('Part time', 'Part time'), ('Internship', 'Internship'), ('Freelance', 'Freelance'), ('Temporary', 'Temporary')], max_length=30)),
                ('experience', models.CharField(max_length=4)),
                ('salary', models.CharField(blank=True, max_length=30)),
                ('monthly_working_hours', models.CharField(max_length=30)),
                ('currency', models.CharField(choices=[('PLN', 'PLN'), ('EUR', 'EUR'), ('USD', 'USD')], max_length=3)),
                ('is_published', models.BooleanField(default=False)),
                ('is_closed', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, related_name='Category', to='job_board.jobcategory')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EmployerProfile', to='profiles.employerprofile')),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]
