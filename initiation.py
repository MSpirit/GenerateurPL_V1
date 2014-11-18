import logging
import modules.arguments
import modules.fonctions
from database.recuperationdonnees import *


logging.basicConfig(filename ="Journal_log.log", level = logging.DEBUG)
#logging.basicConfig(level = logging.DEBUG)
logging.info("Mise en marche du programme")

# On affiche les arguments obligatoire
modules.arguments.arguments_generals()
modules.arguments.arguments_optionnels()
args = modules.arguments.parser.parse_args()
logging.info(repr(args))
            
#Vérification du temps
modules.fonctions.verification_du_temps(args.dureePlaylist)
args.genrePlaylist[0][1] = modules.fonctions.verifier_mes_quantite(args.genrePlaylist[0][1])

#Affiche dans le fichier de logs les arguments
logging.info(repr(args))

modules.fonctions.aVoir(args)

recupererDonnees(args)
print("Récupération de votre musique")
logging.info("Récupération des données musicales")

generationPlaylist(args)
print("generation de votre musique")
logging.info("Génération de la playlist")


Playlist(args)
print("Playlist en phase de création")

EcritureFichier(args, musiquePL)
print("Ecriture de votre playlist")
logging.info("Ecriture de la playlist dans le fichier demandé préalablement par l'utilisateur")



print("Bonne lecture de votre playlist")
logging.info('Tout a été opérationel')
logging.info('*****************FIN************************')
logging.shutdown()
exit(0)