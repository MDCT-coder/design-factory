# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from materials.constants import MATERIAL_TYPE_CHOICE, MaterialType
from users.models import User


class Material(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField('标题', max_length=255)
    cover = models.ImageField('封面', upload_to='cover/', null=True, blank=True)
    type = models.IntegerField('类型', choices=MATERIAL_TYPE_CHOICE, default=MaterialType.MATERIAL)
    description = models.TextField()
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.get_type_display(), self.title)

    def __unicode__(self):
        return '{}-{}'.format(self.get_type_display(), self.title)
