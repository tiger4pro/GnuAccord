#(set-input-mode (string-append "utf-" (string-length #"é")))
\version "2.20.0"

\header {
  title = "Accord de d8 majeur"
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
      <d8 cis8 e8>4
    }
    \new Staff {
      \clef "bass"
      \key d \major
      \autoBeamOn
      \hideNotes
      <d8 cis8 e8>4
    }
  >>
}
