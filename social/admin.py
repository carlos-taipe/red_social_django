from django.contrib import admin
from .models import Profile,Post,Relationship
# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Relationship)