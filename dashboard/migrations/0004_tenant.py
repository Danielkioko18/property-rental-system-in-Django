# Generated by Django 4.2.16 on 2024-11-12 09:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_housing_photo_1_housingimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('house_no', models.CharField(max_length=20)),
                ('monthly_rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('water_bill', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('housing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenants', to='dashboard.housing')),
            ],
        ),
    ]
