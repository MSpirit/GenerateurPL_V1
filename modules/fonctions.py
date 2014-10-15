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
            
def aVoir(arguments):
    for argument in ['titrePlaylist','artistePlaylist','albumPlaylist','genrePlaylist']:
# Si l'argument est renseigné
        if getattr(arguments, argument) is not None:
            # On écrit la valeur de ses ss-arg dans le fichier de logs
            logging.info(' Argument --' + argument + ' :\t' + getattr(arguments, argument)[0][0] + ' ; ' + str(getattr(arguments, argument)[0][1]) + ' \t ' + getattr(arguments,argument)[1][0] + ' ; ' + str(getattr(arguments,argument)[1][1]) + '.')
