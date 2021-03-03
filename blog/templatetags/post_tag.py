from django import template
from blog.models import Post, Comment

register = template.Library()


@register.inclusion_tag('blog/latest_posts.html')
def latest_posts():
    context = {
        'last_5_posts': Post.objects.all()[:5]
    }
    return context


@register.inclusion_tag('blog/latest_comments.html')
def latest_comments():
    context = {
        'last_5_comments': Comment.objects.all()[:5]
    }
    return context