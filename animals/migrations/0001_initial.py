# Generated by Django 4.1 on 2022-08-09 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Animal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                ("weight", models.FloatField()),
                (
                    "sex",
                    models.CharField(
                        choices=[
                            ("Macho", "Macho"),
                            ("Fêmea", "Femea"),
                            ("Não informado", "Nao Informado"),
                        ],
                        default="Não informado",
                        max_length=15,
                    ),
                ),
            ],
        ),
    ]
