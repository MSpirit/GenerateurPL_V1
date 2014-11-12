import sqlalchemy
import random
from database.Basedonnees_initiation import table_morceaux, connection as conn
from creationfichier.fichier import writeM3U, writeXSPF

argument_cli = ['titrePlaylist','artistePlaylist','albumPlaylist','genrePlaylist']
musiquePL =[]


def recupererDonnees(args):
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
                duree = 0
                for ligne in recuperation:
                    duree += ligne[5]
                    if(duree < argument[1]*60):
                        argument[2].insert(i, ligne)
                        i += 1
                    else:
                        duree -= ligne[5]
                          

#Génération de la liste de playlist
def generationPlaylist(args):
    i = 0
    for attribut in argument_cli:
        if getattr(args, attribut) is not None:
            for argument in getattr(args, attribut):
                for musique in argument[2]:
                    musiquePL.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
                    i += 1
    random.shuffle(musiquePL)
        
def Playlist(args):
    duree = 0
    for musique in musiquePL:
        duree += musique[3]
        
    if(duree < args.dureePlaylist*60):
        select_morceaux = sqlalchemy.select([table_morceaux])
        resultat = conn.execute(select_morceaux)
        resultat = list(resultat)
        random.shuffle(resultat)
    
    i=len(musiquePL)
    for musique in resultat:
        duree += musique[5]
        if(duree < args.dureePlaylist*60):
            musiquePL.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
            i += 1
        else:
            duree -= musique[5]
    
def EcritureFichier(args, musiquePL):
    if(args.formatPlaylist == 'm3u'):
        writeM3U(args, musiquePL)
    if(args.formatPlaylist == 'xspf'):
        writeXSPF(args, musiquePL)
