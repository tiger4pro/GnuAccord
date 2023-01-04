# Liste des notes du clavier de 88 touches
notes = [
    "a",
    "ais",
    "b",
    "c",
    "cis",
    "d",
    "dis",
    "e",
    "f",
    "fis",
    "g",
    "gis",
]

# Création de la liste des noms de fichiers
filenames = [f"1_{note}_majeur_64_double_portee.ly" for note in notes]

# Génération des fichiers
for filename, note in zip(filenames, notes):
    with open(filename, "w") as f:
        f.write(f"""\
\\version "2.20.0"

\\header {{
  title = "Accord de {note} majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}}

\\score {{
  \\new PianoStaff <<
    \\new Staff {{
      \\clef "treble"
      \\time 4/4
      \\set Score.tempoHideNote = ##t
      \\tempo 4=60
      \\key {note} \\major
      \\autoBeamOn
      <{note} cis e>4
    }}
    \\new Staff {{
      \\clef "bass"
      \\key {note} \\major
      \\autoBeamOn
      \\hideNotes
      <{note} cis e>4
    }}
  >>
}}
"""
        )