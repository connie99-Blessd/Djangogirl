from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()  # Save the object after publishing

    def __str__(self):
        return self.title  # String representation for the object, typically used in the admin


