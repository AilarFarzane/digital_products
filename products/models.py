from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='category/')
    is_enabled = models.BooleanField(_('enabled'), default=True)
    created_at = models.DateTimeField(_('created at'),auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name = _('category')
        verbose_name_plural = _('categories')

class Product(models.Model):
    title = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='product/')
    categories = models.ManyToManyField('Category', verbose_name=_('category'), blank=True)
    is_enabled = models.BooleanField(_('enabled'), default=True)
    created_at = models.DateTimeField(_('created at'),auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)


    class Meta:
        db_table = 'product'
        verbose_name = _('product')
        verbose_name_plural = _('products')

class File(models.Model):
    parent = models.ForeignKey('Product', verbose_name=_('product'), on_delete=models.CASCADE)
    title = models.CharField(_('name'), max_length=50)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d')
    is_enabled = models.BooleanField(_('enabled'), default=True)
    created_at = models.DateTimeField(_('created at'),auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        db_table = 'file'
        verbose_name = _('file')
        verbose_name_plural = _('files')







