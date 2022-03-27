from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    neck = models.DecimalField(
        verbose_name="Neck", max_digits=5, decimal_places=2, null=True, blank=True
    )
    shoulders = models.DecimalField(
        verbose_name="Shoulders", max_digits=5, decimal_places=2, null=True, blank=True
    )
    chest = models.DecimalField(
        verbose_name="Chest", max_digits=5, decimal_places=2, null=True, blank=True
    )
    bust = models.DecimalField(
        verbose_name="Bust", max_digits=5, decimal_places=2, null=True, blank=True
    )
    under_bust = models.DecimalField(
        verbose_name="Under bust", max_digits=5, decimal_places=2, null=True, blank=True
    )
    bicep_r = models.DecimalField(
        verbose_name="Bicep (R)", max_digits=5, decimal_places=2, null=True, blank=True
    )
    bicep_l = models.DecimalField(
        verbose_name="Bicep (L)", max_digits=5, decimal_places=2, null=True, blank=True
    )
    forearm_r = models.DecimalField(
        verbose_name="Forearm (R)",
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )
    forearm_l = models.DecimalField(
        verbose_name="Forearm (L)",
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )
    waist = models.DecimalField(
        verbose_name="Waist", max_digits=5, decimal_places=2, null=True, blank=True
    )
    abdomen = models.DecimalField(
        verbose_name="Abdomen", max_digits=5, decimal_places=2, null=True, blank=True
    )
    hips = models.DecimalField(
        verbose_name="Hips", max_digits=5, decimal_places=2, null=True, blank=True
    )
    buttocks = models.DecimalField(
        verbose_name="Buttocks", max_digits=5, decimal_places=2, null=True, blank=True
    )
    thigh_r = models.DecimalField(
        verbose_name="Thigh (R)", max_digits=5, decimal_places=2, null=True, blank=True
    )
    thigh_l = models.DecimalField(
        verbose_name="Thigh (L)", max_digits=5, decimal_places=2, null=True, blank=True
    )
    calf_r = models.DecimalField(
        verbose_name="Calf (R)", max_digits=5, decimal_places=2, null=True, blank=True
    )
    calf_l = models.DecimalField(
        verbose_name="Calf (L)", max_digits=5, decimal_places=2, null=True, blank=True
    )
    weight = models.DecimalField(
        verbose_name="Weight", max_digits=5, decimal_places=2, null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse("tracker:measurement-detail", kwargs={"pk": self.pk})
