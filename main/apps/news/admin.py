from django.contrib import admin
from .models import News, Comments
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comments


class NewsAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(News, NewsAdmin)
admin.site.register(Comments)
