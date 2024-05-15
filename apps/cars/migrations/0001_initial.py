# Generated by Django 5.0.6 on 2024-05-15 09:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auto_parks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message=['First letter of brand must be only uppercase letters.', 'Not aloud spaces at the beginning or end of the brand.', 'Second letter of brand must be only lowercase letters.', 'Length of brand must be between 3 and 50 characters.'], regex='^(?!.*\\s)[A-Z][a-z]{1,49}(?<!\\s)$')])),
                ('seats', models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(10)])),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2024)])),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000000)])),
                ('body_type', models.CharField(choices=[('SEDAN', 'Sedan'), ('HATCHBACK', 'Hatchback'), ('SUV', 'Suv'), ('COUPE', 'Coupe'), ('CONVERTIBLE', 'Convertible'), ('WAGON', 'Wagon'), ('VAN', 'Van'), ('TRUCK', 'Truck'), ('PICKUP', 'Pickup'), ('ELECTRIC', 'Electric'), ('HYBRID', 'Hybrid')], max_length=50)),
                ('capacity', models.FloatField(validators=[django.core.validators.MinValueValidator(0.4), django.core.validators.MaxValueValidator(5)])),
                ('auto_park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='auto_parks.autoparksmodel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cars',
                'ordering': ('-id',),
            },
        ),
    ]
