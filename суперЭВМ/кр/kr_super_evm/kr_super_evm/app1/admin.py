from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Wall)
admin.site.register(models.UserProfile)
admin.site.register(models.Message)
admin.site.register(models.UserAll)
admin.site.register(models.Friend)
admin.site.register(models.Like)
admin.site.register(models.NotesAboutUser)

