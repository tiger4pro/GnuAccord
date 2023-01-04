#(set-input-mode (string-append "utf-" (string-length #"é")))
\version "2.20.0"

\header {
  title = "Accord de f7 majeur"
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
      <f7 cis7 e7>4
    }
    \new Staff {
      \clef "bass"
      \key f \major
      \autoBeamOn
      \hideNotes
      <f7 cis7 e7>4
    }
  >>
}
