from django.db import models


# Create your models here.


class URLs(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    threshold = models.IntegerField()
    failed_times = models.IntegerField(default=0)


class Requests(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    url = models.ForeignKey(URLs, on_delete=models.CASCADE)
    result = models.IntegerField()
