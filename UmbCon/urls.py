"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_confirm, password_reset_complete




from .views import home_page, contact_page, about_page, login_page, register_page, lista_de_usuarios, AuthDetail,AuthDelete,AuthUpdate

urlpatterns = [
    ########################   urls marco   ########################
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page,name='home'),
    url(r'^contact/$', contact_page,name='contacto'),
    url(r'^about/$', about_page,name='about'),
    url(r'^login/$', login_page,name='login'),
    url(r'^user_list/$', lista_de_usuarios,name='users'),
    url(r'^register/$', register_page,name='register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^borrar/(?P<pk>\d+)', AuthDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)', AuthDetail.as_view(), name='detail'),
    url(r'^editar/(?P<pk>\d+)', AuthUpdate.as_view(), name='edit'),
    url(r'^reset/PasswordReset', password_reset, {'template_name':'resetpassword/password_reset_form.html','email_template_name':'resetpassword/password_reset_email.html'},name='password_reset'),
    url(r'^reset/PassordResetDone', password_reset_done, {'template_name':'resetpassword/password_reset_done.html'},name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name':'resetpassword/password_reset_confirm.html'},name='password_reset_confirm'),
    url(r'^reset/Done', password_reset_complete, {'template_name':'resetpassword/password_reset_complete.html'},name='password_reset_complete'),
    ########################   urls marco   ########################
    url(r'^', include('control.urls', namespace='umbrellas')),
    ########################   urls clientes   ########################
    #url(r'^', include('clientes.urls', namespace='clientes')),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
