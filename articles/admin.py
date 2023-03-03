from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        flag = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') is True:
                flag += 1
            print(form.cleaned_data.get('is_main'))
        if flag > 1:
            raise ValidationError('Главный раздел может быть только один!')

        elif flag == 0:
            raise ValidationError('Не выбран Главный раздел!')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 0



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']