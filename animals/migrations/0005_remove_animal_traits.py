# Generated by Django 4.1 on 2022-08-12 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0004_animal_traits"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="animal",
            name="traits",
        ),
    ]
