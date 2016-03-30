from django.http import HttpResponse
from django.views.generic import View
from django.http import HttpResponseRedirect
from forms import LoginForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def home_by_function(request):
    print dir(request)
    print "Host: ", request.get_host()
    print "Port: ", request.get_port()
    print "User: ", request.user
    return HttpResponse("Home function...............")


class IndexClass(View):

    def get(self, request):
        return HttpResponse("Index get function.......")


class LoginClass(View):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("login success")
                else:
                    return HttpResponse("user not active")
            else:
                return HttpResponse("login failed")
        return render(request, self.template_name, {'form': form})
