from __future__ import unicode_literals

from django.db import models

from django_admin.common.dbbase import AbstractBase


class House(AbstractBase):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    source = models.SmallIntegerField()
    picture = models.CharField(max_length=50)

    class Meta:
        db_table = "house"
        ordering = ["-updated_at"]

    def __unicode__(self):
        return "{name}-{source}-{price}".format(name=self.name, source=self.source, price=self.price)
