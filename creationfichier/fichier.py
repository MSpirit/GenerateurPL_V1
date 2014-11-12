#from database.recuperationdonnees import musiquePL


def writeM3U(args, musiquePL):
    fichier = args.nomFichierPlaylist +"."+ args.formatPlaylist
    fichier = open(fichier, 'w')
    for champ_musique in musiquePL:
        fichier.write(champ_musique[4] + "\n")
    fichier.close()
    
def writeXSPF(args, musiquePL):
    fichier = (args.nomFichierPlaylist + "." + args.formatPlaylist)
    fichier = open(fichier, 'w')
    fichier.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+
                       "<playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\">\n"+
                       "\t<title>"+ fichier +"</title>\n"+
                       "\t<trackList>\n")
    #Parcours le résultat pour chaque ligne
    for champ_musique in musiquePL:
            fichier.write("\t\t<track>\n\t\t\t<location>file://"+ champ_musique[8] +"</location>\n"+
                               "\t\t\t<title>"+ champ_musique[0] +"</title>\n"+
                               "\t\t\t<creator>"+ champ_musique[1] +"</creator>\n"+
                               "\t\t\t<album>"+ champ_musique[2] +"</album>\n"+
                               "\t\t\t<duration>"+ str(champ_musique[3]) +"</duration>\n"+
                               "\t\t</track>\n")
    fichier.write("\t</trackList>\n</playlist>")
    fichier.close()