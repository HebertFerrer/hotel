from django.db import models
from django.core.validators import MinValueValidator


from utils.models import ProjectModel


class Room(ProjectModel):
    limit = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text='Persons limit',
    )
    number = models.CharField(
        unique=True,
        max_length=4,
        help_text='Follows the format "0001", "0002", etc...'
    )
    m2 = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Per day',
    )

    def __str__(self):
        return "{} - {} - {}".format(self.number, self.m2, self.limit)
