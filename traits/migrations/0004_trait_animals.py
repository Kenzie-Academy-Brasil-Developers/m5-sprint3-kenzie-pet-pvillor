# Generated by Django 4.1 on 2022-08-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0005_remove_animal_traits"),
        ("traits", "0003_remove_trait_animals"),
    ]

    operations = [
        migrations.AddField(
            model_name="trait",
            name="animals",
            field=models.ManyToManyField(related_name="traits", to="animals.animal"),
        ),
    ]
