import argparse


parser = argparse.ArgumentParser()


def arguments_generals():
    parser.add_argument("dureePlaylist", type = int, help="duree de la playlist en minutes")
    parser.add_argument("formatPlaylist", choices = ["m3u","xspf","pls"], help="format de sortie de la playlist")
    parser.add_argument("nomFichierPlaylist", help="nom du fichier de sortie")

def arguments_optionnels():
    parser.add_argument("-t", "--titrePlaylist", help="titre choisis")
    parser.add_argument("-ar", "--artistePlaylist", help="nom de l'artiste")
    parser.add_argument("-al", "--albumPlaylist", help="album présent dans la playlist")
    parser.add_argument("-g", "--genrePlaylist", action='append', help="genre%%pourcentage", nargs=2)
