# Generated by Django 4.1.1 on 2022-09-28 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppCoder", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="estudiante",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
