#(set-input-mode (string-append "utf-" (string-length #"é")))
\version "2.20.0"

\header {
  title = "Accord de a6 majeur"
  composer = "Ce fichier a été généré par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key a \major
      \autoBeamOn
      <a6 cis6 e6>4
    }
    \new Staff {
      \clef "bass"
      \key a \major
      \autoBeamOn
      \hideNotes
      <a6 cis6 e6>4
    }
  >>
}
