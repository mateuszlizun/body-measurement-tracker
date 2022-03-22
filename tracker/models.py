from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    neck = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    shoulders = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    chest = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bust = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    under_bust = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bicep_r = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bicep_l = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    forearm_r = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    forearm_l = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    waist = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    abdomen = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    hips = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    buttocks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    thigh_r = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    thigh_l = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    calf_r = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    calf_l = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def get_absolute_url(self):
        return reverse("tracker:measurement-detail", kwargs={"pk": self.pk})
