from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

from userprofile.forms import UserForm, ProfileForm, ProfileEditForm
from userprofile.models import Profile
from seminar.models import Seminar
from seminar.decorators import user_has_registered, user_is_affiliate



@login_required
@user_has_registered
def addinfo(request):
	if request.method == "POST":
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			profileform = profile_form.save(commit=False)
			profileform.addinfoflag = True
			profileform.save()
			user_form.save()

			#return redirect('home')# HttpResponseRedirect can accept a model, view, or url as it's "to" argument. So it is a little more flexible in what it can "redirect" to.
			return HttpResponseRedirect(reverse('home'))
	else:
		user_form = UserForm()
		profile_form = ProfileForm()
			#else:
				#raise PermissionDenied

	return render(request, 'profile/profile_form.html', {
			'user_form': user_form,
			'profile_form': profile_form
		})



@login_required
def ProfileEdit(request, pk=None, template_name='profile/profile_form.html'):
	user = request.user
	profile = request.user.profile
	if request.user.id == profile.user_id:  #elenxos gia to an to id tou profile einai tou xristi pou kanei request
		user_form = UserForm(request.POST or None, instance = request.user) # xreaizete to or non edw gia na fanous ta dedomena stin forma
		profile_form = ProfileEditForm(request.POST or None, instance = request.user.profile)
		if request.method == "POST":
			if user_form.is_valid() and profile_form.is_valid():
				profile_form.save()
				user_form.save()
		
				# Save was successful, so redirect to another page

				return HttpResponseRedirect(reverse('home'))
	else:
		raise PermissionDenied	
				
	return render(request, template_name, {
		'user_form': user_form,
		'profile_form': profile_form
	})



@login_required
def UserProfile(request, username):
	if request.user.username == username:
		user = get_object_or_404(User, username=username) #gia na min exi prosvasi s alles selides opws /accounts/ALLOUSERNAME/
		profile = Profile.objects.get(user=user)
	else:
		raise PermissionDenied

	return render(request, 'profile/profile_user.html',{
			'profile': profile,
		})



@login_required
@user_is_affiliate
def AffiliateProfile(request, username):	
	if request.user.username == username:
		user = get_object_or_404(User, username=username)
		seminarlist = Seminar.objects.filter(author_id__user_id = user.id)
		print seminarlist
		paginator = Paginator(seminarlist, 10)
		page = request.GET.get('page')
		try:
			seminarlist = paginator.page(page)
		except PageNotAnInteger:
			seminarlist = paginator.page(1)
		except EmptyPage:
			seminarlist = paginator.page(paginator.num_pages)
	else:
		raise PermissionDenied
	return render(request, 'profile/profile_affiliate.html', {
		'seminarlist':seminarlist
		})


#	def get_redirect_url(self, param):
#		return reverse_lazy('resource-view',
#							kwargs={'param': param},
#							current_app='myapp')




#def AffiliateProfile(request, username):
	#username = User.objects.get(username=request.user.username)
	#return render(request, 'profile_affiliate.html', {
	#		'username': username,
	#	})






