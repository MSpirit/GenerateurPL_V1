import argparse
import logging
parser = argparse.ArgumentParser()

parser.add_argument("dureePlaylist", type = int, help="duree de la playlist en minutes")
parser.add_argument("formatPlaylist", choices = ["m3u","xspf","pls"], help="format de sortie de la playlist")
parser.add_argument("nomFichierPlaylist", help="nom du fichier de sortie")


parser.add_argument("--titrePlaylist", help="titre choisis")
parser.add_argument("--artistePlaylist", help="nom de l'artiste")
parser.add_argument("--albumPlaylist", help="album présent dans la playlist")
parser.add_argument("--genrePlaylist", help="genre%pourcentage", nargs=2)

args = parser.parse_args()

def verifier_mes_quantité(quantite):
    return int(quantite)



try:
    args.genrePlaylist[1] = verifier_mes_quantité(args.genrePlaylist[1])
    print(args)
except ValueError:
    print ("Erreur lors de la conversion !")



if args.genrePlaylist[1] > 0 and args.genrePlaylist[1] <= 100:
    print ("ok")
else:
    print("Veuillez saisir un nombre entre 0 et 100")

