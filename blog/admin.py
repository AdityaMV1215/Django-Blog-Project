from django.contrib import admin
from .models import Email, Phone, Country, Address, Author, Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["author", "date"]

admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

