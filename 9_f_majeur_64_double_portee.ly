\version "2.20.0"

\header {
  title = "Accord de f majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key f \major
      \autoBeamOn
      <f cis e>4
    }
    \new Staff {
      \clef "bass"
      \key f \major
      \autoBeamOn
      \hideNotes
      <f cis e>4
    }
  >>
}
