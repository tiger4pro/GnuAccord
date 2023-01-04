#(set-input-mode (string-append "utf-" (string-length #"é")))
\version "2.20.0"

\header {
  title = "Accord de fis3 majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key fis \major
      \autoBeamOn
      <fis3 cis3 e3>4
    }
    \new Staff {
      \clef "bass"
      \key fis \major
      \autoBeamOn
      \hideNotes
      <fis3 cis3 e3>4
    }
  >>
}
