from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.validators import validate_phone_number

class Gateway(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='gateways/', blank=True)
    is_enable = models.BooleanField(_('is enable'), default=True)
    credentials  = models.TextField(_('credentials'), blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        verbose_name = _('Gateway')
        verbose_name_plural = _('Gateways')
        db_table = 'gateways'

class Payment(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED = 30
    STATUS_REFUNDED = 31
    STATUS_CHOICES = (
        (STATUS_VOID, _('Void')),
        (STATUS_PAID, _('Paid')),
        (STATUS_ERROR, _('Error')),
        (STATUS_CANCELED, _('Cancelled')),
        (STATUS_REFUNDED, _('Refunded')),
    )

    STATUS_TRANSLATION = {
        STATUS_VOID: _('Payment could not be processed'),
        STATUS_PAID: _('Payment was successfully processed'),
        STATUS_ERROR: _('Payment has encountered an error. our technical team will check issue'),
        STATUS_CANCELED: _('Payment has been cancelled by the user'),
        STATUS_REFUNDED: _('Payment has been refunded'),
    }

    user = models.ForeignKey('users.User', verbose_name=_('user'), related_name='%(class)s', on_delete=models.CASCADE)
    package = models.ForeignKey('subscriptions.Package', verbose_name=_('package'), related_name='%(class)s', on_delete=models.CASCADE)
    gateway = models.ForeignKey(Gateway, verbose_name=_('gateway'), related_name='%(class)s', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(_('price'), default=0)
    status = models.SmallIntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_VOID)
    token = models.CharField(STATUS_CHOICES, max_length=20, blank=True)
    device_uuid = models.CharField(_('device uuid'), max_length=40, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=20, blank=True, validators=[validate_phone_number])
    consumed_code = models.PositiveIntegerField(_('consumed code'), null=True, db_index=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True, db_index=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)


