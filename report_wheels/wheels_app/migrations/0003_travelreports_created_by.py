# Generated by Django 4.2.1 on 2023-06-02 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wheels_app', '0002_travelreports_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelreports',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='travel_reports_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
