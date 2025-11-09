from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    first_name = models.CharField(max_length=20, help_text="First name of the author", verbose_name="Имя автора")
    last_name = models.CharField(max_length=50, help_text="Last name of the author", verbose_name="Фамилия автора")
    birthday = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return f"{self.title} --{self.author.last_name if self.author else 'NONAME'}"
