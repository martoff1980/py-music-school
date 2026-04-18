from django.test import TestCase
from django.db.models import CharField, IntegerField, DateField

from musician.models import Musician


class MusicianModelTest(TestCase):
    def setUp(self) -> None:
        Musician.objects.create(
            first_name="Joseph",
            last_name="Green",
            instrument="the guitar",
            age=16,
        )

    def test_types_of_fields(self):
        char_fields = ["first_name", "last_name", "instrument"]

        for field in char_fields:
            with self.subTest(field):
                print(Musician._meta.get_field(field))
                self.assertEqual(
                    isinstance(Musician._meta.get_field(field), CharField),
                    True,
                )

        self.assertEqual(
            isinstance(Musician._meta.get_field("age"), IntegerField), True
        )
        self.assertEqual(
            isinstance(Musician._meta.get_field("date_of_applying"), DateField),
            True,
        )

    def test_fields_max_length(self):
        char_fields = ["first_name", "last_name", "instrument"]

        for field in char_fields:
            with self.subTest(f"{field} max_length"):
                self.assertEqual(Musician._meta.get_field(field).max_length, 63)

    def test_str_method(self):
        musician = Musician.objects.get(first_name="Joseph")
        self.assertEqual(str(musician), "Joseph Green")

    def test_is_adult_property(self):
        self.assertTrue(hasattr(Musician, "is_adult"))
