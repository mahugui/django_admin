# -*- encoding: utf-8 -*-

from django.db import models


class AbstractBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    updated_at = models.DateTimeField(auto_now=True, help_text='更新时间')

    class Meta:
        abstract = True
