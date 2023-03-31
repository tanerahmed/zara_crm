from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe


class User(AbstractUser):

    class Meta:
        verbose_name = 'Потребител'
        verbose_name_plural = 'Моите Служители'


class Company(models.Model):
    CATEGORY_CHOICES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Big', 'Big'),
    )

    name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    social_media_profile_url = models.URLField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateField(null=True, blank=True)
    company_info = models.TextField(blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
    work_with_us = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Client(models.Model):
    company = models.ManyToManyField(Company)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    social_media_profile_url = models.URLField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    client_info = models.TextField(blank=True, null=True)
    meeting_information = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенти'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Distributors(models.Model):
    company_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.company_name}"

    class Meta:
        verbose_name = 'Дистрибутор'
        verbose_name_plural = 'Дистрибутори'


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'


class Sold(models.Model):

    company_buyer = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    client_buyer = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    product_url = models.URLField(max_length=250,  blank=True, null=True)
    distributor = models.ForeignKey(Distributors, on_delete=models.SET_NULL, blank=True, null=True)
    items = models.IntegerField(default=1)

    sold_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    buy_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    profit_procent = models.IntegerField(blank=True, null=True)
    product_information = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    sold = models.BooleanField(default=False)

    def profit(self):
        calculate = self.sold_price - self.buy_price
        return calculate

    def __str__(self):
        return f" company:{self.company_buyer}, product: {self.product}, items: {self.items}"

    class Meta:
        verbose_name = 'Продажба'
        verbose_name_plural = 'Продажби'


class Article(models.Model):
    title = models.CharField(max_length=150)
    url_address = models.URLField(max_length=200, blank=True, null=True)
    company = models.ManyToManyField(Company)

    class Meta:
        verbose_name = 'Статия'
        verbose_name_plural = 'Статии'