\version "2.20.0"

\header {
  title = "Accord de la majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new Staff <<
    \clef "treble"
    \time 4/4
    \set Score.tempoHideNote = ##t
    \tempo 4=60
    \key a \major
    \autoBeamOn
    a4 ais e4
  >>
}
