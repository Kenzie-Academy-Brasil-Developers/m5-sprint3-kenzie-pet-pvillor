from rest_framework import serializers

from .models import SexAnimal

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexAnimal.choices,
        default=SexAnimal.NAO_INFORMADO
        )