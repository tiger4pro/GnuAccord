\version "2.20.0"

\header {
  title = "Accord de do majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new Staff <<
    \clef "treble"
    \time 4/4
    \set Score.tempoHideNote = ##t
    \tempo 4=60
    \key c \major
    \autoBeamOn
    c4 cis e4
  >>
}
