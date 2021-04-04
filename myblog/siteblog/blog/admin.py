from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Tag, Post
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'get_photo') # какие поля будут отображаться в админке
    list_display_links = ('id', 'title') # поля на которые мы можем кликнуть
    search_fields = ('title',) # поля по которым идет поиск
    list_filter = ('category', 'tags') # поля по которым можем фильтровать список статей
    save_on_top = True
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'author', 'photo', 'get_photo', 'views', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
    save_as = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Миниатюра'

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
