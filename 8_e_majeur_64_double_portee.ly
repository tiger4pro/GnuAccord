\version "2.20.0"

\header {
  title = "Accord de e majeur"
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
      <e cis e>4
    }
    \new Staff {
      \clef "bass"
      \key e \major
      \autoBeamOn
      \hideNotes
      <e cis e>4
    }
  >>
}
