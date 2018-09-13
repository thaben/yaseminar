from django.db import models
from django.utils import timezone
from django.db.models import permalink
from django.conf import settings

from model_utils import FieldTracker
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from userprofile.models import Profile, AffiliateUser,SimpleUser

# Create your models here.


class Category(models.Model):							#(exei simasia) na mpei to category apo panw gia na dimiourgithei swsta to Foreign Key
	name = models.CharField(max_length=50)
	seminarcounter = models.PositiveIntegerField(default=0)
	categoryimage = models.ImageField(default='avatarlogo.jpg')
	categoryimage_thumbnail = ImageSpecField(source='categoryimage',
                                      processors=[ResizeToFill(100, 100)],
                                      format='JPEG',
                                      options={'quality': 100})
	#slug = models.SlugField(max_length=100, unique=True, null=True)
	
	
	class Meta:
		verbose_name_plural = "Categories" # alliws sto admin panel tha fenotan Categorys#
	def __unicode__(self):  #__str__ aparxaiwmeno gt epistrefei bytes k oxi characters
		return self.name

	
	#@permalink
	#def get_absolute_url(self):
		#return ('view_category_post', None, { 'slug': self.slug })


class Seminar(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(AffiliateUser,on_delete=models.CASCADE)
	#slug = models.SlugField(max_length=100, unique=True, null=True)
	description = models.TextField(max_length=200,null=True)
	pub_date = models.DateTimeField(default=timezone.now)
	location = models.CharField(max_length=30)
	category = models.ForeignKey(Category,related_name='seminar_category', null=True)
	users_max = models.PositiveIntegerField(null=True)
	user_counter = models.IntegerField(default=0,null=True)
	usersbooked = models.ManyToManyField('userprofile.SimpleUser', blank=True)
	seminarimage = models.ImageField(default='avatarlogo.jpg')
	seminarimage_thumbnail = ImageSpecField(source='seminarimage',
                                      processors=[ResizeToFill(200, 200)],
                                      format='JPEG',
                                      options={'quality': 100})

	tracker = FieldTracker()
	#auto_now_add=True den emfanizete sto admin panel me auti tin entoli
	#deadline=model.DateTimeField('date deadline')
	#users_booked=model.IntegerField()
	#fees=models.FloatField(null=True)

	def __unicode__(self):
		return self.title







"""
You can do that by first getting the date of the 6th most recent entry. Then delete everything that is older than this date.

max_date = MyModel.objects.order_by('-date')[5]
delete_qs = MyModel.objects.filter(date__lt=max_date)
# it might be a good idea to inspect the result at this point
# to ensure you are deleting the right stuff
delete_qs.delete()
"""


"""prepei na grapsw ena view pou tha kanei diagrafei ola ta notification otan read=TRUE, notifications/clear"""


#if request.user in receiver



#for affiliate





	
	#@permalink
	#def get_absolute_url(self):
		#return ('view_seminar_post', None, { 'slug': self.slug })
	


#class UserRegisterSeminar(models.Model):
	#user=models.ForeignKey(settings.AUTH_USER_MODEL)
	#seminar_name=models.ForeignKey(Seminar)
