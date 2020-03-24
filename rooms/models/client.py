from utils.models import ProjectModel

from django.db import models


class Client(ProjectModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    document = models.CharField(max_length=200)

    def __str__(self):
        return '{} {} - {}'.format(
            self.first_name,
            self.last_name,
            self.document,
        )
