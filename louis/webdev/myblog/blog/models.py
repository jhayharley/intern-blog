from django.conf import settings

from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.

class Index(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    heading                 = models.CharField(max_length=120)
    sub_heading             = models.CharField(max_length=120)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.heading)

class Tag(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    tag                     = models.CharField(max_length=120)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.tag)

class Category(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    category                = models.CharField(max_length=120)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.category)


POST_STATUS = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('hidden', 'Hidden')
)

class Post(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    post_list               = models.ForeignKey('Index', on_delete=models.CASCADE,)
    title                   = models.CharField(max_length=120)
    subtitle_or_caption     = models.CharField(max_length=120)
    banner_photo            = models.ImageField()
    author                  = models.CharField(max_length=120)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)
    tags                    = models.ManyToManyField(Tag)
    category                = models.ForeignKey('Category', on_delete=models.CASCADE,)
    body                    = models.TextField(max_length=1000)
    status                  = models.CharField(max_length=9, choices=POST_STATUS, default='published',)

    def __str__(self):
        return '{}'.format(self.post_list)