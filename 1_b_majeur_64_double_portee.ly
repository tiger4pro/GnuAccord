\version "2.20.0"

\header {
  title = "Accord de b majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key b \major
      \autoBeamOn
      <b cis e>4
    }
    \new Staff {
      \clef "bass"
      \key b \major
      \autoBeamOn
      \hideNotes
      <b cis e>4
    }
  >>
}
