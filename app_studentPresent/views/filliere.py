from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from ..models import Filliere
from ..forms.filliere_forms import fillierRegistration
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
def addNewfil(request, template_name='app_studentPresent/filliere/add_filliere.html'):
    
    if request.method == 'POST': 
        fm = fillierRegistration(request.POST)
        if fm.is_valid():
            lbl = fm.cleaned_data['libelle']
            fc= fm.cleaned_data['faculte']
            reg = Filliere(libelle = lbl, faculte = fc)
            reg.save()
             
            fm=fillierRegistration()
    else:
        fm = fillierRegistration()
    filliere= Filliere.objects.all()
    return render(request, template_name, {'form':fm,'fill':filliere})

# modifier les informations 

def update_data_fil(request,id,template_name='app_studentPresent/filliere/updatefil.html'):
    if request.method=='POST':
        pi = Filliere.objects.get(pk=id)
        fm = fillierRegistration(request.POST, instance=pi) 
        if fm.is_valid():
            fm.save()
    else:
        pi = Filliere.objects.get(pk=id)   
        fm=fillierRegistration(instance=pi)    
    return render (request, template_name,{'form':fm})   


# cette fontion permet de supprimer les informatiosn de la base de données
def delete_data_fil(request,id):
    if request.method == 'POST':
        pi = Filliere.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add_new_fil')
    
    
