from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=120)
    count = models.IntegerField(default=0)

class Posts(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    slug = models.CharField(max_length=500)
    category = models.ManyToManyField(Category, related_name='post_category', blank=True)
    time_stamp = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class GithubProjects(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    slug = models.CharField(max_length=500)
    category = models.ManyToManyField(Category, related_name='github_project_category', blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Github Project"
        verbose_name_plural = "Github Projects"

class UserEmails(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"

class Newsletter(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    content = models.TextField()
    time_stamp = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"