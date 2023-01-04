\version "2.20.0"

\header {
  title = "Accord de dis majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key dis \major
      \autoBeamOn
      <dis cis e>4
    }
    \new Staff {
      \clef "bass"
      \key dis \major
      \autoBeamOn
      \hideNotes
      <dis cis e>4
    }
  >>
}
