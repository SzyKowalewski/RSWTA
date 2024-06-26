# Generated by Django 5.0.4 on 2024-04-16 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produkcje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tytul', models.CharField(max_length=50)),
                ('Rezyser', models.CharField(max_length=50)),
                ('Dlugosc_ilosc_odcinkow', models.IntegerField()),
                ('Opis', models.CharField(max_length=1000)),
                ('Data_premiery', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Uzytkownicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nazwa_Uzytkownika', models.TextField()),
                ('Haslo', models.TextField()),
                ('E_mail', models.TextField()),
                ('Publiczne', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Rezencje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ocena', models.IntegerField()),
                ('Komentarz', models.TextField()),
                ('ID_Produkcji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.produkcje')),
                ('ID_Uzytkownika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.uzytkownicy')),
            ],
        ),
        migrations.CreateModel(
            name='Obejrzane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Produkcji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.produkcje')),
                ('ID_Uzytkownika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.uzytkownicy')),
            ],
        ),
        migrations.CreateModel(
            name='Do_obejrzenia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Produkcji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.produkcje')),
                ('ID_Uzytkownika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.uzytkownicy')),
            ],
        ),
    ]
