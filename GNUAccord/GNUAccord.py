# Noms des notes de la musique en français
notes = ['do', 'do#', 'réb', 'ré', 'ré#', 'mib', 'mi', 'fa', 'fa#', 'solb', 'sol', 'sol#', 'labb', 'la', 'la#', 'sib', 'si']

# Durée de la quadruple croche
dur = "quadruplecroche"

def generate_lilypond_content(note, octave, dur):
  """
  Génère le contenu du fichier Lilypond pour un accord majeur.
  
  Args:
    note (str): le nom de la note
    octave (int): le numéro de l'octave
    dur (str): la durée de l'accord
    
  Returns:
    str: le contenu du fichier Lilypond
  """
  return f"""\\version "2.20.0"

% {note} majeur
{{
  \\time 4/4
  \\tempo 4=100
  \\key {note} \\major
  \\autoBeamOff
  s1
  {note}{octave}1\\{dur} {note}{octave+1}\\{dur} | {note}{octave+2}\\{dur} {note}{octave+3}\\{dur} | {note}{octave+4}\\{dur} {note}{octave+5}\\{dur}
}}"""

# Boucle sur tous les octaves (de 1 à 10)
for octave in range(1, 11):
  # Boucle sur toutes les notes de la gamme
  for i, note in enumerate(notes):
    # Remplace les dièses par le caractère "d"
    note_for_filename = note.replace("#", "d")
    
    # Crée le nom du fichier
    filename = f"{octave}_{note_for_filename}_majeur_{dur}.ly"
    
    # Ouvre le fichier en mode écriture
    with open(filename, 'w') as f:
      # Écrit le contenu du fichier
      f.write(generate_lilypond_content(note, octave, dur))
      
print("Fichiers créés avec succès!")
