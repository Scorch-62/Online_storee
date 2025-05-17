from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name="описание"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=1000, verbose_name="описание")
    image = models.ImageField(
        upload_to="books/photo", blank=True, null=True, verbose_name="изображение"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="категория",
        blank=True,
        null=True,
        related_name="Categories",
    )
    price = models.CharField(max_length=100, verbose_name="цена за покупку")
    created_at = models.DateField(blank=True, null=True, verbose_name="дата создания")
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="дата последнего изменения"
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["category", "price"]

    def __str__(self):
        return self.name
