from django.contrib import admin
from core.models import *
from django.utils.html import format_html
from django.conf.urls import url, include
# Register your models here.
def minus_one_Tip(TipAdmin, request, queryset):
    for Tip in queryset:
        Tip.amount_available = Tip.amount_available - 1
        Tip.save()
        minus_one_Tip.short_description = 'Зменшити кількість на 1'
def plus_one_Tip(TipAdmin, request, queryset):
    for Tip in queryset:
        Tip.amount_available = Tip.amount_available + 1
        Tip.save()
        minus_one_Tip.short_description = 'Збільшити кількість на 1'

def minus_one_Thrust(ThrustAdmin, request, queryset):
    for Thrust in queryset:
        Thrust.amount_available = Thrust.amount_available - 1
        Thrust.save()
        minus_one_Thrust.short_description = 'Зменшити кількість на 1'
def plus_one_Thrust(ThrustAdmin, request, queryset):
    for Thrust in queryset:
        Thrust.amount_available = Thrust.amount_available + 1
        Thrust.save()
        minus_one_Thrust.short_description = 'Збільшити кількість на 1'

def minus_one_SteelWheel(SteelWheelAdmin, request, queryset):
    for SteelWheel in queryset:
        SteelWheel.amount_available = SteelWheel.amount_available - 1
        SteelWheel.save()
        minus_one_SteelWheel.short_description = 'Зменшити кількість на 1'
def plus_one_SteelWheel(SteelWheelAdmin, request, queryset):
    for SteelWheel in queryset:
        SteelWheel.amount_available = SteelWheel.amount_available + 1
        SteelWheel.save()
        minus_one_SteelWheel.short_description = 'Збільшити кількість на 1'


def minus_one_Anthers(AnthersAdmin, request, queryset):
    for Anthers in queryset:
        Anthers.amount_available = Anthers.amount_available - 1
        Anthers.save()
        minus_one_Anthers.short_description = 'Зменшити кількість на 1'
def plus_one_Anthers(AnthersAdmin, request, queryset):
    for Anthers in queryset:
        Anthers.amount_available = Anthers.amount_available + 1
        Anthers.save()
        minus_one_Anthers.short_description = 'Збільшити кількість на 1'

def minus_one_Bearing(BearingAdmin, request, queryset):
    for Bearing in queryset:
        Bearing.amount_available = Bearing.amount_available - 1
        Bearing.save()
        minus_one_Bearing.short_description = 'Зменшити кількість на 1'
def plus_one_Bearing(BearingAdmin, request, queryset):
    for Bearing in queryset:
        Bearing.amount_available = Bearing.amount_available + 1
        Bearing.save()
        minus_one_Bearing.short_description = 'Збільшити кількість на 1'

def minus_one_BrakePads(BrakePadsAdmin, request, queryset):
    for BrakePads in queryset:
        BrakePads.amount_available = BrakePads.amount_available - 1
        BrakePads.save()
        minus_one_BrakePads.short_description = 'Зменшити кількість на 1'
def plus_one_BrakePads(BrakePadsAdmin, request, queryset):
    for BrakePads in queryset:
        BrakePads.amount_available = BrakePads.amount_available + 1
        BrakePads.save()
        minus_one_BrakePads.short_description = 'Збільшити кількість на 1'

def minus_one_FilterAdmin(FilterAdmin, request, queryset):
    for FilterAdmin in queryset:
        FilterAdmin.amount_available = FilterAdmin.amount_available - 1
        FilterAdmin.save()
        minus_one_FilterAdmin.short_description = 'Зменшити кількість на 1'
def plus_one_FilterAdmin(FilterAdmin, request, queryset):
    for FilterAdmin in queryset:
        FilterAdmin.amount_available = FilterAdmin.amount_available + 1
        FilterAdmin.save()
        minus_one_FilterAdmin.short_description = 'Збільшити кількість на 1'

class TipAdmin(admin.ModelAdmin):
    list_display = ['detail_number','description','short_description_number','diameter1', 'step1','diameter2','step2','length','cone','mounting_side','price','amount_available','image']
    search_fields = ['detail_number','description','short_description_number','diameter1', 'step1','diameter2','step2','length','cone','mounting_side','price','amount_available','image']
    actions = [minus_one_Tip, plus_one_Tip]
#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             url(
#                 r'^(?P<account_id>.+)/deposit/$',
#                 self.admin_site.admin_view(self.process_deposit),
#                 name='account-deposit',
#             ),
#             url(
#                 r'^(?P<account_id>.+)/withdraw/$',
#                 self.admin_site.admin_view(self.process_withdraw),
#                 name='account-withdraw',
#             ),
#         ]
#         return custom_urls + urls
#     def account_actions(self, obj):
#         return format_html(
#             '<a class="button" href="{}">Deposit</a>&nbsp;'
#             '<a class="button" href="{}">Withdraw</a>',
#             reverse('admin:account-deposit', args=[obj.pk]),
#             reverse('admin:account-withdraw', args=[obj.pk]),
#         )
#     account_actions.short_description = 'Account Actions'
#     account_actions.allow_tags = True
class ThrustAdmin(admin.ModelAdmin):
    list_display = ['detail_number','description','short_description_number','diameter1', 'step1','diameter2','step2','length','price','amount_available','image']
    search_fields = ['detail_number','description','short_description_number','diameter1', 'step1','diameter2','step2','length','price','amount_available','image']
    actions = [minus_one_Thrust, plus_one_Thrust]
class SteelWheelAdmin(admin.ModelAdmin):
    list_display = ['detail_number','description','short_description_number','diameter1','diameter2','length','price','amount_available','image']
    search_fields = ['detail_number','description','short_description_number','diameter1','diameter2','length','price','amount_available','image']
    actions = [minus_one_SteelWheel, plus_one_SteelWheel]
class AnthersAdmin(admin.ModelAdmin):
    list_display = ['detail_number','description','short_description_number','diameter1','diameter2','length','price','amount_available','image']
    search_fields = ['detail_number','description','short_description_number','diameter1','diameter2','length','price','amount_available','image']
    actions = [minus_one_Anthers, plus_one_Anthers]

class BearingAdmin(admin.ModelAdmin):
    list_display = ['detail_number','description','short_description_number','diameter1','diameter2','height','price','amount_available','image']
    search_fields = ['detail_number','description','short_description_number','diameter1','diameter2','height','price','amount_available','image']
    actions = [minus_one_Bearing, plus_one_Bearing]
class BrakePadsAdmin(admin.ModelAdmin):
    list_display = ['detail_number','description','short_description_number','mounting_data','price','amount_available','image']
    search_fields = ['detail_number','description','short_description_number','mounting_data','price','amount_available','image']
    actions = [minus_one_Bearing, plus_one_Bearing]
class FilterAdmin(admin.ModelAdmin):
    list_display = ['detail_number','description','short_description_number','mounting_data','price','amount_available','image']
    search_fields = ['detail_number','description','short_description_number','mounting_data','price','amount_available','image']
    actions = [minus_one_Bearing, plus_one_Bearing]  



admin.site.register(Tip, TipAdmin)
admin.site.register(Thrust, ThrustAdmin)
admin.site.register(SteelWheel, SteelWheelAdmin)
admin.site.register(Anthers, AnthersAdmin)
admin.site.register(Bearing, BearingAdmin)
admin.site.register(BrakePads, BrakePadsAdmin)
admin.site.register(Filter, FilterAdmin)
admin.site.register(Ordered)
admin.site.register(GeneralInfo)


