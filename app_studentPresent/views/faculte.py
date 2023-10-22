from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from ..models import Faculte
from ..forms.faculte_forms import faculteRegistration
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
def addNewfac(request, template_name='app_studentPresent/faculte/add_faculte.html'):
    
    if request.method == 'POST': 
        fm = faculteRegistration(request.POST)
        if fm.is_valid():
            lbl = fm.cleaned_data['libelle']
            reg = Faculte(libelle = lbl)
            reg.save()
             
            fm=faculteRegistration()
    else:
        fm = faculteRegistration()
    faculte= Faculte.objects.all()
    return render(request, template_name, {'form':fm,'facul':faculte})
# modifier les informations 

def update_data_fac(request,id,template_name='app_studentPresent/faculte/updatefac.html'):
    if request.method=='POST':
        pi = Faculte.objects.get(pk=id)
        fm = faculteRegistration(request.POST, instance=pi) 
        if fm.is_valid():
            fm.save()
    else:
        pi = Faculte.objects.get(pk=id)   
        fm=faculteRegistration(instance=pi)    
    return render (request, template_name,{'form':fm})   


# cette fontion permet de supprimer les informatiosn de la base de données
def delete_data_fac(request,id):
    if request.method == 'POST':
        pi = Faculte.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add_new_fac')
    
    