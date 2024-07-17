from django.contrib import admin
from .models import PersonalAppImg
from .models import PersonalAppText

class PersonalAppAdminText(admin.ModelAdmin):
    list_display = ('title', 'text')

class PersonalAppAdminIMG(admin.ModelAdmin):
    list_display = ('title', 'imgURL')

# Models are registered below.

admin.site.register(PersonalAppText, PersonalAppAdminText)
admin.site.register(PersonalAppImg, PersonalAppAdminIMG)
