# Generated by Django 4.0.2 on 2022-02-16 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(max_length=100, verbose_name='English Name')),
                ('latin_name', models.CharField(max_length=100, verbose_name='Latin Name')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_specie', models.CharField(max_length=100, verbose_name='Add New Specie')),
                ('type', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='clone1.tree', verbose_name='Species Type')),
            ],
        ),
    ]
