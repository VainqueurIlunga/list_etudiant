from django.db import models

# Create your models here.
class Faculte(models.Model):
    nom_fac = models.CharField(max_length=25)
    def __str__(self):
        return self.nom_fac
    
class Filliere(models.Model):
    nom_fil = models.CharField(max_length=25)
    fac = models.ForeignKey(Faculte, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.nom_fil}/{self.fac}"
class Promotion(models.Model):
    nom_pro = models.CharField(max_length=15)
    fil = models.ForeignKey(Filliere, on_delete=models.CASCADE)
    
    def __str__(self) :
        return f"{self.nom_pro}/{self.fil}"
class Etudiant(models.Model):
    nom= models.CharField(max_length=45)
    postnom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    promo = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom}/{self.postnom}/{self.prenom}/{self.promo}"
    
class Enseignant(models.Model):
    name= models.CharField(max_length=45)
    fistname=models.CharField(max_length=45, null=True)
    lastname=models.CharField(max_length=45, null=True)
    adresse = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return f"{self.name}/{self.fistname}/{self.lastname}/{self.adresse}"
    
class Courses(models.Model):
    title = models.CharField(max_length=45)
    promo = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} /{self.enseignant} / {self.promo}"


    
class Participation(models.Model):
    date= models.DateTimeField(auto_now_add=True)
    etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Courses, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.etudiant} /{self.etudiant.promo} / {self.cours}/{self.date}"
    