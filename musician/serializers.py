from rest_framework import serializers
from .models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.BooleanField(read_only=True)

    class Meta:
        model = Musician
        fields = [
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult",
        ]
        read_only_fields = ["date_of_applying"]

    def validate_age(self, value):
        if value < 14:
            raise serializers.ValidationError(
                "We do not accept people who are under 14."
            )
        return value
