#from database.recuperationdonnees import musiquePL


def writeM3U(args, musiquePL):
    fichier = args.nomFichierPlaylist +"."+ args.formatPlaylist
    fichier = open(fichier, 'w')
    for champ_musique in musiquePL:
        fichier.write(champ_musique[4] + "\n")
    fichier.close()
    
def writeXSPF(args, musiquePL):
    fichierxspf1 = (args.nomFichierPlaylist + "." + args.formatPlaylist)
    fichierxspf = open(fichierxspf1, 'w')
    fichierxspf.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+
                       "<playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\">\n"+
                       "\t<title>"+ fichierxspf1 +"</title>\n"+
                       "\t<trackList>\n")
    #Parcours le résultat pour chaque ligne
    for champ_musique in musiquePL:
            fichierxspf.write("\t\t<track>\n\t\t\t<location>file://"+ champ_musique[4] +"</location>\n"+
                               "\t\t\t<title>"+ champ_musique[0] +"</title>\n"+
                               "\t\t\t<creator>"+ champ_musique[1] +"</creator>\n"+
                               "\t\t\t<album>"+ champ_musique[2] +"</album>\n"+
                               "\t\t\t<duration>"+ str(champ_musique[3]) +"</duration>\n"+
                               "\t\t</track>\n")
    fichierxspf.write("\t</trackList>\n</playlist>")
    fichierxspf.close()
    
def writePLS(args, musiquePL):
    i=1
    fichierPLS1 = (args.nomFichierPlaylist + "." + args.formatPlaylist)
    fichierpls = open(fichierPLS1, 'w')
    fichierpls.write("[playlist]\n\n")
    for champ_musique in musiquePL:
        fichierpls.write("File"+ str(i) +"="+ champ_musique[4] +"\n")
        fichierpls.write("creator"+ str(i) +"="+ champ_musique[1] +"\n")
        fichierpls.write("Title"+ str(i) +"="+ champ_musique[0] + "\n")
        fichierpls.write("Length"+ str(i) +"="+ str(champ_musique[3]) + "\n\n")
        i+=1
    fichierpls.write("NumberOfEntries="+ str(len(musiquePL)) +"\n")
    fichierpls.close()