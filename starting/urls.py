
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
#from . import views
from rest_insurance.rest_api.views import trendchart
from rest_insurance.views import blog_list, home,homepage
from rest_insurance.rest_api.views import trendchart1,trendchart2,trendchart3,trendchart4,trendchart5
urlpatterns = [
    url(r'login/',include('insurance.urls')),
    url(r'admin/',admin.site.urls),
    #url(r'^home/', views.home,name="home"),
    url(r'^$', blog_list),
    url(r'^vital/', trendchart.as_view()),
    url(r'^vital2/', trendchart1.as_view()),
    url(r'^vital3/', trendchart2.as_view()),
    url(r'^chronic/', trendchart3.as_view()),
    url(r'^chronic2/', trendchart4.as_view()),
    url(r'^chronic3', trendchart5.as_view()),
    url(r'^loginpage/', include('rest_insurance.urls')),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
