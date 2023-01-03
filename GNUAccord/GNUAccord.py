# Nombres d'octaves à générer
octave_min = 1
octave_max = 9

# Notes du clavier de 88 touches
notes = ["a", "ais", "b", "c", "cis", "d", "dis", "e", "f", "fis", "g", "gis"]

# Génération des fichiers
for octave in range(octave_min, octave_max + 1):
    for note in notes:
        filename = f"{octave}_{note}_majeur_64_double_portee.ly"
        with open(filename, "w") as f:
            f.write(f"""\
\\version "2.20.0"

\\header {{
  title = "Accord de {note}{octave} majeur"
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
      <{note}{octave} cis{octave} e{octave}>4
    }}
    \\new Staff {{
      \\clef "bass"
      \\key {note} \\major
      \\autoBeamOn
      \\hideNotes
      <{note}{octave} cis{octave} e{octave}>4
    }}
  >>
}}
"""
            )