from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='category/', blank=True)
    is_enabled = models.BooleanField(_('enabled'), default=True)
    created_at = models.DateTimeField(_('created at'),auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.title

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

    def __str__(self):
        return self.title

class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPES = (
        (FILE_AUDIO, _('Audio file')),
        (FILE_VIDEO, _('Video file')),
        (FILE_PDF, _('PDF file')),
    )
    parent = models.ForeignKey('Product', verbose_name=_('product'), related_name='files', on_delete=models.CASCADE)
    title = models.CharField(_('name'), max_length=50)
    file_type = models.PositiveSmallIntegerField(_('file type'), choices=FILE_TYPES, default=FILE_VIDEO)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d')
    is_enabled = models.BooleanField(_('enabled'), default=True)
    created_at = models.DateTimeField(_('created at'),auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        db_table = 'file'
        verbose_name = _('file')
        verbose_name_plural = _('files')

    def __str__(self):
        return self.title







