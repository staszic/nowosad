from django.db import models

# Create your models here.
class Image(models.Model):
    alt_title = models.CharField(max_length=100)
    img_src = models.ImageField(null=True)

    def __str__(self):
        return self.alt_title
