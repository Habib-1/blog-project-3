from django.contrib import admin
from .models import user_image,blog_post,Category
# Register your models here.
admin.site.register(user_image)

class blog_postAdmin(admin.ModelAdmin):
    list_display=('title','author','post_time',)
    search_fields=('title','author',)
    list_filter=('author',)
admin.site.register(blog_post,blog_postAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category',)}
    list_display=('category','slug')
admin.site.register(Category,CategoryAdmin)