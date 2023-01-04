\version "2.20.0"

\header {
  title = "Accord de mi majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new Staff <<
    \clef "treble"
    \time 4/4
    \set Score.tempoHideNote = ##t
    \tempo 4=60
    \key e \major
    \autoBeamOn
    e4 eis e4
  >>
}
