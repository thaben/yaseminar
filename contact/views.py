from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from contact.forms import ContactForm, MassSeminarEmailForm
from seminar.models import Seminar
from seminar.decorators import user_is_affiliate
# our view
@login_required
def contactemail(request):
	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name')
			contact_email = request.POST.get('contact_email')
			
			form_content = request.POST.get('content')
			template = get_template('contact/contact_template.txt')
			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
			})
			content = template.render(context)

			email = EmailMessage(
				"New contact form submission",
				content,
				"Your website" +'',
				['youremail@gmail.com'],
				headers = {'Reply-To': contact_email }
			)
			email.send()
			print 'stalthikee emailll'
			return redirect('contact')

	return render(request, 'contact/contact.html', {
		'form': form_class,
	})




@user_is_affiliate
@login_required
def MassEmailUsers(request, seminar_id):
	seminar = Seminar.objects.get(id=seminar_id)
	userslist = seminar.usersbooked
	form = MassSeminarEmailForm
	if request.method == 'POST':
			content = request.POST.get('content')
			for u in userslist.all():
				uemail = User.objects.get(username=u)
				send_mail('Subject about seminar', content, 'yaseminar@gmail.com', [uemail.email])

	return render(request, 'contact/contactmass.html', {
		'form': form,
		'seminar': seminar,
	})
