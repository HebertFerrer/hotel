from utils.models import ProjectModel

from django.db import models


class Reservation(ProjectModel):
    client = models.ForeignKey(
        'rooms.Client',
        on_delete=models.CASCADE,
        related_name='reservations',
    )
    room = models.ForeignKey(
        'rooms.Room',
        on_delete=models.CASCADE,
        related_name='reservations',
    )
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return '{} - {}'.format(self.client.first_name, self.room.number)
