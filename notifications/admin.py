from django.contrib import admin

from notifications.models import Notifications
# Register your models here.


class NotificationsAdmin(admin.ModelAdmin):
		list_filter = ('receiver','s_name','n_sender','created')
		list_display =('receiver','s_name','n_sender','created')

admin.site.register(Notifications,NotificationsAdmin)