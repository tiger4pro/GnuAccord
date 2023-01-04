#(set-input-mode (string-append "utf-" (string-length #"é")))
\version "2.20.0"

\header {
  title = "Accord de b2 majeur"
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
      <b2 cis2 e2>4
    }
    \new Staff {
      \clef "bass"
      \key b \major
      \autoBeamOn
      \hideNotes
      <b2 cis2 e2>4
    }
  >>
}
