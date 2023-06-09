from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.item


class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, related_name='favorite', default=None, blank=True)

    def __str__(self):
        return str(self.id)


# Add in a comments model for here
class Comment(models.Model):
    content = models.TextField(max_length=300)
    book_origin = models.ForeignKey(Book, on_delete=models.CASCADE)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    publishdate = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)





