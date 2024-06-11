from django.contrib import admin
from .models import *

# Class for category configuration
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','url', 'add_date','image_tag')
    search_fields = ('title',)
    list_filter = ('add_date',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 10


    # class Media:
    #    js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/7/tinymce.min.js ','js/script.js',)    

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
