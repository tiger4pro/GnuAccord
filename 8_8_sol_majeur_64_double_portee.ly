\version "2.20.0"

\header {
  title = "Accord de sol majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key g \major
      \autoBeamOn
      <g cis e>4
    }
    \new Staff {
      \clef "bass"
      \key g \major
      \autoBeamOn
      \hideNotes
      <g cis e>4
    }
  >>
}