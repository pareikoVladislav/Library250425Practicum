from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    first_name = models.CharField(max_length=20, help_text="First name of the author", verbose_name="Имя автора")
    last_name = models.CharField(max_length=50, help_text="Last name of the author", verbose_name="Фамилия автора")
    birthday = models.DateField(verbose_name="Дата рождения")
    profile = models.URLField(blank=True, null=True, verbose_name="Ссылка на соцсеть")
    deleted = models.BooleanField(default=False, help_text="Если галочка включена автор удалён", verbose_name="Профиль удалён")
    rating = models.FloatField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)],
        default=0,
        verbose_name="Рейтинг автора"
    )

    def __str__(self):
        return f"{self.last_name[0]}. {self.first_name}"

"""Обновите уже существующую модель Author дополнительными полями:
Профиль: ссылка на личную страницу автора, может быть не указана
Удалён: поле, которое позволит смотреть удалён ли этот автор из базы всех авторов.
По умолчанию все авторы активны
Рейтинг: позволит отсматривать рейтинг популярности авторов, от 1 до 10"""