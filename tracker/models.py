from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    chest = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    waist = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    hips = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
