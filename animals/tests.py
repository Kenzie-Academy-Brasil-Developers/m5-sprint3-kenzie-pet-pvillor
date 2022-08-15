from django.test import TestCase
from traits.models import Trait
from groups.models import Group
from .models import Animal

class AnimalTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.animal_1_data = {
            "name": "Akamaru",
            "age": 1,
            "weight": 30,
            "sex": "Macho"
        }

        cls.animal_1 = Animal.objects.create(**cls.animal_1_data)

        group_1_data = {
            "name": "cão",
            "scientific_name": "canis familiaris"
        }

        cls.group_1 = Group(**group_1_data)

        trait_1_data = {
            "name": "peludo"
        }

        trait_2_data = {
            "name": "médio porte"
        }

        cls.trait_1 = Trait(**trait_1_data)
        cls.trait_2 = Trait(**trait_2_data)

    def test_animal_fields(self):
        self.assertEqual(self.animal_1.name, self.animal_1_data["name"])
        self.assertEqual(self.animal_1.age, self.animal_1_data["age"])
        self.assertEqual(self.animal_1.weight, self.animal_1_data["weight"])
        self.assertEqual(self.animal_1.sex, self.animal_1_data["sex"])

    def test_group_relation(self):
        self.animal_1.group = self.group_1
        self.group_1.save()

    def test_traits_relation(self):
        self.trait_1.save()
        self.trait_2.save()
        self.animal_1.traits.set([self.trait_1, self.trait_2])