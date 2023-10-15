from django.contrib import admin
from .models import Etudiant, Participation, Courses, Faculte, Promotion, Filliere, Enseignant
# Register your models here.
@admin.register(Faculte)
class FacAdmin(admin.ModelAdmin):
    list_display = ('id', 'libelle',)

@admin.register(Filliere)
class FilAdmin(admin.ModelAdmin):
    list_display = ('id', 'libelle','faculte')


@admin.register(Promotion)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('id','libelle', 'filliere',)

@admin.register(Enseignant)
class EnseiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Etudiant,)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom','postnom','prenom','promo')

@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date','etudiant','cours',)
    

