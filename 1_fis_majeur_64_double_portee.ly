\version "2.20.0"

\header {
  title = "Accord de fis majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key fis \major
      \autoBeamOn
      <fis cis e>4
    }
    \new Staff {
      \clef "bass"
      \key fis \major
      \autoBeamOn
      \hideNotes
      <fis cis e>4
    }
  >>
}
