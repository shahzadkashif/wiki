from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    last_update= models.DateTimeField(auto_now=True)
    
    def __str__(self):
    	return self.title

    def get_absolute_url(self):
    	return f"/pages/{self.id}/"