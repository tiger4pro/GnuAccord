# Création du nom du fichier
filename = "1_do_majeur_64_double_portee.ly"

# Création du contenu du fichier
content = """\
\\version "2.20.0"

\\header {
  title = "Double portée de piano"
  composer = "Inconnu"
}

\\score {
  \\new PianoStaff <<
    \\new Staff {
      \\clef "treble"
      \\time 4/4
      \\set Score.tempoHideNote = ##t
      \\tempo 4=60
      \\key c \\major
      \\autoBeamOn
      <c e g>4
    }
    \\new Staff {
      \\clef "bass"
      \\key c \\major
      \\autoBeamOn
      <c e g>4
    }
  >>
}
"""

# Écriture du fichier
with open(filename, "w") as f:
    f.write(content)