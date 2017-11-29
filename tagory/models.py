from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name     = models.CharField(max_length=100, unique=True)
    slug     = models.SlugField(allow_unicode=True, blank=True)
    created  = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('tagory:', kwargs={'slug':self.slug})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = self.slug.strip().replace(' ', '-')
        else:
            self.slug = self.name.strip().replace(' ', '-')

        super(Tag, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100)
