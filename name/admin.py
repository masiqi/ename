from django.contrib import admin
from models import Name, Pinyin

class CnameListFilter(admin.SimpleListFilter):
    title = 'cname'
    parameter_name = 'cname'

    def lookups(self, request, model_admin):
        return (
            ('None', 'no cname'),
            ('Has', 'has cname'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'None':
            return queryset.filter(cname=None)
        if self.value() == 'Has':
            return queryset.exclude(cname=None)

class DescriptionListFilter(admin.SimpleListFilter):
    title = 'description'
    parameter_name = 'description'

    def lookups(self, request, model_admin):
        return (
            ('None', 'no description'),
            ('Has', 'has description'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'None':
            return queryset.filter(description=None)
        if self.value() == 'Has':
            return queryset.exclude(description=None)

class PronounceListFilter(admin.SimpleListFilter):
    title = 'pronounce'
    parameter_name = 'pronounce'

    def lookups(self, request, model_admin):
        return (
            ('None', 'no pronounce'),
            ('Has', 'has pronounce'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'None':
            return queryset.filter(pronounce=None)
        if self.value() == 'Has':
            return queryset.exclude(pronounce=None)


class NameOptions(admin.ModelAdmin):
    list_filter = (CnameListFilter, DescriptionListFilter, PronounceListFilter,)
    list_display = ['name', 'cname', 'gender', 'pronounce', 'description',] 

class PinyinOptions(admin.ModelAdmin):
    list_display = ['name', 'roma',]

admin.site.register(Name, NameOptions)
admin.site.register(Pinyin, PinyinOptions)

