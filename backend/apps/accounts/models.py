from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey('core.CustomUser', verbose_name=_('user'), on_delete=models.CASCADE)