from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from ..models import Courses
from ..forms.cours_forms import coursRegistration

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
def AddNewCourses(request, template_name='app_studentPresent/cours/add_cours.html'):
    if request.method == 'POST':
        fm = coursRegistration(request.POST)
        if fm.is_valid():
            titl = fm.cleaned_data['title']
            ensei = fm.cleaned_data['enseignant']
            prmo = fm.cleaned_data['promo']
            reg = Courses(title=titl, enseignant=ensei, promo=prmo)
            reg.save()
            fm = coursRegistration()
    else:
        fm = coursRegistration()
    courses = Courses.objects.all()
    return render(request, template_name, {'form': fm, 'cours': courses})


# modifier les informations

def update_data_cr(request, id, template_name='app_studentPresent/cours/updatecours.html'):
    if request.method == 'POST':
        pi = Courses.objects.get(pk=id)
        fm = coursRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Courses.objects.get(pk=id)
        fm = coursRegistration(instance=pi)
    return render(request, template_name, {'form': fm})


# cette fontion permet de supprimer les informatiosn de la base de données
def delete_data_cr(request, id):
    if request.method == 'POST':
        pi = Courses.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add_new_cr')


