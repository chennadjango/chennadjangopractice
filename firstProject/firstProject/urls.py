from django.conf.urls import include, url
from django.contrib import admin
from firstAPP import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'firstProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'greetings/',views.display),
]
