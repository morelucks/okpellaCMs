from django.contrib import admin

# Register your models here.
from .models import Category, User,Contact, About

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(About)
