#(set-input-mode (string-append "utf-" (string-length #"é")))
\version "2.20.0"

\header {
  title = "Accord de cis8 majeur"
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
      <cis8 cis8 e8>4
    }
    \new Staff {
      \clef "bass"
      \key cis \major
      \autoBeamOn
      \hideNotes
      <cis8 cis8 e8>4
    }
  >>
}
