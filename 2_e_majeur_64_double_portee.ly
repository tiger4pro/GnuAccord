#(set-input-mode (string-append "utf-" (string-length #"é")))
\version "2.20.0"

\header {
  title = "Accord de e2 majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key e \major
      \autoBeamOn
      <e2 cis2 e2>4
    }
    \new Staff {
      \clef "bass"
      \key e \major
      \autoBeamOn
      \hideNotes
      <e2 cis2 e2>4
    }
  >>
}
