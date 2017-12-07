
from django.conf.urls import url,include
from django.contrib import admin
from file import views as myapp_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$',myapp_views.home,name='home'),
    url(r'^form/$',myapp_views.form,name='form'),


    url(r'^admin/', include(admin.site.urls)),

]


