from django.contrib import admin
from .models import (
    User, Phone, Hour, Mailing, Message
)


admin.site.register(User)
admin.site.register(Phone)
admin.site.register(Hour)
admin.site.register(Mailing)
admin.site.register(Message)
