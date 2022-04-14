from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField() 
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # Add in thumbnail later
    # Add in author later

    # Built-in function that will view the Article as a title of the instance
    def __str__(self):  
        return self.title