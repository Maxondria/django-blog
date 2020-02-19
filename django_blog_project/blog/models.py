from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @classmethod
    def find_all(cls):
        return cls.objects.all()

    @classmethod
    def find_all_by_user(cls, user):
        return cls.objects.filter(author=user).order_by('-date_posted')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
