
from django.conf.urls import url, include
from . import views
from test_project.settings import MEDIA_ROOT, DEBUG
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from registration.backends.default import views as registration_views



urlpatterns = [

    url(r'^users/logout/$', auth_views.logout,
     kwargs={'next_page': 'test_list'}, 
    	name='auth_logout'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)