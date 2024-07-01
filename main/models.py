from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from words.models import Word


class Profile(AbstractUser):  # do we need to create the user variables when we are using base user?
    username = models.CharField(max_length=15, unique=True, verbose_name="نام کاربری")  # TODO: unique=true
    password = models.CharField(max_length=128, verbose_name="رمز عبور")
    first_name = models.CharField(max_length=255, verbose_name="نام")
    last_name = models.CharField(max_length=255, verbose_name="نام خانوادگی")
    age = models.PositiveIntegerField(verbose_name="سن", null=True, blank=True)
    email = models.EmailField(verbose_name="ایمیل")
    image = models.ImageField(upload_to='uploads/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
                              verbose_name="تصویر")  # TODO: upload to
    liked_words = models.ManyToManyField(Word, related_name='liked_by', verbose_name="کلمه های مورد علاقه")

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'
