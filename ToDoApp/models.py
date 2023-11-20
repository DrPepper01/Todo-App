from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.class Category(models.Model):


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class ToDo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    expiration_date = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("todo_detail", kwargs={"pk": self.pk})
