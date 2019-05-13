import django.db.models.deletio
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BiljnaVrsta',
            fields=[
                ('ID_biljne_vrste', models.AutoField(primary_key=True, serialize=False)),
                ('hrvatski_naziv_vrste', models.CharField(max_length=100)),
                ('latinski_naziv', models.CharField(max_length=100)),
                ('sinonim_vrste', models.CharField(max_length=100)),
                ('opis_vrste', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Biljna vrsta',
                'verbose_name_plural': 'Biljne vrste',
            },
        ),
        migrations.CreateModel(
            name='Podvrsta',
            fields=[
                ('ID_podvrste', models.AutoField(primary_key=True, serialize=False)),
                ('naziv_podvrste', models.CharField(max_length=100)),
                ('ID_bilje_vrste',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biljnevrsteapp.BiljnaVrsta')),
            ],
            options={
                'verbose_name': 'Podvrsta',
                'verbose_name_plural': 'Podvrste',
            },
        ),
        migrations.CreateModel(
            name='Rod',
            fields=[
                ('ID_roda', models.AutoField(primary_key=True, serialize=False)),
                ('naziv_roda', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Rod',
                'verbose_name_plural': 'Rodovi',
            },
        ),
        migrations.CreateModel(
            name='Sistematicar',
            fields=[
                ('ID_sistematicara', models.AutoField(primary_key=True, serialize=False)),
                ('naziv_sistematicara', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Sistematicar',
                'verbose_name_plural': 'Sistematicari',
            },
        ),
        migrations.CreateModel(
            name='Varijet',
            fields=[
                ('ID_varijeta', models.AutoField(primary_key=True, serialize=False)),
                ('naziv_varijeta', models.CharField(max_length=100)),
                ('ID_podvrste',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biljnevrsteapp.Podvrsta')),
            ],
            options={
                'verbose_name': 'Varijet',
                'verbose_name_plural': 'Varijeti',
            },
        ),
        migrations.CreateModel(
            name='UporabniDio',
            fields=[
                ('ID_Uporabni_Dio', models.AutoField(primary_key=True, serialize=False)),
                ('naziv', models.CharField(max_length=100)),
                ('biljna_vrsta', models.ManyToManyField(to='biljnevrsteapp.BiljnaVrsta')),
            ],
            options={
                'verbose_name': 'Uporabni dio',
                'verbose_name_plural': 'Uporabni dijelovi',
            },
        ),
        migrations.CreateModel(
            name='Slika',
            fields=[
                ('ID_Slike', models.AutoField(primary_key=True, serialize=False)),
                ('naziv_slike', models.CharField(max_length=50)),
                ('opis_slike', models.CharField(max_length=255)),
                ('ID_uporabni_dio',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biljnevrsteapp.UporabniDio')),
            ],
            options={
                'verbose_name': 'Slika',
                'verbose_name_plural': 'Slike',
            },
        ),
        migrations.CreateModel(
            name='Porodica',
            fields=[
                ('ID_porodice', models.AutoField(primary_key=True, serialize=False)),
                ('hrvatski_naziv_porodice', models.CharField(max_length=100)),
                ('latisnki_naziv_porodice', models.CharField(max_length=100)),
                ('ID_roda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biljnevrsteapp.Rod')),
            ],
            options={
                'verbose_name': 'Porodica',
                'verbose_name_plural': 'Porodice',
            },
        ),
        migrations.AddField(
            model_name='biljnavrsta',
            name='ID_roda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biljnevrsteapp.Rod'),
        ),
        migrations.AddField(
            model_name='biljnavrsta',
            name='ID_sistematicara',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biljnevrsteapp.Sistematicar'),
        ),
    ]
