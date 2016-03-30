from django.conf.urls import url
from views import PersonView, UploadView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^person/', PersonView.as_view()),
    url(r'^upload/', login_required(UploadView.as_view()))
]
