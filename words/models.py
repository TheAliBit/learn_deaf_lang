from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام")
    image = models.ImageField(upload_to='uploads/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
                              verbose_name="تصویر", blank=True, null=True)  # TODO: upload to
    parent = models.ForeignKey('Category', related_name='children', on_delete=models.CASCADE,
                               verbose_name="دسته بندی پدر", null=True, blank=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


class Word(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام")
    video = models.FileField(upload_to='uploads/', blank=True, null=True,
                             validators=[FileExtensionValidator(['mp4', 'mkv'])],
                             verbose_name="ویدیو")  # TODO: FileExtensionValidator
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")  # TODO: null=True
    image = models.ImageField(upload_to='uploads/', blank=True, null=True,
                              validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
                              verbose_name="تصویر")  # TODO: Upload to
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="دسته بندی",
                                 related_name="words")  # TODO: error
    slug = models.SlugField(unique=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'کلمه'
        verbose_name_plural = 'کلمه ها'
