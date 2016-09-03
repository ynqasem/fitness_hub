from django.contrib import admin

from app.models import Gym, Image, CustomUser
admin.site.register(CustomUser)
admin.site.register(Gym)
admin.site.register(Image)