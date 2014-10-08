import logging
import argparse
import sys

logging.basicConfig(filename ="Journal_log.log", level = logging.DEBUG)
logging.info("Mise en marche du programme")

parser = argparse.ArgumentParser()

parser.add_argument("dureePlaylist", type = int, help="duree de la playlist en minutes")
parser.add_argument("formatPlaylist", choices = ["m3u","xspf","pls"], help="format de sortie de la playlist")
parser.add_argument("nomFichierPlaylist", help="nom du fichier de sortie")


parser.add_argument("-t", "--titrePlaylist", help="titre choisis")
parser.add_argument("-ar", "--artistePlaylist", help="nom de l'artiste")
parser.add_argument("-al", "--albumPlaylist", help="album présent dans la playlist")
parser.add_argument("-g", "--genrePlaylist", help="genre%pourcentage", nargs=2)

args = parser.parse_args()

# On affiche les arguments obligatoire
logging.info(args.dureePlaylist)
logging.info(args.formatPlaylist)
logging.info(args.nomFichierPlaylist)

#Vérification d'un temps positif'''
logging.info("Utilisation de la fonction pour vérifier que le temps est un entier positif")
if args.dureePlaylist < 0 :
    print ("Le temps doit être positive !")
    logging.error("le temps " + str(args.dureePlaylist) + " n'est pas un entier positif")
    exit(1)
    
def verifier_mes_quantite(quantite):
    try:
        global genre
        logging.info("Mise en marche de la fonction des vérification des quantités")
        genre = abs(int(quantite))
        if genre < 0:
            genre = abs(genre)
            logging.warning('La quantité saisie doit etre positive')
            logging.info('Nombre négatif transformé en positif: ' + str(genre))
            
        elif genre > 100:
            
            genre = None
            logging.warning('La quantité saisie est supérieur à 100')
            logging.info('Nombre supérieur à 100 transformé en : ' + str(genre))
            return True
            return genre
    except ValueError:
        logging.error("La valeur saisie pour la quantité n'est pas une valeur numérique : '" + quantite + "'")
        exit(1)
        
def gestionPctage(typeArg):
    logging.info("Mise en marche de la fonction des vérification des pourcentages")
    i = 0
    ligneList = 1
    j = 0
    ligneList2 = 1
    somme = 0

    '''Tant que la liste du type d'argument passé à encore une ligne'''
    while ligneList <= len(typeArg):
        logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
        '''Vérification du %'''
        verifier_mes_quantite(typeArg[i][1])
        print (genre)
        somme = somme + genre
        ligneList = ligneList + 1
        i = i + 1
    logging.info('Total des sommes des %: ' + str(somme))
    print (somme)
    if somme > 100:
        '''Tant que la liste du type d'argument passé à encore une ligne'''
        logging.info('Remise du total des % à 100 grace à la proportionalité')
        while ligneList2 <= len(args.genrePlaylist):
            '''Round() permet d'arrondir à l'entier le plus proche'''
            typeArg[j][1] = round(int(typeArg[j][1])*100/somme)
            print(typeArg[j][1])
            j = j + 1
            ligneList2 = ligneList2 + 1

          
            
#print(args)

for argument in ['titrePlaylist','artistePlaylist','albumPlaylist','genrePlaylist']:
# Si l'argument est renseigné
    if getattr(args, argument) is not None:
        # On écrit la valeur de ses ss-arg dans le fichier de logs
        logging.info(' Argument --' + argument + ' :\t' + getattr(args, argument)[0] + ' ; ' + str(getattr(args, argument)[1]))



args.genrePlaylist[1] = verifier_mes_quantite(args.genrePlaylist[1])

logging.info('Tout a été opérationel')
logging.info(' *****************************************')
logging.shutdown()
exit(0)