from django.db import models
#from geoposition.fields import GeopositionField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


#class ProfileManager(models.Manager):
   # def get_affiliate(self):
    #    return self.filter(affiliate=True)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)   #OneToOneField is similar a ForeignKey with the attribute unique=True.
	bio = models.TextField(max_length=500, blank=True)
	birth_date = models.DateField(null=True, blank=False)
	affiliate = models.BooleanField(default=False)
	addinfoflag = models.BooleanField(default=False)
	avatar = models.ImageField(default='avatarlogo.jpg')
	avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(120, 120)],
                                      format='JPEG',
                                      options={'quality': 100})


	#profile = Profile.objects.all()[0]
	#print(profile.avatar_thumbnail.url)    # > /media/CACHE/images/982d5af84cddddfd0fbf70892b4431e4.jpg
	#print(profile.avatar_thumbnail.width)  # > 100
	#objects = ProfileManager()

	def __unicode__(self):
		return unicode(self.user)

class AffiliateUser(models.Model):
	user = models.OneToOneField(Profile)
	
	def __unicode__(self):
		return unicode(self.user)




class SimpleUser(models.Model):
	user = models.OneToOneField(Profile, null=False, blank=False)

	def __unicode__(self):
		return unicode(self.user)






@receiver(post_save, sender=Profile)
def create_users_profile(sender, instance, created, **kwargs):
	print 'phase 1'
	e = Profile.objects.get(user=instance.user)
	b = e.affiliate
	if created:
			SimpleUser.objects.create(user=instance)
			print 'phase 2'
	elif b == True:
			uid = instance.id
			try:
			   s = SimpleUser.objects.get(id=uid)
			   s.delete()
			except SimpleUser.DoesNotExist:
				c = AffiliateUser.objects.get_or_create(user=instance)
			print 'phase 3'
			
#@receiver(post_save, sender=Profile)
#def save_affiliateuser_profile(sender, instance, **kwargs):
#	instance.AffiliateUser.save()

#@receiver(post_save, sender=Profile)
#def save_simpluser_profile(sender, instance, **kwargs):
#	instance.SimpleUser.save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
