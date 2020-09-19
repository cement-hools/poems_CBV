from django.db import models
from django.urls import reverse


class Poet(models.Model):
    first_name = models.CharField('Имя', max_length=150)
    last_name = models.CharField('Фамилия', max_length=150,
                                 blank=True, null=True)
    bio = models.TextField('Биография', null=True, blank=True)
    photo_url = models.URLField('Ссылка на фото', null=True, blank=True)

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Поэт'
        verbose_name_plural = 'Поэты'

    def __str__(self):
        return f"Поэт: {self.full_name}"

    @property
    def full_name(self):
        return (f"{self.first_name} {self.last_name}"
                if self.last_name is not None
                else f"{self.first_name}")

    def get_absolute_url(self):
        return reverse('poet', args=(self.pk,))


class Poem(models.Model):
    author = models.ForeignKey('Poet', on_delete=models.CASCADE,
                               verbose_name='Автор')
    title = models.CharField('Название', max_length=250)
    text = models.TextField('Текст')
    year = models.CharField('Год(ы)', max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Стихотворение'
        verbose_name_plural = 'Стихотворения'

    def __str__(self):
        return f"Стихотворение: {self.title}"

    def get_absolute_url(self):
        return reverse('poem', args=(self.pk,))
