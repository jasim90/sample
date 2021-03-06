"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
import views
from django.conf.urls.static import static
from django.conf import settings
# from views import IndexClass

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home_by_function),
    url(r'^index/', views.IndexClass.as_view()),
    url(r'^sample/', include('sample.urls')),
    url(r'^login/', views.LoginClass.as_view())
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
