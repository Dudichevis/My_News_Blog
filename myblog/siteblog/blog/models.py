from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование категории')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Tag(models.Model):
    title = models.CharField(max_length=155, verbose_name='Наименование тега')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

class Post(models.Model):
    title = models.CharField(max_length=155, verbose_name='Наименование поста')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField(verbose_name='Контент', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка', blank=True)
    views = models.IntegerField(default=0, verbose_name='Колличество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категории')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Теги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
