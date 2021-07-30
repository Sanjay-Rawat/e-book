from django.db import models
class Books(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    about = models.TextField(max_length=1000) 
    fileUrl = models.TextField(max_length=1000)
    posterUrl = models.TextField(max_length=1000)
    category = models.CharField(max_length=50)
    isForMembers = models.BooleanField(default=True)
    class Meta:
        db_table = 'book'