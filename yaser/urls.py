from django.conf import settings #egw to prosthesa
from django.conf.urls.static import static #egw to prosthesa
from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse

from seminar.views import SeminarUpdate, SeminarDelete
from userprofile.views import addinfo, UserProfile #ProfileUpdate
from contact.views import contactemail, MassEmailUsers
from notifications.views import Notify



#from seminar import views
urlpatterns = [
    # Examples:
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^secret/', include(admin.site.urls)),
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'seminar.views.home', name= 'home'),
    url(r'^contactemailmass/(?P<seminar_id>\d+)/$', 'contact.views.MassEmailUsers', name='contactemailmass'),
    url(r'^contactemail/$', 'contact.views.contactemail', name='contactemail'),
    url(r'^search/$', 'seminar.views.search', name='search'),
    url(r'^about/$', 'seminar.views.about', name= 'about'),
   	url(r'^seminars/all/$', 'seminar.views.seminars', name= 'seminars'),
   	url(r'^seminar/(?P<seminar_id>\d+)/$', 'seminar.views.seminardetails', name='seminardetails'),
   	url(r'^seminar/(?P<seminar_id>\d+)/register/$', 'seminar.views.UserBook', name='userbook'),
    url(r'^seminar/add/$', 'seminar.views.addseminar', name='addseminar'),
    url(r'seminar/(?P<pk>[0-9]+)/update/$', SeminarUpdate.as_view(), name='seminar-update'),
    url(r'seminar/(?P<pk>[0-9]+)/delete/$', SeminarDelete.as_view(), name='seminar-delete'),
   	url(r'^category/all/$', 'seminar.views.categories', name='categories'),
   	url(r'^category/(?P<category_id>\d+)/$', 'seminar.views.category', name='category'),
    url(r'^grappelli/', include('grappelli.urls')),
    #url(r'^accounts/affiliate/(?P<username>\w+)/$', 'userprofile.views.AffiliateProfile', name='affiliateprofile'),
    url(r'^accounts/add-information$', 'userprofile.views.addinfo', name='addinfo'),
    url(r'^accounts/(?P<pk>\d+)/edit/$', 'userprofile.views.ProfileEdit', name='editinfo'),
    url(r'^accounts/', include('registration.backends.default.urls')), #redux registration form activation
    url(r'^accounts/(?P<username>[\w.@+-]+)/$', 'userprofile.views.UserProfile' , name='userprofile'),
    url(r'^accounts/(?P<username>[\w.@+-]+)/notifications/$', 'notifications.views.Notify' , name='notifications'),
    url(r'^accounts/affiliate/(?P<username>[\w.@+-]+)/$', 'userprofile.views.AffiliateProfile' , name='affiliateprofile'),

    #url(r'^hello/$', 'seminar.views.hello'),
     # url(r'^blog/', include('blog.urls')),
]

#edw grafoume ta url gia static k media
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


  #UserProfileView.as_view()
