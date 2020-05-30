from django.db import models


class projects(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='image/')
    summary = models.CharField(max_length=250)
    pub_date = models.DateTimeField()

