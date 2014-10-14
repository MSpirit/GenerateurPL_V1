import logging
import modules.fonctions
import modules.arguments
import argparse
import sys
from modules import fonctions
from modules.arguments import arguments_generals, arguments_optionnels


#logging.basicConfig(filename ="Journal_log.log", level = logging.DEBUG)
logging.basicConfig(level = logging.DEBUG)
logging.info("Mise en marche du programme")

arguments_generals
arguments_optionnels

# On affiche les arguments obligatoire
modules.arguments.arguments_generals()
modules.arguments.arguments_optionnels()
args = modules.arguments.parser.parse_args()
logging.info(repr(args))
            
fonctions.verification_du_temps(args.dureePlaylist)       
args.genrePlaylist[1] = modules.fonctions.verifier_mes_quantite(args.genrePlaylist[1])
logging.info(repr(args))
#fonctions.gestion_Pourcentage()
            
#print(args)

#fonctions.aVoir()


#modules.arguments.args.genrePlaylist[1] = fonctions.verifier_mes_quantite(modules.arguments.args.genrePlaylist[1])

logging.info('Tout a été opérationel')
logging.info(' *****************FIN************************')
logging.shutdown()
exit(0)