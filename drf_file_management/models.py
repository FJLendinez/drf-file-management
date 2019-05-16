# -*- coding: utf-8 -*-
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel


class AbstractFile(TimeStampedModel):
    uuid = models.UUIDField(default=uuid4, primary_key=True)
    file = models.FileField()

    def __str__(self):
        return f'{self.uuid} - {self.file.name}'

    class Meta:
        abstract = True


class File(AbstractFile):
    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')
