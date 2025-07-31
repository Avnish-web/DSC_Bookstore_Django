from django.db import models

class Book(models.Model):
       title = models.CharField(max_length=200)
       author = models.CharField(max_length=100)
       pdf = models.FileField(upload_to='books/')
       image = models.ImageField(upload_to='images/')
       created_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return self.title