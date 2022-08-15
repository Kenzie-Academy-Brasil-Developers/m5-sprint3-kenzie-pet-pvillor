from django.test import TestCase
from .models import Trait

class TraitTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.trait_1_data = {
            "name": "peludo"
        }

        cls.trait_1 = Trait.objects.create(**cls.trait_1_data)

    def test_trait_fields(self):
        self.assertEqual(self.trait_1.name, self.trait_1_data["name"])