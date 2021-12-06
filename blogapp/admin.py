from django.contrib import admin
from .models import Card, Like, Comment, PostView

class CardAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'createdDate',
        'updatedDate',
    ]
    list_filter = ("title", 'createdDate', 'updatedDate')
    search_fields = ("title",)
admin.site.register(Card, CardAdmin)

admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(PostView)