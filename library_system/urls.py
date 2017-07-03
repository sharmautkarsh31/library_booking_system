from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from soft_lib.api import Issue

router= routers.DefaultRouter()
router.register(r'books',Issue)

urlpatterns = (
    # Examples:
    # url(r'^$', 'library_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),

)
