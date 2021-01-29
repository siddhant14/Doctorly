from django.conf import settings
from django.db import models

# Create your models here.

class Hospital(models.Model):
    Image = models.ImageField(upload_to="Images/")
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Link = models.CharField(max_length=500)

    # class Meta:
    #     db_table = 'doctorly'