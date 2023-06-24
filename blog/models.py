from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    title_slug = models.SlugField(max_length=300, blank=True, null=True)
    subtitle = models.CharField(max_length=255)
    headerImage_url = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(null=True, blank=True)
    isPublished = models.BooleanField(default=False)
    categories = models.ManyToManyField('Category')
    tags = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_created=True, auto_now=True)

    def save(self, *args, **kwargs):
        self.title_slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Author(models.Model):
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    bio = models.CharField(max_length=255)
    avatar_url = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
