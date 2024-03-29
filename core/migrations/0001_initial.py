# Generated by Django 2.2.4 on 2019-09-09 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_number', models.TextField(blank=True, verbose_name='Номер деталі')),
                ('price', models.FloatField(blank=True, verbose_name='Ціна')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('description_number', models.TextField(blank=True, verbose_name='Конструкційний номер')),
                ('amount_available', models.IntegerField(blank=True, default=False, verbose_name='У наявності')),
                ('image', models.URLField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Anthers',
            fields=[
                ('generalinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.GeneralInfo')),
                ('diameter1', models.FloatField(blank=True, verbose_name='Діаметр 1')),
                ('diameter2', models.FloatField(blank=True, verbose_name='Діаметр 2')),
                ('length', models.FloatField(blank=True, verbose_name='Довжина')),
            ],
            options={
                'verbose_name': 'Пильник кулака',
                'verbose_name_plural': 'Пильники кулака',
            },
            bases=('core.generalinfo',),
        ),
        migrations.CreateModel(
            name='Bearing',
            fields=[
                ('generalinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.GeneralInfo')),
                ('diameter1', models.FloatField(blank=True, verbose_name='Діаметр 1')),
                ('diameter2', models.FloatField(blank=True, verbose_name='Діаметр 2')),
                ('height', models.FloatField(blank=True, verbose_name='Висота')),
            ],
            options={
                'verbose_name': 'Підшипник',
                'verbose_name_plural': 'Підшипники',
            },
            bases=('core.generalinfo',),
        ),
        migrations.CreateModel(
            name='BrakePads',
            fields=[
                ('generalinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.GeneralInfo')),
                ('mounting_data', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Гальмівні колодки',
                'verbose_name_plural': 'Гальмівні колодки',
            },
            bases=('core.generalinfo',),
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('generalinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.GeneralInfo')),
                ('mounting_data', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Фільтр',
                'verbose_name_plural': 'Фільтри',
            },
            bases=('core.generalinfo',),
        ),
        migrations.CreateModel(
            name='SteelWheel',
            fields=[
                ('generalinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.GeneralInfo')),
                ('diameter1', models.FloatField(blank=True, verbose_name='Діаметр 1')),
                ('diameter2', models.FloatField(blank=True, verbose_name='Діаметр 2')),
                ('length', models.FloatField(blank=True, verbose_name='Довжина')),
            ],
            options={
                'verbose_name': 'Пильник кермової тяги',
                'verbose_name_plural': 'Пильники кермової тяги',
            },
            bases=('core.generalinfo',),
        ),
        migrations.CreateModel(
            name='Thrust',
            fields=[
                ('generalinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.GeneralInfo')),
                ('diameter1', models.FloatField(blank=True, verbose_name='Діаметр 1')),
                ('step1', models.FloatField(blank=True, verbose_name='Крок 1')),
                ('diameter2', models.FloatField(blank=True, verbose_name='Діаметр 2')),
                ('step2', models.FloatField(blank=True, verbose_name='Крок 2')),
                ('length', models.FloatField(blank=True, verbose_name='Довжина')),
            ],
            options={
                'verbose_name': 'Кермова тяга',
                'verbose_name_plural': 'Кермові тяги',
            },
            bases=('core.generalinfo',),
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('generalinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.GeneralInfo')),
                ('diameter1', models.FloatField(blank=True, verbose_name='Діаметр 1')),
                ('step1', models.FloatField(blank=True, verbose_name='Крок 1')),
                ('diameter2', models.FloatField(blank=True, verbose_name='Діаметр 2')),
                ('step2', models.FloatField(blank=True, verbose_name='Крок 2')),
                ('length', models.FloatField(blank=True, verbose_name='Довжина')),
                ('cone', models.FloatField(blank=True, verbose_name='Конус')),
                ('mounting_side', models.IntegerField(choices=[(0, 'Права'), (1, 'Ліва')])),
            ],
            options={
                'verbose_name': 'Кермовий наконечник',
                'verbose_name_plural': 'Кермові наконечники',
            },
            bases=('core.generalinfo',),
        ),
    ]
