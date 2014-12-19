from django.contrib import admin
from images.models import FeaturedImage

# Register your models here.

@admin.register(FeaturedImage)
class FeaturedImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail','name', 'tagline', 'uploaded')
    ordering = ('-uploaded',)
   
    def thumbnail(self, obj):
        if obj.img:
            return '<img src="%s" style="height: 50px; width: auto">' % (obj.img.url)
        else:
            "no image"

    thumbnail.allow_tags = True


