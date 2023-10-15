from django.db import models

# Create your models here.
class Faculte(models.Model):
    libelle = models.CharField(max_length=25)
    
class Filliere(models.Model):
    libelle = models.CharField(max_length=25)
    faculte= models.ForeignKey(Faculte, on_delete= models.CASCADE)

class Promotion(models.Model):
    libelle= models.CharField(max_length=15)
    filliere = models.ForeignKey(Filliere, on_delete=models.CASCADE)
    
class Etudiant(models.Model):
    nom= models.CharField(max_length=45)
    postnom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    promo = models.ForeignKey(Promotion, on_delete=models.CASCADE)

class Enseignant(models.Model):
    name= models.CharField(max_length=45)
    
class Courses(models.Model):
    title = models.CharField(max_length=45)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    promo = models.ForeignKey(Promotion, on_delete=models.CASCADE)


    
class Participation(models.Model):
    date= models.DateTimeField(auto_now_add=True)
    etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Courses, on_delete=models.CASCADE)
    