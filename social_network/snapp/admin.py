from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Group)
admin.site.register(Message)
admin.site.register(AppUser)
# admin.site.register(Gallery)
admin.site.register(GalleryImage)  
admin.site.register(Contact)  

