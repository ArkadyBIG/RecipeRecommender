# Generated by Django 4.2.6 on 2023-11-26 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ingredient", "0001_initial"),
        ("recipe", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="ingredients",
        ),
        migrations.AddField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(to="ingredient.ingredient"),
        ),
    ]