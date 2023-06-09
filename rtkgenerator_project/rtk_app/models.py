from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

        
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class AbonReestr(models.Model):
    dev_name = models.TextField(max_length=200)
    ip_address = models.GenericIPAddressField(protocol='IPv4')
    dev_model = models.TextField(max_length=200)
    vendor = models.TextField(max_length=200)
    role = models.TextField(max_length=200)
    num_of_ports = models.IntegerField()
    geo_address = models.TextField(max_length=200)

    class Meta():
        verbose_name = "Абонентский Реестр"         
        verbose_name_plural = "Абонентский Реестр"
        ordering = ['id',]

    def __str__(self):
        return self.dev_model


class ASOCatalog(models.Model):
    nomenclature_num = models.PositiveBigIntegerField(primary_key=True, unique=True, verbose_name="Номенклатурный номер")
    #nomenclature_num = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, verbose_name="Номенклатурный номер")
    product_name = models.TextField(verbose_name="Наименование товара",)
    unit_of_measure = models.CharField(max_length = 255, verbose_name="Единицы измерения")
    cuantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    unit_price_wo_nds = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена за единицу без НДС, $")
    #price_wo_nds = models.MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    agency_fee = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal(0), validators=PERCENTAGE_VALIDATOR, verbose_name= "Агентское вознаграждение, %") 
    #total_wo_NDS = models.MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    #Цена всего без НДС
    @property
    def price_wo_nds(self):
        return self.cuantity*self.unit_price_wo_nds

    #Итого без НДС
    @property
    def total_wo_nds(self):
        return self.price_wo_nds + (self.price_wo_nds *self.agency_fee * 0.01)


    class Meta():
        verbose_name = "АСО"         
        verbose_name_plural = "АСО"
        ordering = ('product_name',)

    def __str__(self):
        return self.product_name