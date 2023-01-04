#(set-input-mode (string-append "utf-" (string-length #"é")))
\version "2.20.0"

\header {
  title = "Accord de d4 majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key d \major
      \autoBeamOn
      <d4 cis4 e4>4
    }
    \new Staff {
      \clef "bass"
      \key d \major
      \autoBeamOn
      \hideNotes
      <d4 cis4 e4>4
    }
  >>
}
