#(set-input-mode (string-append "utf-" (string-length #"é")))
\version "2.20.0"

\header {
  title = "Accord de cis2 majeur"
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
      <cis2 cis2 e2>4
    }
    \new Staff {
      \clef "bass"
      \key cis \major
      \autoBeamOn
      \hideNotes
      <cis2 cis2 e2>4
    }
  >>
}
