from django.contrib import admin
from .models import Label, Translation

class TranslationInline(admin.TabularInline):
    model = Translation
    extra = 1

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    inlines = [TranslationInline]
