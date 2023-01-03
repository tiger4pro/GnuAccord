# Noms des notes de la musique en fran�ais
notes = ['do', 'do#', 'r�', 'r�#', 'mi', 'fa', 'fa#', 'sol', 'sol#', 'la', 'la#', 'si']

# Dur�e de la quadruple croche
dur = "\\quadruplecroche"

# Boucle sur tous les octaves (de 1 � 10)
for octave in range(1, 11):
  # Boucle sur toutes les notes de la gamme
  for note in notes:
    # Cr�e le nom du fichier
    filename = "{}_{}_majeur_{}.ly".format(octave, note, dur)
    
    # Ouvre le fichier en mode �criture
    with open(filename, 'w') as f:
      # �crit le contenu du fichier
      f.write("\\version \"2.20.0\"\n")
      f.write("\n")
      f.write("% {} majeur\n".format(note))
      f.write("{\n")
      f.write("  \\time 4/4\n")
      f.write("  \\tempo 4=100\n")
      f.write("  \\key {} \\major\n".format(note))
      f.write("  \\autoBeamOff\n")
      f.write("  s1\n")
      f.write("  {}{}1{} {}{}3{} | {}{}5{} {}{}6{} | {}{}8{} {}{}10{} | {}{}12{} {}{}13{}\n".format(note, octave, dur, note, octave+1, dur, note, octave+2, dur, note, octave+3, dur, note, octave+4, dur, note, octave+5, dur))
      f.write("}\n")
      
print("Fichiers cr��s avec succ�s!")
