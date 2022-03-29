from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Measurement


class MeasurementCreateUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.measurementTypesVisibility = kwargs.pop(
            "measurement_types_visibility", None
        )
        super().__init__(*args, **kwargs)

        fields = self.fields.copy()

        for field in fields:
            if not getattr(self.measurementTypesVisibility, field, False):
                self.fields.pop(field)

    class Meta:
        model = Measurement
        fields = [
            "pub_date",
            "neck",
            "shoulders",
            "chest",
            "bust",
            "under_bust",
            "bicep_r",
            "bicep_l",
            "forearm_r",
            "forearm_l",
            "waist",
            "abdomen",
            "hips",
            "buttocks",
            "thigh_r",
            "thigh_l",
            "calf_r",
            "calf_l",
            "weight",
        ]
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
