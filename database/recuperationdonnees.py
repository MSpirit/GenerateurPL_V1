import sqlalchemy
import random
from database.Basedonnees_initiation import *
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


            
def EcritureFichier(args, playlist):
    if(args.type_playlist == 'm3u'):
        writeM3U(args, playlist)
 
