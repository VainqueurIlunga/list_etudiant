from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from ..models import Promotion
from ..forms.promo_forms import promoRegistration
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
def AddNewpromo(request, template_name='app_studentPresent/promotion/add_promotion.html'):
    
    if request.method == 'POST': 
        fm = promoRegistration(request.POST)
        if fm.is_valid():
            lb = fm.cleaned_data['nom_pro']
            fil= fm.cleaned_data['filliere']
            reg = Promotion(libelle = lb, filliere = fil,)
            reg.save()
             
            fm=promoRegistration()
    else:
        fm = promoRegistration()
    promo= Promotion.objects.all()
    return render(request, template_name, {'form':fm,'promo':promo})
# modifier les informations 

def update_data_pro(request,id,template_name='app_studentPresent/promotion/updatepromotion.html'):
    if request.method=='POST':
        pi = Promotion.objects.get(pk=id)
        fm = promoRegistration(request.POST, instance=pi) 
        if fm.is_valid():
            fm.save()
    else:
        pi = Promotion.objects.get(pk=id)   
        fm=promoRegistration(instance=pi)    
    return render (request, template_name,{'form':fm})   


# cette fontion permet de supprimer les informatiosn de la base de données
def delete_data_pro(request,id):
    if request.method == 'POST':
        pi = Promotion.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add_new_pro')
    
    
