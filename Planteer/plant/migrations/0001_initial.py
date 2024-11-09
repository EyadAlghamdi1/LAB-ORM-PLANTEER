# Generated by Django 5.1.2 on 2024-11-07 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('about', models.TextField()),
                ('used_for', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('Fruits', 'Fruits'), ('Vegetables', 'Vegetables'), ('Flowers', 'Flowers'), ('Med', 'Medicinal Planet')], max_length=256)),
                ('is_edible', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
