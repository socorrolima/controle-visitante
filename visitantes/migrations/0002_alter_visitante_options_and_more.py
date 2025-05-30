# Generated by Django 5.2 on 2025-04-08 18:48

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porteiros', '0001_initial'),
        ('visitantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visitante',
            options={'verbose_name': 'Visitante', 'verbose_name_plural': 'Visitantes'},
        ),
        migrations.AddField(
            model_name='visitante',
            name='horario_autorizacao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Horário de autorização de entrada'),
        ),
        migrations.AddField(
            model_name='visitante',
            name='horario_chegada',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Horário de chegada na portaria'),
        ),
        migrations.AddField(
            model_name='visitante',
            name='horario_saida',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Horário de Saída do condomínio'),
        ),
        migrations.AddField(
            model_name='visitante',
            name='morador_responsavel',
            field=models.CharField(blank=True, max_length=194, verbose_name='Nome do morador responsável por autorizar a entrada do visitante'),
        ),
        migrations.AddField(
            model_name='visitante',
            name='registrado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='porteiros.porteiro', verbose_name='Porteiro responsável pelo registro'),
        ),
        migrations.AlterModelTable(
            name='visitante',
            table='visitante',
        ),
    ]
