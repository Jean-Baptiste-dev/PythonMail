import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('votre_adresse_mail@gmail.com', 'Votre_mot_de_passe')

def Continue():
    print("Voulez-vous envoyer un autre mail ? Oui ou Non")
    reponse: str = input()
    if reponse == 'Oui':
        mailtosend()
    elif reponse =='Non':
        print("Vous avez quitté le système :(")
        exit()

def mailtosend():
    email_sender = input("Entrez le mail d'envoi s'il vous plaît: ")
    print("vous avez entrer : " + email_sender)
    email_receiver = input("Entrez le mail de recuperation s'il vous plaît : ")
    print("Vous venez d'entrer : " + email_receiver)
    objet = input("Entrez l'objet du mail s'il vous plaît : ")
    print("Vous venez d'entrer : " + objet)
    content = input("Entrez votre contenu s'il vous plait: ")
    print("Voici votre message : " + content)
    print("Voulez-vous envoyer le mail ? Y si Oui et X si Non")
    envoi: str = input()
    if envoi == 'Y':
        server.sendmail(email_sender, email_receiver, content)
        Continue()
    elif envoi == 'X':
        print("Vous avez refusé l'envoi du mail")
    else:
        print("Erreur, desolé on ne reconnais pas ce que vous entrez...")


if __name__ == '__main__':
    print("SYSTEME D'ENVOI DE MAIL :")
    print("   Menu du Système  ")
    print("A- Je veux envoyer un mail  ")
    print("B-Je veux quitter le système")
    print("Quel est votre choix ?")
    choix: str = input()
    while choix:
        if choix == 'A':
            mailtosend()
        elif choix == 'B':
            print("Au revoir..")
            exit()
        else:
            print("Désole, choix introuvable")















