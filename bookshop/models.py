from pydoc import describe
from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name="Title")
    image = models.ImageField(upload_to='Images/', verbose_name="Image", null=True)
    describe = models.TextField(verbose_name="Description",null=True)
    
    
    def __str__(self):
        file = "Title: " + self.title + " - " + "Description: " + self.describe
        return file
      
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
    