# Generated by Django 4.1.3 on 2022-11-28 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'items_category_one',
            },
        ),
        migrations.CreateModel(
            name='CategoryThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'items_category_three',
            },
        ),
        migrations.CreateModel(
            name='CategoryTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.categoryone')),
            ],
            options={
                'db_table': 'items_category_two',
            },
        ),
        migrations.CreateModel(
            name='UnitOfMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'items_unit_of_measurement',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('price_sp', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('quantity', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('property_fields', models.CharField(blank=True, max_length=510)),
                ('joint_purchase', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/items/')),
                ('is_on_the_main_page', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=15300)),
                ('category_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.categoryone')),
                ('category_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.categorytwo')),
                ('category_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.categorythree')),
                ('unit_of_measurement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.unitofmeasurement')),
            ],
        ),
        migrations.AddField(
            model_name='categorythree',
            name='parent_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.categorytwo'),
        ),
    ]