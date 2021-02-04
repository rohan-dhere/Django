from django.db import models

#model to generate database
class blogs(models.Model): 
    project_name = models.CharField(max_length=200) 
    data = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')