from django.shortcuts import render

from notifications.models import Notifications
from userprofile.models import SimpleUser

# Create your views here.



def Notify(request, username):
	#u = SimpleUser.objects.get(user=request.user)
	n = Notifications.objects.filter(receiver__user=request.user.profile)
	return render(request, 'profile/notifications.html', {
			'notifications': n ,
		})
#def DeleteNotification(request):
			