#(set-input-mode (string-append "utf-" (string-length #"é")))
\version "2.20.0"

\header {
  title = "Accord de gis8 majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key gis \major
      \autoBeamOn
      <gis8 cis8 e8>4
    }
    \new Staff {
      \clef "bass"
      \key gis \major
      \autoBeamOn
      \hideNotes
      <gis8 cis8 e8>4
    }
  >>
}
