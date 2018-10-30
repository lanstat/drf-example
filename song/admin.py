from django.contrib import admin
from .models import Track, Genre, PlayList

# Register your models here.


admin.site.register(Track)
admin.site.register(Genre)
admin.site.register(PlayList)
#admin.site.register(PlayListContent)