#(set-input-mode (string-append "utf-" (string-length #"é")))
\version "2.20.0"

\header {
  title = "Accord de cis5 majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key cis \major
      \autoBeamOn
      <cis5 cis5 e5>4
    }
    \new Staff {
      \clef "bass"
      \key cis \major
      \autoBeamOn
      \hideNotes
      <cis5 cis5 e5>4
    }
  >>
}
