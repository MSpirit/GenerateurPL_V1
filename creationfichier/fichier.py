def writeM3U(args, musiquePL):
    playlistFileName = args.nomFichierPlaylist +"."+ args.formatPlaylist
    playlistFile = open(playlistFileName, 'w')
    for champ_musique in musiquePL:
        playlistFile.write(champ_musique[4] + "\n")
    playlistFile.close()