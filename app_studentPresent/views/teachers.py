from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from ..models import Enseignant
from ..forms.teacher_forms import teacherRegistration
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
def AddNewTeacher(request, template_name='app_studentPresent/enseignant/add_enseignant.html'):
    
    if request.method == 'POST': 
        fm = teacherRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            fn = fm.cleaned_data['fistname']
            ln = fm.cleaned_data['lastname']
            ad = fm.cleaned_data['adresse']
            reg = Enseignant(name = nm, fistname = fn, lastname = ln, adresse = ad)
            reg.save()
            fm=teacherRegistration()
    else:
        fm = teacherRegistration()
    ensei= Enseignant.objects.all()
    return render(request, template_name, {'form':fm,'ensei':ensei})
# modifier les informations 

def update_data_en(request,id,template_name='app_studentPresent/enseignant/updateenseignant.html'):
    if request.method=='POST':
        pi = Enseignant.objects.get(pk=id)
        fm = teacherRegistration(request.POST, instance=pi) 
        if fm.is_valid():
            fm.save()
    else:
        pi = Enseignant.objects.get(pk=id)
        fm=teacherRegistration(instance=pi)    
    return render (request, template_name,{'form':fm})   


# cette fontion permet de supprimer les informatiosn de la base de données
def delete_data_en(request,id):
    if request.method == 'POST':
        pi = Enseignant.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add_new_en')
