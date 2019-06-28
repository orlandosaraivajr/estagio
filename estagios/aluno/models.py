import datetime

from django.db import models

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
