import random
import uuid

from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser, send_mail
from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _
from utils.validators import validate_phone_number, validate_username

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, username, phone_number, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('Users must have username')
        email = self.normalize_email(email)
        user = self.model(username=username, phone_number=phone_number,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          email=email,date_joined = now,
                           **extra_fields)
        if not extra_fields.get('no_password'):
            user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, username=None, phone_number=None, email=None, password=None, **extra_fields):
        if username is None:
            if email:
                username = email.split('@', 1)[0]
            if phone_number:
                username = random.choice('abcdefghijklmnopqrstuvwxyz') + str(phone_number) [-7:]
            while User.objects.filter(username=username).exists():
                username += str(random.randint(10, 99))
        return self._create_user(username, phone_number, email, password, False, False, **extra_fields)

    def create_superuser(self, username, phone_number, email, password, **extra_fields):
        return self._create_user(username, phone_number, email, password, True, True, **extra_fields)

    def get_by_phone_number(self, phone_number):
        return self.get(**{'phone_number': phone_number})



class User(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(_('username'),max_length =30, unique=True,
                              validators = [validate_username])
    first_name=models.CharField(_('first name'), max_length=30, blank=True)
    last_name=models.CharField(_('last name'), max_length=30, blank=True)
    email=models.EmailField(_('email address'), unique=True)
    phone_number=models.CharField(_('phone number'), unique=True, blank=True, null=True, max_length=15,
                                        validators=[validate_phone_number],
                                    )
    is_staff=models.BooleanField(_('staff status'), default=False,
                                 help_text=_('Designates whether the user can log into this admin site.'))
    is_active=models.BooleanField(_('active'), default=True,
                                  help_text=_('Designates whether this user should be treated as active. '))

    date_joined=models.DateTimeField(_('date joined'), default=timezone.now)
    last_seen = models.DateTimeField(_('last seen'), null=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(_('nickname'), max_length=30, blank=True)
    avatar = models.ImageField(_('avatar'), blank=True)
    birthday = models.DateField(_('birthday'), blank=True, null=True)
    gender = models.BooleanField(_('gender'), default=False,null=True, help_text=_('Female is False, Male is True, null is unset'))
    province =models.ForeignKey(verbose_name=_('province'), to='Province', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'user_profile'
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    @property
    def get_first_name(self):
        return self.user.first_name

    @property
    def get_last_name(self):
        return self.user.last_name

    @property
    def get_nickname(self):
        return self.nickname if self.nickname else self.user.username

class Device(models.Model):
    WEB = 1
    IOS = 2
    ANDROID = 3
    DEVICE_TYPES=(
        (WEB, 'Web'),
        (IOS, 'IOS'),
        (ANDROID, 'Android'),
    )
    user = models.ForeignKey(User, related_name='devices', on_delete=models.CASCADE)
    device_uuid = models.UUIDField(_('Device UUID'), null=True)
    last_login = models.DateTimeField(_('last login'), null=True)
    device_type = models.PositiveSmallIntegerField(_('device type'), choices=DEVICE_TYPES, default=WEB)
    device_os = models.CharField(_('device OS'), max_length=30, blank=True)
    device_model = models.CharField(_('device model'), max_length=30, blank=True)
    app_version = models.CharField(_('app version'), max_length=30, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        db_table = 'device'
        verbose_name = _('device')
        verbose_name_plural = _('devices')
        unique_together = ('user', 'device_uuid')


class Province(models.Model):
    name = models.CharField( max_length=30)
    is_valid = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name










