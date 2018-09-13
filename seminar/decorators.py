from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from userprofile.models import Profile
from seminar.models import Seminar



def user_is_affiliate(function):
    def wrap(request, *args, **kwargs):
    	cuser = request.user.id
        cobject = get_object_or_404(Profile, user_id=cuser)
        caffiliate = True
        if cobject.affiliate == caffiliate:
       	 return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__=function.__doc__		#ektupwnei tin sunartisi pou tha kalesoume sta views px . def addseminar
    wrap.__name__=function.__name__     #den ta ftiaxnei mono tou epiedi einai partia object, edw emfanizete to apotelesma apo def addseminar
    return wrap


def user_has_registered(function):
    def wrap(request, *args, **kwargs):
    	cfuser = request.user.id
        cfobject = Profile.objects.get(user_id=cfuser)
        cflag = False
        if cfobject.addinfoflag == cflag:
       	 return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__=function.__doc__
    wrap.__name__=function.__name__
    return wrap