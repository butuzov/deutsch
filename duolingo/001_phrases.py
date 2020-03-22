from dataclasses import dataclass
from typing import Optional, List
from os.path import (basename, dirname)

import easydecks as ed


@dataclass
class Card:
    deu: str
    eng: str


Phrases: List[Card] = [
    Card("Guten Tag", "Good afternoon"),
    Card("Guten Abent", "Good evening"),
    Card("Guten Morgen", "Good morning"),
    Card("Gute Nacht", "Good night"),
    Card("Bitte", "Sorry? Please? What?"),
    Card("Ja", "Yes"),
    Card("Nein", "No"),
    Card("Später", "Later"),
    Card("Sprechen", "Speak"),
    Card("Schnee", "Show"),
    Card("Tcshüss", "Bye"),
    Card("Wie geht's?", "How is it going?"),
    Card("Genau", "Exactly"),
    Card("Leider", "Unfortunatly"),
    Card("Bis morgen", "Se you tomorrow"),
    Card("Bis später", "See you later"),
    Card("Bis bald", "See you soon"),
    Card("Danke", "Thanks"),
    Card("Auf Wiedersehen", "Goodbye"),
    Card("Mir Geht's gut", "I am doing well/ok!"),
    Card("Keine Ahnung", "No Idea"),
    Card("In Ordnung", "In Order"),
    Card("Entschuldigung", "Sorry!"),
    Card("Es tut mir leid", "I am sorry!"),
]

if __name__ == "__main__":
    from random import shuffle

    shuffle(Phrases)

    deck = ed.Deck("Duo.Deu.Basics_Phrases")
    for c in Phrases:
        deck.default(c.eng, c.deu)

    deck.save(__file__.replace(".py", ""))
