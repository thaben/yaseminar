from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


from userprofile.models import AffiliateUser, SimpleUser
from seminar.models import Seminar

# Create your models here.
class Notifications(models.Model):
	message = models.TextField(max_length=200)
	created = models.DateTimeField(default=timezone.now)
	read = models.BooleanField(default=False)
	receiver = models.ForeignKey(SimpleUser,null=True,related_name='user_notification')
	n_sender = models.ForeignKey(AffiliateUser,blank=True, null=True)
	s_name = models.ForeignKey(Seminar,null=True)


	class Meta:
		verbose_name_plural ="Notifications" 
	
	#class Meta:
	#	order_by = "created"

	def __unicode__(self):
		return self.message




@receiver(post_save, sender=Seminar)
def CreateNotification(sender, instance, created, **kwargs):
	c = SimpleUser.objects.all().filter(seminar=instance)
	if not created:
		for users in c:
			d = Notifications.objects.filter(receiver=users).count()
			s = instance.tracker.changed()
			#print s.items()
			#for key, value in s.iteritems():
   			#	 print (key, value)
			b = Notifications.objects.create(message="Seminar %s has changed its info, click on the title !" % (instance.tracker.previous('title')), n_sender=instance.author, receiver=users, s_name = instance )
			#b = Notifications.objects.create(message=" Seminar Title %s its data" % (s.items()	), n_sender=instance.author, receiver=users, s_name = instance )
			#print 'OBJECTCREATED' , d
			if d >=5 :
				max_date = Notifications.objects.filter(receiver_id=users.id,s_name=instance).order_by('-created')
				print max_date  # gia na leitourgisei to revrerse prepei na exei proigithei taksinomisi
				e = max_date.reverse()[0]
				e.delete()
				#delete_qs = Notifications.objects.filter(receiver_id=users.id).exclude(id=max_date).delete()
				print 'diagrafikan'

#a.tracker.changed()