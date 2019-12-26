from django.contrib import admin
from .models import Posts, GithubProjects, UserEmails, Newsletter
# Register your models here.

admin.site.register(Posts)
admin.site.register(GithubProjects)
admin.site.register(UserEmails)
admin.site.register(Newsletter)