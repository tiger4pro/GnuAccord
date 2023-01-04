#(set-input-mode (string-append "utf-" (string-length #"é")))
\version "2.20.0"

\header {
  title = "Accord de e7 majeur"
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
      <e7 cis7 e7>4
    }
    \new Staff {
      \clef "bass"
      \key e \major
      \autoBeamOn
      \hideNotes
      <e7 cis7 e7>4
    }
  >>
}
