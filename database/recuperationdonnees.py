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



def generationPlaylist(args):
    i = 0
    for attribut in argument_cli:
        if getattr(args, attribut) is not None:
            for argument in getattr(args, attribut):
                for champ_musique in argument[0]:
                    playlist.insert(i, [champ_musique[0], champ_musique[2], champ_musique[1], champ_musique[5]])
                    i += 1
    random.shuffle(playlist)
    completePlaylist(args)
    
    
def completePlaylist(args):
    somme_duree = 0
    for champ_musique in playlist:
        somme_duree += champ_musique[5]
        
    if(somme_duree < args.dureePlayslist*60):
        selection_morceaux = sqlalchemy.select([table_morceaux])
        resultat = conn.execute(selection_morceaux)
        resultat = list(resultat)
        random.shuffle(resultat)
    
    i=len(playlist)
    for champ_musique in resultat:
        somme_duree += champ_musique[5]
        if(somme_duree < args.dureePlayslist*60):
            playlist.insert(i, [champ_musique[0], champ_musique[2], champ_musique[1], champ_musique[5]])
            i += 1
        else:
            somme_duree -= champ_musique[5]
            
def writeFile(args, playlist):
    if(args.type_playlist == 'm3u'):
        writeM3U(args, playlist)
 
