from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def uplode_image_news(self, filename):
    return f"new/{self.id}/{filename}"

class New(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    time_add = models.DateTimeField(auto_now_add=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to=uplode_image_news)

    def __str__(self):
        return self.title

    def image_url(self):
        if self.image:
            return self.image.url
