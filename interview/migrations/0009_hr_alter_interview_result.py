# Generated by Django 5.0.6 on 2024-08-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0008_alter_interview_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mob', models.CharField(max_length=16)),
                ('compnay', models.CharField(max_length=100)),
                ('discription', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='interview',
            name='result',
            field=models.CharField(blank=True, choices=[('passed', 'Passed'), ('failed', 'Failed'), ('pending', 'Pending'), ('rescheduled', 'Rescheduled')], max_length=100, null=True),
        ),
    ]
