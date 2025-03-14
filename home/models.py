# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Structure(models.Model):

    #__Structure_FIELDS__
    step name = models.CharField(max_length=255, null=True, blank=True)
    clause = models.TextField(max_length=255, null=True, blank=True)
    control = models.TextField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)

    #__Structure_FIELDS__END

    class Meta:
        verbose_name        = _("Structure")
        verbose_name_plural = _("Structure")


class Audit View(models.Model):

    #__Audit View_FIELDS__
    clause = models.TextField(max_length=255, null=True, blank=True)
    sub-clause = models.TextField(max_length=255, null=True, blank=True)
    applicability = models.BooleanField()

    #__Audit View_FIELDS__END

    class Meta:
        verbose_name        = _("Audit View")
        verbose_name_plural = _("Audit View")



#__MODELS__END
