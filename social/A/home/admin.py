from django.contrib import admin
from .models import Post, Comment, Vote

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'created')
    search_fields = ('slug', 'body')
    list_filter = ('update',)
    prepopulated_fields = {'slug':('body',)}
    raw_id_fields = ('user',)

#admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created', 'is_reply')
    raw_id_fields = ('user', 'post', 'reply')



admin.site.register(Vote)