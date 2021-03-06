import datetime

from django.db import models
from django.utils import timezone

from estagios.core.models import TimeStampedModel, User

CHOICES_SEXO = (
    ('1', 'MASCULINO'),
    ('2', 'FEMININO'),
    ('0', 'OUTROS'),
)

CHOICES_DEFICIENCIA = (
    ('1', 'FÍSICA'),
    ('2', 'AUDITIVA'),
    ('3', 'VISUAL'),
    ('4', 'INTELECTUAL'),
    ('5', 'MÚLTIPLA'),
    ('6', 'READAPTADO'),
    ('0', 'NENHUMA'),
)

CHOICES_ESTADOS_BRASILEIROS = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Acre'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
)
CHOICES_SITUACAO_ACADEMICA = (
    ('0', 'em andamento'),
    ('1', 'concluído'),
    ('2', 'não concluído')
)


class SobreMimModel(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    data_nascimento = models.DateTimeField(
        verbose_name='Data de Nascimento',
        blank=False,
        default=datetime.date(2000, 1, 1)
    )
    sobre_voce = models.TextField(
        verbose_name="Fale mais sobre você",
        default='Sou uma pessoa que...',
        max_length=500,
        blank=False
    )
    objetivos_profissionais = models.TextField(
        verbose_name="Fale sobre seus objetivos profissionais",
        max_length=500,
        default='Meus objetivos profissionais são ...',
        blank=False
    )
    sexo = models.CharField(
        verbose_name="Sexo",
        max_length=10,
        choices=CHOICES_SEXO,
        default='1'
    )
    deficiencia = models.CharField(
        verbose_name="Deficiência",
        max_length=10,
        choices=CHOICES_DEFICIENCIA,
        default='0'
    )

    def save(self, *args, **kwargs):
        self.user.is_student = True
        super(SobreMimModel, self).save(*args, **kwargs)


class ContatoModel(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    endereco = models.CharField(
        verbose_name="Endereço",
        max_length=100,
        blank=False,
        default=""
    )
    endereco_numero = models.CharField(
        verbose_name="Número",
        max_length=5,
        blank=False,
        default=""
    )
    endereco_complemento = models.CharField(
        verbose_name="complemento",
        max_length=30,
        blank=True,
        default=""
    )
    endereco_cidade = models.CharField(
        verbose_name="cidade",
        max_length=30,
        blank=False,
        default=""
    )
    endereco_estado = models.CharField(
        verbose_name="estado",
        max_length=20,
        blank=False,
        choices=CHOICES_ESTADOS_BRASILEIROS,
        default='SP'
    )

    telefone = models.CharField(
        verbose_name="Telefone",
        max_length=16,
        blank=True
    )
    celular = models.CharField(
        verbose_name="Celular",
        max_length=16,
        blank=True
    )
    telefone_recado = models.CharField(
        verbose_name="Telefone para recados",
        max_length=16,
        blank=True
    )

    def save(self, *args, **kwargs):
        self.user.is_student = True
        super(ContatoModel, self).save(*args, **kwargs)


class RedesSociaisModel(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github = models.URLField(verbose_name="GitHub", blank=True, default="")
    linkedin = models.URLField(verbose_name="LinkedIn", blank=True, default="")
    facebook = models.URLField(verbose_name="Facebook", blank=True, default="")
    portfolio = models.URLField(verbose_name="Portfolio", blank=True, default="")

    def save(self, *args, **kwargs):
        self.user.is_student = True
        super(RedesSociaisModel, self).save(*args, **kwargs)


class FaculdadeModel(TimeStampedModel):
    acrescimo = datetime.timedelta(2 * 365)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.CharField(
        verbose_name='Curso', max_length=100,
        blank=False, default=''
    )
    instituicao = models.CharField(
        verbose_name='Curso', max_length=100,
        blank=False, default=''
    )
    carga_horaria = models.IntegerField(
        verbose_name='Carga Horária do curso',
        blank=True, default='2400'
    )
    data_inicio = models.DateTimeField(
        verbose_name='Início do curso',
        blank=False,
        default=datetime.date(2019, 1, 1)
    )
    data_fim = models.DateTimeField(
        verbose_name='Previsão de término',
        blank=True,
        default=timezone.now() + acrescimo
    )
    situacao = models.CharField(
        verbose_name='Situação',
        max_length=10,
        choices=CHOICES_SITUACAO_ACADEMICA,
        default='0'
    )

    def data_com_acrescido(self, **datetime_qualquer):
        if not datetime_qualquer:
            datetime_qualquer = timezone.now()
        return datetime_qualquer + self.acrescimo

    def __str__(self):
        return self.curso

    def save(self, *args, **kwargs):
        self.user.is_student = True
        super(FaculdadeModel, self).save(*args, **kwargs)
