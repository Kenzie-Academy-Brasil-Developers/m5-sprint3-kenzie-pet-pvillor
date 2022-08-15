from rest_framework.exceptions import ValidationErrorPatch
from rest_framework import serializers
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer
from traits.models import Trait
from groups.models import Group
from rest_framework import status
import math
from .models import Animal, SexAnimal

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    age_in_human_years = serializers.IntegerField(read_only=True)
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexAnimal.choices,
        default=SexAnimal.NAO_INFORMADO
        )
    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    def create(self, validated_data):
        traits_list = validated_data.pop("traits")
        group = validated_data.pop("group")

        animal = Animal.objects.create(**validated_data)

        group_obj, _ = Group.objects.get_or_create(**group)
        animal.group = group_obj

        for trait_dict in traits_list:
            trait_obj, _ = Trait.objects.get_or_create(**trait_dict)
            animal.traits.add(trait_obj)

        animal.age_in_human_years = 16 * math.log(animal.age) + 31
        animal.save()

        return animal

    def update(self, instance: Animal, validated_data: dict) -> Animal:
        no_change = ('traits', 'group', 'sex')
        errors = {}

        for key, value in validated_data.items():
            if key in no_change:
                errors.update({f"{key}": f"You can not update {key} property."})
                continue

            setattr(instance, key, value)

        if errors:
            raise ValidationErrorPatch(errors)

        instance.age_in_human_years = 16 * math.log(instance.age) + 31

        instance.save()

        return instance