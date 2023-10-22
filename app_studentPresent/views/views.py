from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from ..models import Etudiant
from ..forms.forms import studentRegistration
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
def AddNewStudent(request, template_name='app_studentPresent/student/add_participation.html'):
    
    if request.method == 'POST': 
        fm = studentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['nom']
            pstnom = fm.cleaned_data['postnom']
            prnom = fm.cleaned_data['prenom']
            prmo = fm.cleaned_data['promo']
            reg = Etudiant(nom = nm, postnom = pstnom, prenom = prnom, promo = prmo)
            reg.save()
             
            fm=studentRegistration()
    else:
        fm = studentRegistration()
    etudiant= Etudiant.objects.all()
    return render(request, template_name, {'form':fm,'etud':etudiant})
# modifier les informations 

def update_data(request,id,template_name='app_studentPresent/student/updateStudent.html'):
    if request.method=='POST':
        pi = Etudiant.objects.get(pk=id)
        fm = studentRegistration(request.POST, instance=pi) 
        if fm.is_valid():
            fm.save()
    else:
        pi = Etudiant.objects.get(pk=id)   
        fm=studentRegistration(instance=pi)    
    return render (request, template_name,{'form':fm})   


# cette fontion permet de supprimer les informatiosn de la base de données
def delete_data(request,id):
    if request.method == 'POST':
        pi = Etudiant.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add_new')
    
    
class ShowNewStudent(TemplateView):
    template_name='app_studentPresent/show_studentPresnet.html' 