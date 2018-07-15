from django.db import models


class Definition(models.Model):
    word = models.CharField(max_length=64)
