from django.contrib import admin

# Register your models here.

#Board app 관련 추가
from .models import Board                                               

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['subject','price','photo','category']
    # raw_id_fields = ['author']
    # list_filter = ['created','updated','author']
    # search_fields = ['text','created','author__username']
    # ordering = ['-updated','-created']

admin.site.register(Board, PhotoAdmin)