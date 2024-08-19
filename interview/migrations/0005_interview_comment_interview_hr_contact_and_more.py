# Generated by Django 5.0.6 on 2024-08-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0004_interview_linkdin'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interview',
            name='hr_contact',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='interview',
            name='hr_name',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
