from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self):
        """Returns True if musician is 21 years or older"""
        return self.age >= 21

    def clean(self):
        """Validate that age is not under 14"""
        if self.age < 14:
            raise ValidationError(
                {"age": "We do not accept people who are under 14."}
            )

    def save(self, *args, **kwargs):
        """Override save to run validation"""
        self.clean()
        super().save(*args, **kwargs)
