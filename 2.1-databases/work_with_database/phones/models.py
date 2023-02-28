from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug':self.slug})
    
    def __str__(self):
        return self.name
    


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)