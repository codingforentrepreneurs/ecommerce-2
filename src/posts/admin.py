from django.contrib import admin
from .models import Post, PostFeatured

# Register your models here.
# llamamos la clase admin para agregar filtrado lista de orden etc y estilo a la tabla.

class PostModelStyle(admin.ModelAdmin):
        list_display = ['title','updated', 'timestamp']
        list_display_links = ['title']
        list_filter = ['category', 'updated']
        search_fields = ['title','author', 'category']

        class Meta:
                model = Post

admin.site.register(Post, PostModelStyle)
admin.site.register(PostFeatured)
