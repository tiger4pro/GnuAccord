\version "2.20.0"

\header {
  title = "Accord de gis majeur"
  composer = "Ce fichier a �t� g�n�r� par GNU Accord"
}

\score {
  \new PianoStaff <<
    \new Staff {
      \clef "treble"
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo 4=60
      \key gis \major
      \autoBeamOn
      <gis cis e>4
    }
    \new Staff {
      \clef "bass"
      \key gis \major
      \autoBeamOn
      \hideNotes
      <gis cis e>4
    }
  >>
}
