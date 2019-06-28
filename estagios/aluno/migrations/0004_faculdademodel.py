# Generated by Django 2.2.2 on 2019-06-28 19:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aluno', '0003_auto_20190627_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaculdadeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('curso', models.CharField(blank=True, default='', max_length=100, verbose_name='Curso')),
                ('instituicao', models.CharField(blank=True, default='', max_length=100, verbose_name='Curso')),
                ('carga_horaria', models.IntegerField(default='2400', max_length=5, verbose_name='Carga Horária do curso')),
                ('data_inicio', models.DateTimeField(blank=True, default=datetime.date(2019, 1, 1), verbose_name='Início do curso')),
                ('data_fim', models.DateTimeField(default=datetime.date(2019, 1, 1), verbose_name='Previsão de término')),
                ('situacao', models.CharField(choices=[('0', 'em andamento'), ('1', 'concluído'), ('2', 'não concluído')], default='1', max_length=10, verbose_name='Situação')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]