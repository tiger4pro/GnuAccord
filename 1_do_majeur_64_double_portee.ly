\version "2.20.0"

\header {
  title = "Accord de do majeur"
  composer = "Ce fichier a �t� g�n�r� par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key c \major
      \autoBeamOn
      <c e g>4
    }
    \new Staff {
      \clef "bass"
      \key c \major
      \autoBeamOn
      \hideNotes
      <c e g>4
    }
  >>
}
