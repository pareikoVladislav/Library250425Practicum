from django.db import models
from  django.core.validators import MinValueValidator,MaxValueValidator

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    profile_link = models.URLField(blank=True,null=True)
    deleted = models.BooleanField(default=False)
    rating = models.FloatField(validators=[MinValueValidator(0),
                                           MaxValueValidator(10)], default=0)

    def __str__(self):
        return f"{self.last_name[0]}. {self.first_name}"