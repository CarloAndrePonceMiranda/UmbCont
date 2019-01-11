from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_confirm, password_reset_complete
from . import views
from .views import (
    UmbrellaList,
    UmbrellaCreation,
    UmbrellaUpdate,
    UmbrellaDelete
)
urlpatterns = [
    url(r'^SmartUmbrellas/',views.SU,name="SU"),
    url(r'^Control/',views.Control,name="control"),
    url(r'^List/Umbrellas/',views.UmbrellaList, name='umbrellalist'),
    url(r'^Umbrella/(?P<pk>[0-9]+)/$',views.UmbrellaDetail,name='umbrelladetail'),
    url(r'^Umbrella/New',views.Umbrella,name="umbrella"),
    url(r'^Edit/(?P<pk>\d+)', login_required(UmbrellaUpdate.as_view()), name='edit'),
    url(r'^Delete/(?P<pk>\d+)', login_required(UmbrellaDelete.as_view()), name='delete'),
    # url(r'^reset/PasswordReset', password_reset, {'template_name':'resetpassword/password_reset_form.html','email_template_name':'resetpassword/password_reset_email.html'},name='password_reset'),
    # url(r'^reset/PassordResetDone', password_reset_done, {'template_name':'resetpassword/password_reset_done.html'},name='password_reset_done'),
    # # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?<token>.+)/$', password_reset_confirm, {'template_name':'resetpassword/password_reset_confirm.html'},name='password_reset_confirm'),
    # url(r'^reset/Done', password_reset_complete, {'template_name':'resetpassword/password_reset_complete.html'},name='password_reset_complete'),
]
