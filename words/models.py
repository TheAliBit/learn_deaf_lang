from django.core.validators import FileExtensionValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام")
    image = models.ImageField(upload_to='uploads/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
                              verbose_name="تصویر", blank=True, null=True)  # TODO: upload to
    parent = models.ForeignKey('Category', related_name='children', on_delete=models.CASCADE,
                               verbose_name="دسته بندی پدر", null=True, blank=True)
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural= 'دسته بندی ها'

    def __str__(self):
        return self.name


class Word(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام")
    video = models.FileField(upload_to='uploads/', validators=[FileExtensionValidator(['mp4', 'mkv'])],
                             verbose_name="ویدیو")  # TODO: FileExtensionValidator
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")  # TODO: null=True
    image = models.ImageField(upload_to='uploads/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
                              verbose_name="تصویر")  # TODO: Upload to
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="دسته بندی",
                                 related_name="words")  # TODO: error

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'کلمه'
        verbose_name_plural = 'کلمه ها'
