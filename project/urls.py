from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'app.views.login_view'),
    url(r'^signup/$', 'app.views.sign_up'),
    url(r'^logout/$', 'app.views.logout_view'),
    url(r'^gym_register/(?P<pk>\d+)/$', 'app.views.gym_register'),
    url(r'^video_of_the_day/', 'app.views.video_of_the_day'),
    url(r'^male_gyms/', 'app.views.male_gyms'),
    url(r'^female_gyms/', 'app.views.female_gyms'),
    url(r'^mixed_gyms/', 'app.views.mixed_gyms'),
    url(r'^homepage/$', 'app.views.homepage'),
    url(r'^index/$', 'app.views.index'),
    url(r'^about/$', 'app.views.about'),
    url(r'^blog/$', 'app.views.blog'),
    url(r'^contact/$', 'app.views.contact'),
    url(r'^edit_gym/(?P<pk>\d+)/$', 'app.views.edit_gym', name='edit_gym'),
    url(r'^delete_gym/(?P<pk>\d+)/$', 'app.views.delete_gym'),
    url(r'^create_gym/', 'app.views.create_gym'),
    url(r'^list_all_gyms/', 'app.views.list_all_gyms'),
    url(r'^list_users_for_gym/(?P<pk>\d+)/$', 'app.views.list_users_for_gym'),
    url(r'^gym_details/(?P<pk>\d+)/$', 'app.views.gym_details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)