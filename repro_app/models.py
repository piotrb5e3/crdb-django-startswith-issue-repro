from django.db import models
from django.db.models.constraints import UniqueConstraint


class ReproExample(models.Model):
    value = models.TextField(unique=True)
