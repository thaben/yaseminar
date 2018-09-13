from django.contrib import admin
from seminar.models import Seminar, Category
# Register your models here.


#class SeminarAdmin(admin.ModelAdmin):
   # exclude = ['posted']
   # prepopulated_fields = {'slug': ('title',)}

#class CategoryAdmin(admin.ModelAdmin):
   # prepopulated_fields = {'slug': ('name',)}


class SeminarAdmin(admin.ModelAdmin):
		filter_horizontal = ('usersbooked',)
		search_fields = ('title','location')

class SeminarStackedInline(admin.StackedInline):
	model = Seminar
	extra = 1
	
	


class CategoryAdmin(admin.ModelAdmin):
	search_fields = ['name']
	inlines = [
		SeminarStackedInline,
		]
	class Meta:
		model = Category



admin.site.register(Category, CategoryAdmin)
admin.site.register(Seminar, SeminarAdmin)


#admin.site.register(Category)