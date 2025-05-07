from django.contrib import admin
from .models import Order, Review

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'tour', 'date', 'person', 'child', 'created_at')
    search_fields = ('name', 'phone_number', 'tour__name')
    list_filter = ('date', 'tour')
    readonly_fields = ('created_at',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rating', 'comment', 'tour', 'created_at')
    search_fields = ('username', 'email', 'comment')
    list_filter = ('rating', 'tour')
    readonly_fields = ('created_at', 'updated_at')