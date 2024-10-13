from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from utils.validators import validate_sku

class Package(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(_('Description'), blank=True)
    sku = models.CharField(_('stock keeping unit'), max_length=20, validators=[validate_sku], db_index=True)
    avatar =models.ImageField(_('avatar'), blank=True, upload_to='packages/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    price = models.PositiveIntegerField(_('price'))
    duration = models.DurationField(_('duration'), blank=True, null=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    class Meta:
        db_table = 'packages'
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')

    def __str__(self):
        return self.title

class Subscription(models.Model):
    user = models.ForeignKey('users.User', related_name='%(class)s', on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='%(class)s', on_delete=models.CASCADE)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    expires_at = models.DateTimeField(_('expires_at'), blank=True, null=True)

    class Meta:
        db_table = 'subscriptions'
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')




