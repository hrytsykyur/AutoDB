from django.db import models
from django.template.defaultfilters import truncatechars
from model_utils.managers import InheritanceManager
# Create your models here.


class GeneralInfo(models.Model):
    objects = InheritanceManager()
    detail_number = models.TextField("Номер деталі",blank=True, null=True)
    price = models.FloatField("Ціна",blank=True, null=True)
    amount_available = models.IntegerField("У наявності",blank=True, null=True, default=0)
    description = models.TextField("Опис",blank=True, null=True)
    description_number = models.TextField("Конструкційний номер",blank=True, null=True)
    image = models.URLField(blank=True)
    @property
    def short_description_number(self):
        return truncatechars(self.description_number, 400)

class Tip(GeneralInfo):
    RIGHT = 0
    LEFT = 1
    SIDE = (
        (RIGHT, 'Права'),
        (LEFT, 'Ліва'),
    )
    diameter1 = models.FloatField("Діаметр 1",blank=True, null=True)
    step1 = models.FloatField("Крок 1",blank=True, null=True)
    diameter2 = models.FloatField("Діаметр 2",blank=True, null=True)
    step2 = models.FloatField("Крок 2",blank=True, null=True)
    length = models.FloatField("Довжина",blank=True, null=True)
    cone = models.FloatField("Конус",blank=True, null=True)
    mounting_side = models.IntegerField(choices=SIDE, default=RIGHT)
    class Meta:
        verbose_name = "Кермовий наконечник"
        verbose_name_plural = "Кермові наконечники"

class Thrust(GeneralInfo):
    diameter1 = models.FloatField("Діаметр 1",blank=True, null=True)
    step1 = models.FloatField("Крок 1",blank=True, null=True)
    diameter2 = models.FloatField("Діаметр 2",blank=True, null=True)
    step2 = models.FloatField("Крок 2",blank=True, null=True)  
    length = models.FloatField("Довжина",blank=True, null=True)
    class Meta:
        verbose_name = "Кермова тяга"
        verbose_name_plural = "Кермові тяги"
class SteelWheel(GeneralInfo):
    diameter1 = models.FloatField("Діаметр 1",blank=True, null=True)
    diameter2 = models.FloatField("Діаметр 2",blank=True, null=True)
    length = models.FloatField("Довжина",blank=True, null=True)  
    class Meta:
        verbose_name = "Пильник кермової тяги"
        verbose_name_plural = "Пильники кермової тяги"
class Anthers(GeneralInfo):
    diameter1 = models.FloatField("Діаметр 1",blank=True, null=True)
    diameter2 = models.FloatField("Діаметр 2",blank=True, null=True) 
    length = models.FloatField("Довжина",blank=True, null=True)
    class Meta:
        verbose_name = "Пильник кулака"
        verbose_name_plural = "Пильники кулака"
class Bearing(GeneralInfo):
    diameter1 = models.FloatField("Діаметр 1",blank=True, null=True)
    diameter2 = models.FloatField("Діаметр 2",blank=True, null=True)      
    height = models.FloatField("Висота",blank=True, null=True)
    class Meta:
        verbose_name = "Підшипник"
        verbose_name_plural = "Підшипники"
class BrakePads(GeneralInfo):
    mounting_data = models.TextField("Монтажні дані",blank=True, null=True)
    class Meta:
        verbose_name = "Гальмівні колодки"
        verbose_name_plural = "Гальмівні колодки"
class Filter(GeneralInfo):
    mounting_data = models.TextField("Монтажні дані",blank=True, null=True)
    class Meta:
        verbose_name = "Фільтр"
        verbose_name_plural = "Фільтри"

class Ordered(models.Model):
    parent = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE)
    amount = models.IntegerField()
    class Meta:
        verbose_name = "Замовлено"