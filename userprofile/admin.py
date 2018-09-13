from django.contrib import admin
from userprofile.models import Profile, AffiliateUser, SimpleUser
# Register your models here.


#class SeminarAdmin(admin.ModelAdmin):
   # exclude = ['posted']
   # prepopulated_fields = {'slug': ('title',)}

#class CategoryAdmin(admin.ModelAdmin):
   # prepopulated_fields = {'slug': ('name',)}


class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user','birth_date', 'affiliate')
	list_filter = ['affiliate']
	search_fields = ['user__username']

#admin.site.register(Profile)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(AffiliateUser)
admin.site.register(SimpleUser)

