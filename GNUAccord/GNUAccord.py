# Création du nom du fichier
filename = "1_do_majeur_64_double_portee.ly"

# Écriture du contenu du fichier
with open(filename, "w") as f:
    f.write(f"""\
\\version "2.20.0"

\\header {{
  title = "Accord de do majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}}

\\score {{
  \\new PianoStaff <<
    \\new Staff {{
      \\clef "treble"
      \\time 4/4
      \\set Score.tempoHideNote = ##t
      \\tempo 4=60
      \\key c \\major
      \\autoBeamOn
      <c e g>4
    }}
    \\new Staff {{
      \\clef "bass"
      \\key c \\major
      \\autoBeamOn
      \\hideNotes
      <c e g>4
    }}
  >>
}}
"""
    )