# Generated by Django 4.0.6 on 2022-07-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('immagine', models.ImageField(upload_to='')),
                ('prezzo', models.FloatField()),
            ],
        ),
    ]