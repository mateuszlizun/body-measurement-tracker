# Generated by Django 4.0.2 on 2022-03-27 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0004_alter_measurement_abdomen_alter_measurement_bicep_l_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMeasurementTypesVisibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neck', models.BooleanField(default=False, verbose_name='Neck')),
                ('shoulders', models.BooleanField(default=False, verbose_name='Shoulders')),
                ('chest', models.BooleanField(default=True, verbose_name='Chest')),
                ('bust', models.BooleanField(default=False, verbose_name='Bust')),
                ('under_bust', models.BooleanField(default=False, verbose_name='Under bust')),
                ('bicep_r', models.BooleanField(default=False, verbose_name='Bicep (R)')),
                ('bicep_l', models.BooleanField(default=False, verbose_name='Bicep (L)')),
                ('forearm_r', models.BooleanField(default=False, verbose_name='Forearm (R)')),
                ('forearm_l', models.BooleanField(default=False, verbose_name='Forearm (L)')),
                ('waist', models.BooleanField(default=True, verbose_name='Waist')),
                ('abdomen', models.BooleanField(default=False, verbose_name='Abdomen')),
                ('hips', models.BooleanField(default=True, verbose_name='Hips')),
                ('buttocks', models.BooleanField(default=False, verbose_name='Buttocks')),
                ('thigh_r', models.BooleanField(default=False, verbose_name='Thigh (R)')),
                ('thigh_l', models.BooleanField(default=False, verbose_name='Thigh (L)')),
                ('calf_r', models.BooleanField(default=False, verbose_name='Calf (R)')),
                ('calf_l', models.BooleanField(default=False, verbose_name='Calf (L)')),
                ('weight', models.BooleanField(default=True, verbose_name='Weight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
