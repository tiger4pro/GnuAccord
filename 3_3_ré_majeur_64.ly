\version "2.20.0"

\header {
  title = "Accord de ré majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new Staff <<
    \clef "treble"
    \time 4/4
    \set Score.tempoHideNote = ##t
    \tempo 4=60
    \key d \major
    \autoBeamOn
    <d cis e>4
  >>
}
