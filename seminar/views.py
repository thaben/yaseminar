from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

from userprofile.models import AffiliateUser, SimpleUser, Profile
from seminar.forms import SeminarForm
from seminar.models import Category, Seminar
from seminar.decorators import user_is_affiliate
from .filters import SeminarFilter

def home(request):

# thelei douleia edw, mipws  mpei sto add  smeminar to counter etsi wste na prostithete
	category = Category.objects.all().order_by('-seminarcounter')[:7]
	#seminarcounter = category.seminar_category.all().count()
														  #esvisa to context=locals() opws einai apo katw gia na dokimasw tin leitourgikotita
	return render(request, 'home.html', {
			'categories':category,
			# 
	#	'seminarcounter':seminarcounter
		})


def search(request): 
	seminar_list = Seminar.objects.all()
	if request.method == 'GET':
		seminar_filter = SeminarFilter(request.GET, queryset=seminar_list)
	return render(request, 'search.html', {
		'filter': seminar_filter
	})


	
def about(request):
	context = locals()
	template = 'about.html'
	return render(request,template,context)

def seminars(request):
	seminarlist = Seminar.objects.all().order_by('pub_date')
	return render('view_seminars.html',
		{'seminarlist':seminarlist,

	 })



def seminardetails(request, seminar_id=1):
	seminar = Seminar.objects.get(id=seminar_id)
	a = seminar.author
	user = User.objects.get(username=a)
	profile = Profile.objects.get(user=user)
	
	return render(request, 'view_seminar.html', {
		'seminar': seminar,
		'profile': profile,
		'user1': user,
	} )


#
def categories(request, category_id=1):
	categories = Category.objects.all().order_by('-seminarcounter')
	paginator = Paginator(categories, 6)
	page = request.GET.get('page')
	try:
		categorylist = paginator.page(page)
	except PageNotAnInteger:
		categorylist = paginator.page(1)
	except EmptyPage:
		categorylist = paginator.page(paginator.num_pages)

	return render(request, 'view_categories.html', {
		'categories': categories,
		'categorylist': categorylist
	} )

def category(request, category_id=1):
	category = Category.objects.get(id=category_id)
	seminars = category.seminar_category.all().order_by('title') #xrisi related name apo models seminar_cateogoryy
	print seminars
	paginator = Paginator(seminars, 9)
	page = request.GET.get('page')
	try:
		seminarlist = paginator.page(page)
	except PageNotAnInteger:
		seminarlist = paginator.page(1)
	except EmptyPage:
		seminarlist = paginator.page(paginator.num_pages)
	return render(request, 'view_category.html', {
		'category': category,
		'seminarlist': seminarlist
	} )



@login_required
@user_is_affiliate
def addseminar(request):
	if request.method == "POST":
		
		form = SeminarForm(request.POST)
		if form.is_valid():
			seminar = form.save(commit=False)
			seminar.author_id = request.user.id
			c = Category.objects.get(id=seminar.category.id)
			print seminar.author_id, seminar.category.seminarcounter , seminar.category.id , request.user.id
			c.seminarcounter +=1
			print c.seminarcounter
			c.save()
			seminar.save()

			#id = seminar.id
			#t, created = AffiliateSeminars.objects.get_or_create(affiliatebooked=seminar.author, name_of_seminar_id=id) # gia na exoume ton neo pinaka AffiliateSeminars me foreign keys
			#t.save()

			return redirect('home')
	else:
		form = SeminarForm()
	
	return render(request, 'add_seminar.html',
		{'form':form,
	 })

#edw epeidi exoume class based views ta decorators mas xrisimipoioun @method_decorator
class SeminarUpdate(UpdateView):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SeminarUpdate, self).dispatch(*args, **kwargs)
	
	@method_decorator(user_is_affiliate)
	def dispatch(self, *args, **kwargs):
		return super(SeminarUpdate, self).dispatch(*args, **kwargs)

	form_class = SeminarForm # den mporw na exw to fields mazi 
	template_name = 'add_seminar.html'
	model = Seminar
	#fields = ['title'] # form_class i fields
	success_url = reverse_lazy('home') #lazy giati einai generic class-based view

