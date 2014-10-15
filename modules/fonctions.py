import logging

#Vérification d'un temps positif'''
def verification_du_temps(argumentAVerifier):
    logging.info("Utilisation de la fonction pour vérifier que le temps est un entier positif")
    if argumentAVerifier < 0 :
        print ("Le temps doit être positif !")
        logging.error("le temps " + str(argumentAVerifier) + " n'est pas un entier positif")
        exit(1)
    
def verifier_mes_quantite(quantite):
    try:
        logging.info("Mise en marche de la fonction des vérification des quantités")
        quantiteValidee = abs(int(quantite))       
        if quantiteValidee > 100:
            return None
        return quantiteValidee
    except ValueError:
        logging.error("La valeur saisie pour la quantité n'est pas une valeur numérique : '" + quantite +"'")
        return None
            
def gestionPourcentage(typeArg):
    logging.info("Mise en marche de la fonction des vérification des pourcentages")
    i = 0
    ligneListe = 1
    j = 0
    ligneListe2 = 1
    somme = 0
    
    #Tant que la liste du type d'argument passé à encore une ligne
    
    while ligneListe <= len(typeArg):
        logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
        
        #Vérification du %
        quantite = verifier_mes_quantite(typeArg[i][1])
        logging.info("La quantite pour le genre est " + str(quantite) + ".")
        somme = somme + quantite
        ligneListe = ligneListe + 1
        i = i + 1
    logging.info("La sommes totale des genres est de : " + str(somme) +".")
    if somme > 100:        
        #Tant que la liste du type d'argument passé à encore une ligne
        logging.info('Remise du total des % à 100 grace à la proportionalité')
        while ligneListe2 <= len(typeArg):
            '''Round() permet d'arrondir à l'entier le plus proche'''
            typeArg[j][1] = round(int(typeArg[j][1])*100/somme)
            logging.info(str(typeArg[j][1]) + "% de genres voulues 1> 1er genre 2> 2 genre")
            j = j + 1
            ligneListe2 = ligneListe2 + 1          
            
            
def aVoir(arguments):
    for argument in ['titrePlaylist','artistePlaylist','albumPlaylist','genrePlaylist']:
# Si l'argument est renseigné
        if getattr(arguments, argument) is not None:
            # On écrit la valeur de ses ss-arg dans le fichier de logs
            logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
            gestionPourcentage(getattr(arguments, argument))