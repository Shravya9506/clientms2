from django.contrib import admin

from .models import Client, Comment, OwnedCar

class CommentInline(admin.TabularInline):
    model = Comment

class OwnedCarInline(admin.TabularInline):
    model = OwnedCar

class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        OwnedCarInline
    ]

admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(OwnedCar)
