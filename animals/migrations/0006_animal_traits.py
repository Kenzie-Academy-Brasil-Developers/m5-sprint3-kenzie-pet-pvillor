# Generated by Django 4.1 on 2022-08-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("traits", "0005_remove_trait_animals"),
        ("animals", "0005_remove_animal_traits"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="traits",
            field=models.ManyToManyField(related_name="animals", to="traits.trait"),
        ),
    ]