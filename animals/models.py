from django.db import models

class SexAnimal(models.TextChoices):
    MACHO = "Macho"
    FEMEA = "Fêmea"
    NAO_INFORMADO = "Não informado"

class Animal(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=15,
        choices=SexAnimal.choices,
        default=SexAnimal.NAO_INFORMADO
        )
    group = models.ForeignKey("groups.Group", on_delete=models.CASCADE, related_name="animals", null=True)
    traits = models.ManyToManyField('traits.Trait', related_name='animals')

    def __repr__(self) -> str:
        return f'Animal {self.id} - {self.name}'