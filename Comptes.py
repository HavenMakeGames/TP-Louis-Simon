import sqlite3

mail_utilises = []
nom_utilises = []

def verifier_mail(mail):
    if mail in mail_utilises:
        print("Votre Mail est déjà associé à un comptre")
        return False
    elif "@" in mail:
        if ".com" in mail :
            return True
    print("Veuillez entrer un Mail valide")


def verifier_nom(nom):
    if nom in nom_utilises:
        return False
    return True

def creer_compte():
    mailBon = False
    while mailBon == False:
        print("Inserez votre Mail")
        mail = input("")
        if(verifier_mail(mail) == True):
            mailBon = True
        else:
            ("Votre Email est déjà associé à un Compte")
    mdp =""
    print("Inserez votre Mot de Passe")
    mdp = input("")
    print("")
    verifBon = False
    while verifBon == False:
        print("Inserez le Mot de Passe à Nouveau")
        verifmdp = input("")
        if verifmdp == mdp:
            verifBon = True
        else:
            print("Veuillez entrer le bon Mot de Passe")
    nom =""
    nomBon = False
    while nomBon == False:
        print("")
        nom = input("Inserez votre Nom d'utilisateur")
        if (verifier_nom(nom)):
            nomBon = True
        else: 
            print("Votre Nom d'utilisateur est déjà utilisé")
    
    
    
class Comptes:
    def __init__(self, nom , mail, mdp):
        self.Nom_user = nom
        self.Mail = mail 
        self.Password = mdp


creer_compte()