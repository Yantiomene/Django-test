from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from .models import Post

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)

admin.site.unregister(Group)

admin.site.site_header = "Keecash Administration"

admin.site.site_title = "Keecash"