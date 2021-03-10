from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}  {self.title}'


    def get_absolute_url(self):
        # return f'/detail/{self.pk}'
        return reverse('detail', args=(self.pk,))



class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    email = models.EmailField(verbose_name='الايميل')
    body = models.TextField(verbose_name='التعليق')
    comment_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-comment_date']

    # realted_name -> used when we want to call the comments from the posts in the view

    def __str__(self):
        return f'''
علق
{self.name}
علي التدوينة
({self.post.title})
                '''
