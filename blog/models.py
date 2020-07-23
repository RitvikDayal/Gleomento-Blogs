from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    summary = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.content:
            self.summary = self.content[:60]
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return 'Title: {}\nAuthor: {}'.format(self.title, self.author)
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
