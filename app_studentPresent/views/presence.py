from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from ..models import Participation
from ..forms.presence_forms import presenceRegistration

# Create your views here.
"""class AddNewStudent(TemplateView):
    template_name='app_studentPresent/add_participation.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm= Etudiant()
        etud = Etudiant.objects.all()
        context = {'et':etud, 'form':fm }
        return context 
"""


# cette fonction permet d'ajoputer et d'afficher les information
def AddNewPresence(request, template_name='app_studentPresent/presence/add_presence.html'):
    if request.method == 'POST':
        fm = presenceRegistration(request.POST)
        if fm.is_valid():
            etud = fm.cleaned_data['etudiant']
            crs = fm.cleaned_data['cours']
            reg = Participation(etudiant=etud, cours=crs)
            reg.save()


            fm = presenceRegistration()
    else:
        fm = presenceRegistration()
    presence = Participation.objects.all()
    return render(request, template_name, {'form': fm, 'present': presence})


# modifier les informations

def update_data_pre(request, id, template_name='app_studentPresent/presence/updatepresence.html'):
    if request.method == 'POST':
        pi = Participation.objects.get(pk=id)
        fm = presenceRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Participation.objects.get(pk=id)
        fm = presenceRegistration(instance=pi)
    return render(request, template_name, {'form': fm})


# cette fontion permet de supprimer les informatiosn de la base de données
def delete_data_pre(request, id):
    if request.method == 'POST':
        pi = Participation.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add_new_pre')

