from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):

    ''' Note Folder Model defined here'''

    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='notes')
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    reated_by = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Page(models.Model):

    '''Pages  Model defined here'''

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content =  models.TextField()


    def __str__(self):
        return self.title