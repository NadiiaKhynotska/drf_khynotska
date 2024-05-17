# Generated by Django 5.0.6 on 2024-05-17 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profilemodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelManagers(
            name='usermodel',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(default='', upload_to='avatar'),
            preserve_default=False,
        ),
    ]
