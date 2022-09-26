from django.contrib import admin
from .models import Campaign, Subscriber

# Register your models here.

class CampaignModelAdmin(admin.ModelAdmin):
    list_display=('title','created_at','updated_at')
    search_fields=('title', 'description')
    list_per_page=10 #this is how to add pagination, useful when you have lots of records

class SubscriberModelAdmin(admin.ModelAdmin):
    list_display=('email','campaign','created_at')
    search_fields=('email','campaign__title','created_at')
    list_per_page=10

admin.site.register(Campaign,CampaignModelAdmin)
admin.site.register(Subscriber,SubscriberModelAdmin)