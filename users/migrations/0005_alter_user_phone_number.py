# Generated by Django 4.2 on 2024-10-08 07:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_user_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                blank=True,
                error_messages={
                    "unique": "A user with that phone number already exists."
                },
                max_length=15,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^\\+?1?\\d{9,15}$",
                        "Phone number must be entered in the format: +999999. Up to 15 digits allowed.",
                    )
                ],
                verbose_name="phone number",
            ),
        ),
    ]