#elenxos ean o xristis einai o author
	def get_object(self, *args, **kwargs):
		obj = super(SeminarUpdate, self).get_object(*args, **kwargs)
		a = AffiliateUser.objects.get(user_id=self.request.user.id)  #giati exw foreign key sto affiliateuser pinaka , pou ama exei vgalei to tag affiliate kapoios allazei to id kai den einai to idio m to user_id foreign key
		if obj.author != a:
			raise Http404 #You can add a file called 404.html to your templates folder and Django will use this content to display to users during 404 errors.
		return obj

class SeminarDelete(DeleteView):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SeminarDelete, self).dispatch(*args, **kwargs)
	
	@method_decorator(user_is_affiliate)
	def dispatch(self, *args, **kwargs):
		return super(SeminarDelete, self).dispatch(*args, **kwargs)
#elenxos ean o xristis einai o author
	def get_object(self, *args, **kwargs):
		obj = super(SeminarDelete, self).get_object(*args, **kwargs)
		a = AffiliateUser.objects.get(user_id=self.request.user.id)
		if obj.author != a:
			print obj.author.id , self.request.user.id
			raise Http404 #or Http404
		return obj
    

	template_name = 'delete_seminar.html'
	model = Seminar
	#success_url = reverse_lazy('home')
	def get_success_url(self,*args, **kwargs):
		obj = super(SeminarDelete, self).get_object(*args, **kwargs)
		c = Category.objects.get(id=obj.category.id)
		c.seminarcounter-=1
		c.save()
		return reverse_lazy('home')



from django.contrib.auth.models import User



@login_required
def UserBook(request,seminar_id=1):
	print 'phase 2'
	d = Profile.objects.get(user_id=request.user.id)
	e = SimpleUser.objects.get(user_id=d.id)
	if not Seminar.objects.filter(usersbooked__user=d): # name_of_seminar_id=seminar_id).exists():

		print 'stage 1'
		if request.method == "POST":
			print 'stage 2'
			s = Seminar.objects.get(id=seminar_id)
			s.usersbooked.add(e)
			s.user_counter+=1
			s.save()

			print 'APOTHIKEUTIKAN'
		else: raise Http404

		return redirect('home')
			
	return render(request, 'seminar_register.html')

				
				#unbook
				#	else:
				#		if request.method == "POST":
				#			print 'stage unbook'
				#			s = Seminar.objects.get(id=seminar_id)
				#			s.usersbooked.remove(e)
					#		s.user_counter-=1
				#			s.save() 
				#	
				#		print 'stag"e unbook COMPLETED'
				#





	











	#if request.method == "POST":
	#   action = request.POST.get('action')
   # if action == 'Edit':









	#context = RequestContext(request)  
	#if request.method == 'GET':
	#   sem_id = request.GET['seminar_id']
##
	#if sem_id:
#       sem = Seminar.objects.get(id=sem_id)
	#   if sem:
	#       usercounter = sem.user_counter + 1
	#       sem.usercounter =  usercounter
	#       sem.save()

#   return HttpResponse(usercounter) 









#def seminarusers(request, seminar_id=1):
   # seminarusers = AffiliateSeminars.get_object_or_404(nameofseminar_id=seminar_id)
	#return render(request, 'listofusersinseminar.html', {
   #     'semianrusers': seminarusers,
   # } )


#def seminarbooking(request, seminar_id=1):
  #  user = request.user
   # seminarname = AffiliateSeminars.get(AffiliateSeminars_id=seminar_id)


	


	#return render_to_response('view_seminar.html',
		#{'seminar':Seminar.objects.get(id=seminar_id) }) # edw vazoume tin get methodo gia na paroume to id etsi wste na mpei  sta urls.py


