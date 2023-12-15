from django import template
from blog.models import Post, Category, Comment

register = template.Library()


@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts


@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid, approach=True).count()


@register.filter
def snippet(value, args=20):
    return value[:args] + "..."


@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(args):
    posts = Post.objects.filter(status=1).order_by('published_date')[:args]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}
