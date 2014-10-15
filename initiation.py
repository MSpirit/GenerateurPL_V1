import logging
import modules.arguments
import modules.fonctions


logging.basicConfig(filename ="Journal_log.log", level = logging.DEBUG)
#logging.basicConfig(level = logging.DEBUG)
logging.info("Mise en marche du programme")

# On affiche les arguments obligatoire
modules.arguments.arguments_generals()
modules.arguments.arguments_optionnels()
args = modules.arguments.parser.parse_args()
logging.info(repr(args))
            
modules.fonctions.verification_du_temps(args.dureePlaylist)
args.genrePlaylist[0][1] = modules.fonctions.verifier_mes_quantite(args.genrePlaylist[0][1])





logging.info(repr(args))

modules.fonctions.aVoir(args)


#modules.arguments.args.genrePlaylist[1] = fonctions.verifier_mes_quantite(modules.arguments.args.genrePlaylist[1])

print("Bonne lecture de votre playlist")
logging.info('Tout a été opérationel')
logging.info('*****************FIN************************')
logging.shutdown()
exit(0)