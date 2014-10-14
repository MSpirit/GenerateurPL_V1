import logging
import modules.arguments

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
        logging.error("La valeur saisie pour la quantité n'est pas une valeur numérique : '" + quantite + "'")
        return None
        
# def gestion_Pourcentage(typeArg):
#     logging.info("Mise en marche de la fonction des vérification des pourcentages")
#     i = 0
#     ligneList = 1
#     j = 0
#     ligneList2 = 1
#     somme = 0
# 
#     '''Tant que la liste du type d'argument passé à encore une ligne'''
#     while ligneList <= len(typeArg):
#         logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
#         '''Vérification du %'''
#         verifier_mes_quantite(typeArg[i][1])
#         print (genre)
#         somme = somme + genre
#         ligneList = ligneList + 1
#         i = i + 1
#     logging.info('Total des sommes des %: ' + str(somme))
#     print (somme)
#     if somme > 100:
#         '''Tant que la liste du type d'argument passé à encore une ligne'''
#         logging.info('Remise du total des % à 100 grace à la proportionalité')
#         while ligneList2 <= len(modules.arguments.args.genrePlaylist):
#             '''Round() permet d'arrondir à l'entier le plus proche'''
#             typeArg[j][1] = round(int(typeArg[j][1])*100/somme)
#             print(typeArg[j][1])
#             j = j + 1
#             ligneList2 = ligneList2 + 1
            
def aVoir():
    for argument in ['titrePlaylist','artistePlaylist','albumPlaylist','genrePlaylist']:
# Si l'argument est renseigné
        if getattr(modules.arguments.args, argument) is not None:
            # On écrit la valeur de ses ss-arg dans le fichier de logs
            logging.info(' Argument --' + argument + ' :\t' + getattr(modules.arguments.args, argument)[0] + ' ; ' + str(getattr(modules.arguments.args, argument)[1]))
