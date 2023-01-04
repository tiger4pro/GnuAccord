# Dictionnaire des correspondances entre les noms de notes en anglais et en français
note_names = {
    "c": "do",
    "cis": "do dièse",
    "d": "ré",
    "dis": "ré dièse",
    "e": "mi",
    "f": "fa",
    "fis": "fa dièse",
    "g": "sol",
    "gis": "sol dièse",
    "a": "la",
    "ais": "la dièse",
    "b": "si",
}

# Itération sur les notes du clavier de 88 touches
for i, note in enumerate(
    ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b"]
):
    # Création du nom du fichier
    filename = f"{i + 1}_{i + 1}_{note_names[note]}_majeur_64_double_portee.ly"

    # Écriture du contenu du fichier
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""\
\\version "2.20.0"

\\header {{
  title = "Accord de {note_names[note]} majeur"
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

