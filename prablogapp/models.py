from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class Image(models.Model):
    image_url = models.ImageField(storage=S3Boto3Storage(), default="www.google.com")
    image_title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.image_title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title



