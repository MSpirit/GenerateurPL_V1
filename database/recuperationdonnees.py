import sqlalchemy
import random
from database.Basedonnees_initiation import table_morceaux, connection as conn
from creationfichier.fichier import writeM3U

argument_cli = ['titrePlaylist','artistePlaylist','albumPlaylist','genrePlaylist']
playlist =[]


def recupererDonnees(args):
    global recuperation
    for attribut in argument_cli:
        if getattr(args, attribut) is not None:
            for argument in getattr(args, attribut):
                if (attribut == 'titrePlaylist'):
                    RecuperationDonnees = sqlalchemy.select([table_morceaux]).where(table_morceaux.c.titre == argument[0])
                if (attribut == 'artistePlaylist'):
                    RecuperationDonnees = sqlalchemy.select([table_morceaux]).where(table_morceaux.c.artiste == argument[0])
                if (attribut == 'albumPlaylist'):
                    RecuperationDonnees = sqlalchemy.select([table_morceaux]).where(table_morceaux.c.album == argument[0])
                if (attribut== 'genrePlaylist'):
                    RecuperationDonnees = sqlalchemy.select([table_morceaux]).where(table_morceaux.c.genre == argument[0])

                recuperation = conn.execute(RecuperationDonnees)
                recuperation = list(recuperation)
                random.shuffle(recuperation)

                argument.insert(2,[])
                i=0
                somme_duree = 0
                for ligne in recuperation:
                    somme_duree += ligne[5]
                    if(somme_duree < argument[1]*60):
                        argument[2].insert(i, ligne)
                        i += 1
                    else:
                        somme_duree -= ligne[5]


            
def EcritureFichier(args, playlist):
    if(args.formatPlaylist == 'm3u'):
        writeM3U(args, playlist)
 
