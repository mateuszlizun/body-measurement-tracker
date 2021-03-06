# Generated by Django 4.0.2 on 2022-03-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0003_measurement_abdomen_measurement_bicep_l_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="abdomen",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Abdomen",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="bicep_l",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Bicep (L)",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="bicep_r",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Bicep (R)",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="bust",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Bust",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="buttocks",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Buttocks",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="calf_l",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Calf (L)",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="calf_r",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Calf (R)",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="chest",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Chest",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="forearm_l",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Forearm (L)",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="forearm_r",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Forearm (R)",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="hips",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Hips",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="neck",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Neck",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="shoulders",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Shoulders",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="thigh_l",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Thigh (L)",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="thigh_r",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Thigh (R)",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="under_bust",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Under bust",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="waist",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Waist",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="weight",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Weight",
            ),
        ),
    ]
