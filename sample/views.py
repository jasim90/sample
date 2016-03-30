from django.shortcuts import render
from django.views.generic import View
from forms import PersonForm, UploadForm
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from models import Upload
# Create your views here.


class PersonView(View):
    form_class = PersonForm
    template_name = 'person_template.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('person/')
        return render(request, self.template_name, {'form': form})


class UploadView(ListView):
    form_class = UploadForm
    template_name = 'file_upload.html'
    model = Upload
    paginate_by = 1

    # def get(self, request):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        form = self.form_class()
        context = super(UploadView, self).get_context_data(**kwargs)
        context['form'] = form
        return context

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('upload/')
        return render(request, self.template_name, {'form': form})
