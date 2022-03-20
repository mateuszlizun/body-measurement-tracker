from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Measurement


class MeasurementCreateForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ["pub_date", "chest", "waist", "hips", "weight"]
        widgets = {
            "pub_date": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }

    def clean_pub_date(self):
        pub_date = self.cleaned_data["pub_date"]

        if pub_date > timezone.now():
            raise ValidationError("Date cannnot be from the future!")

        return pub_date
