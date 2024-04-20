from django.db import models
lorem = 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Explicabo esse quas rerum repellat hic eum? Provident id fugit dolorum possimus!'
lorem2 = 'Lorem ipsum dolor sit, amet consectetur.'

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50, default='My new blog')
    body = models.TextField(default=lorem)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    description = models.TextField(default=lorem2)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')

    def __str__(self) -> str:
        return f'{self.description} on {self.blog.title}'