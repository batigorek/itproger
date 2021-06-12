from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Name', max_length=50, default='')
    anons = models.CharField('Anons', max_length=250, default='')
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date')

    def __str__(self):
        return f'News:{self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'