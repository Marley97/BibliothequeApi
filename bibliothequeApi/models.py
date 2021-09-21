from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class PAIEMENT(models.IntegerChoices):
    NULL = -1
    LUMICASH = 1
    ECOCASH = 2
    PAYPAL = 3

class Bibliothecaire(models.Model):
	id = models.AutoField(primary_key = True)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	date_naissance = models.DateField(default=datetime.now)
	matricule = models.CharField(max_length=10)

	def __str__(self):
		return self.user.username

class Categorie(models.Model):
    nom = models.CharField(max_length = 50)

    def __str__(self):
        return f" Nom :{self.nom} "

class Livre(models.Model):
	id = models.AutoField(primary_key = True)
	isbn = models.IntegerField()
	titre = models.CharField(max_length=20)  
	couverture = models.ImageField(upload_to = "livres/couverture")
	pdf = models.FileField(upload_to = "livres/pdf")
	annee_publication = models.DateField()
	langue = models.CharField(max_length = 50)
	nombre_exemplaire = models.IntegerField()
	description = models.CharField(max_length=200)
	auteur = models.CharField(max_length=50)
	categorie = models.ForeignKey('Categorie',on_delete = models.CASCADE)
	prix = models.FloatField()

	def __str__(self):
		return f" ISBN : {self.isbn} Titre : {self.titre} Annee_Publication : {self.annee_publication} Nombre_Exemplaire{self.nombre_exemplaire}  "

class Client(models.Model):
	id = models.AutoField(primary_key = True)
	user = models.ForeignKey(User,related_name = "client_user", on_delete = models.CASCADE)
	adresse = models.CharField(max_length = 50)
	telephone = models.CharField(max_length = 50)

	def __str__(self):
		return self.user.username
       
class MesLivre(models.Model):
	id = models.AutoField(primary_key = True)
	client = models.ForeignKey('Client',related_name = "meslivre_user", on_delete = models.CASCADE)
	livres = models.ForeignKey('Livre',on_delete = models.CASCADE)

	def __str__(self):
		return f" client :{self.client} Livres : {self.livres}"
class Panier(models.Model):
	id = models.AutoField(primary_key = True)
	client = models.ForeignKey('Client',related_name = "cart_client", on_delete = models.CASCADE)
	livres = models.ForeignKey('Livre',related_name = "cart_livre",on_delete = models.CASCADE)
	quantite = models.IntegerField()
	prix = models.IntegerField()
	paye = models.BooleanField(default = False)

class Vente(models.Model):
	id = models.AutoField(primary_key = True)
	client = models.ForeignKey('Client', related_name="vente_client", on_delete=models.CASCADE)
	livre = models.ForeignKey(Livre, related_name ="livre_vente", on_delete=models.CASCADE)
	quantite = models.PositiveIntegerField()
	montant = models.FloatField()
	paiement = models.IntegerField(default = -1,choices = PAIEMENT.choices)
	code_transaction = models.PositiveIntegerField()

	def __str__(self):
		return f"{self.user.username} a achete {self.livre.titre} {self.quantite} pour {self.montant}"
		




