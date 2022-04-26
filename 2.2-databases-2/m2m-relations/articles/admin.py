from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):

    def clean(self):
        is_main_lst = []
        for form in self.forms:
            is_main_lst.append(form.cleaned_data['is_main'])
        if not any(is_main_lst):
            raise ValidationError('Укажите основной раздел')
        elif sum(is_main_lst) > 1:
            raise ValidationError('Основным должен быть только один раздел')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at']
    list_filter = ['published_at']
    inlines = [ArticleScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
