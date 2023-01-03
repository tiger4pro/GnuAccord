import mido
import os
import subprocess
import glob
import svgwrite

def generer_accord_lilypond(note, accord, duree):
    # On calcule les notes de l'accord en utilisant la formule de l'accord
    notes = []
    if accord == "majeur":
        notes.append(note)
        notes.append(note + 4)
        notes.append(note + 7)
    elif accord == "mineur":
        notes.append(note)
        notes.append(note + 3)
        notes.append(note + 7)
    elif accord == "majeur_septieme_mineure":
        notes.append(note)
        notes.append(note + 4)
        notes.append(note + 7)
        notes.append(note + 10)
    elif accord == "majeur_septieme_majeure":
        notes.append(note)
        notes.append(note + 4)
        notes.append(note + 7)
        notes.append(note + 11)
    elif accord == "majeur_sixte_majeure":
        notes.append(note)
        notes.append(note + 4)
        notes.append(note + 7)
        notes.append(note + 9)
    elif accord == "majeur_neuvieme_majeure":
        notes.append(note)
        notes.append(note + 4)
        notes.append(note + 7)
        notes.append(note + 14)
    elif accord == "majeur_septieme_mineure_neuvieme_majeure":
        notes.append(note)
        notes.append(note + 4)
        notes.append(note + 7)
        notes.append(note + 10)
        notes.append(note + 14)
    elif accord == "diminue":
        notes.append(note)
        notes.append(note + 3)
        notes.append(note + 6)
    elif accord == "diminue_septieme_diminuee":
        notes.append(note)
        notes.append(note + 3)
        notes.append(note + 6)
        notes.append(note + 9)
    elif accord == "augmente":
        notes.append(note)
        notes.append(note + 4)
        notes.append(note + 8)
    elif accord == "sus2":
        notes.append(note)
        notes.append(note + 2)
        notes.append(note + 7)
    elif accord == "sus4":
        notes.append(note)
        notes.append(note + 5)
        notes.append(note + 7)
        # On convertit la note en chaîne de caractères pour LilyPond
        note_lilypond = convertir_note_lilypond(n)
        notes_lilypond.append(note_lilypond)
    
    # On crée la chaîne de caractères pour l'accord dans LilyPond
    accord_lilypond = " ".join(notes_lilypond) + " " + duree
    
    return accord_lilypond

def ecrire_accord_lilypond(note, accord, duree, nom_fichier):
    # On génère l'accord dans le langage LilyPond
    accord_lilypond = generer_accord_lilypond(note, accord, duree)
    
    # On ouvre le fichier en écriture
    with open(nom_fichier, "w") as f:
        # On écrit l'entête du fichier LilyPond
        f.write("\\version \"2.18.2\"\n")
        f.write("\\header {\n")
        f.write("  title = \"" + nom_fichier + "\"\n")
        f.write("}\n")
        f.write("\\score {\n")
        f.write("  \\new PianoStaff {\n")
        f.write("    \\set PianoStaff.instrumentName = #\"Piano\"\n")
        f.write("    \\set PianoStaff.shortInstrumentName = #\"Pno.\"\n")
        f.write("    \\clef \"treble\"\n")
        f.write("    \\time 4/4\n")
        f.write("    \\new Staff {\n")
        f.write("      \\relative c' {\n")
        
        # On écrit l'accord dans le fichier
        f.write("        " + accord_lilypond + "\n")
        
        # On termine le fichier LilyPond
        f.write("      }\n")
        f.write("    }\n")
        f.write("  }\n")
        f.write("}\n")

def generer_accords_lilypond(duree):
    # On parcourt toutes les notes du piano
    for note in range(88):
        # On génère les accords majeurs
        nom_fichier = str(note // 12) + "_" + convertir_note_nom(note % 12) + "_majeur_" + duree + ".ly"
        ecrire_accord_lilypond(note, "majeur", duree, nom_fichier)
        
        # On génère les accords mineurs
        nom_fichier = str(note // 12) + "_" + convertir_note_nom(note % 12) + "_mineur_" + duree + ".ly"
        ecrire_accord_lilypond(note, "mineur", duree, nom_fichier)
        
        # On continue avec les autres types d'accords...

def convertir_lilypond_midi_pdf(nom_fichier):
    # On utilise la commande lilypond pour convertir le fichier en midi et pdf
    subprocess.run(["lilypond", "-dmidi-extension=midi", "-dbackend=svg", "-dno-print-pages", nom_fichier])
    
    # On renomme les fichiers générés avec l'extension adéquate
    nom_fichier_sans_extension = nom_fichier[:-3]
    os.rename(nom_fichier_sans_extension + ".midi", nom_fichier_sans_extension + ".mid")
    os.rename(nom_fichier_sans_extension + ".pdf", nom_fichier_sans_extension + ".pdf")

def convertir_midi_svg(nom_fichier):
    # On ouvre le fichier midi
    midi_file = mido.MidiFile(nom_fichier)
    
    # On crée le dessin SVG
    dwg = svgwrite.Drawing(nom_fichier[:-4] + ".svg", profile='tiny')
    
    # On parcourt les messages du fichier midi
    for msg in midi_file:
        # Si c'est un message de note on, on dessine un point sur la note correspondante
        if msg.type == "note_on":
            note = msg.note
            x = (note % 12) * 50 + 25
            y = (note // 12) * 50 + 25
            dwg.add(dwg.circle((x, y), 5, fill='red'))
    
    # On enregistre le dessin SVG
    dwg.save()

def generer_accords():
    # On génère les accords lilpond
    generer_accords_lilypond("quadruple_croche")
    generer_accords_lilypond("double_croche")
    generer_accords_lilypond("croche")
    generer_accords_lilypond("noir")
    generer_accords_lilypond("blanche")
    generer_accords_lilypond("ronde")
    
    # On récupère la liste de tous les fichiers lilpond
    fichiers_lilypond = glob.glob("*.ly")
    
    # On convertit chaque fichier lilpond en midi et pdf
    for fichier in fichiers_lilypond:
        convertir_lilypond_midi_pdf(fichier)
    
    # On récupère la liste de tous les fichiers midi
    fichiers_midi = glob.glob("*.mid")
    
    # On convertit chaque fichier midi en svg
    for fichier in fichiers_midi:
        convertir_midi_svg(fichier)

# On appelle la fonction pour lancer le programme
generer_accords()

