from dataclasses import dataclass
from typing import Optional, List
from os.path import (basename, dirname)

import easydecks as ed


@dataclass
class Card:
    deu: str
    eng: str


Phrases: List[Card] = [
    Card("Der Kaffeee geht auf mich", "The coffee is on me"),
    Card("Deine Augen sind wie Sterne", "Your eyes are like starts"),
    Card("Ich bin neu hier, und du?", "I am new here, and you?"),
    Card("Darf ich dich küssen?", "May I kiss you?"),
    Card("Ich finde dich nett", "I think you are nice"), # I am finding you neat
    Card("Ich finde dich suß", "I think you are cute"), # I am finding you neat
    Card("Willst du tanzen?", "Do you want to dance?"),
    Card("Du siehst aus wie meine nächste Freundin", "You looks like my next girlfriend"),
    Card("Darf ich dich zum Abndessen elnladen?", "May i invite you to dinner?"),
    Card("Ich möchte dich besser kennen larnen,", "I would like to get to know you better."),
    Card("Ich mag dich", "I like you"),
    Card("Kann ich dir ein Getränk bestellen", "Can i order you a drink?"),
    Card("Ich hab mich in dich verlibt", "I have fallen in love with you"),
    Card("Willist di mit mir ausgehen?", "Do you want to go out with me?"),
    Card("Do kannst gut tanzen!", "You can dance well"),
    Card("Do bist schlau", "You are smart"),
    Card("Do bist witzig", "You are funny"),
    Card("Kann ich dich unrufen?", "Can I call you?"),
]

if __name__ == "__main__":
    from random import shuffle

    shuffle(Phrases)

    deck = ed.Deck("Duo.Deu.Basics_Flirt")
    for c in Phrases:
        deck.default(c.eng, c.deu)

    deck.save(__file__.replace(".py", ""))
