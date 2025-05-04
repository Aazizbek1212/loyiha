from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rating', 'comment', 'tour', 'created_at')
    search_fields = ('username', 'email', 'comment')
    list_filter = ('rating', 'tour')
    readonly_fields = ('created_at', 'updated_at')  # agar siz BaseModel ishlatayotgan bo'lsangiz

