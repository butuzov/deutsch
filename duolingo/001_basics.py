from dataclasses import dataclass
from typing import Optional, List

import slovo
import easydecks as ed


class Deu(slovo.Word):
    lang = "de"


class Eng(slovo.Word):
    lang = "en"


@dataclass
class Card:
    deu: Deu
    eng: Eng
    img: Optional[str] = None
    snd: Optional[str] = None


Words: List[Card] = [

    # Man, Woman, Boy, Girl, Child
    Card(Deu("eine Frau"), Eng("a Woman"), "images/woman.jpg"),
    Card(Deu("die Frau"), Eng("the Woman"), "images/woman.jpg"),
    Card(Deu("die Frauen"), Eng("then Women"), "images/women.jpg"),
    # man
    Card(Deu("ein Mann"), Eng("a Man"), "images/man.jpg"),
    Card(Deu("der Mann"), Eng("the Man"), "images/man.jpg"),
    Card(Deu("die Männer"), Eng("the Men"), "images/men.jpg"),
    # girl
    Card(Deu("ein Mädchen"), Eng("a Girl"), "images/girl.jpg"),
    Card(Deu("das Mädchen"), Eng("the Girl"), "images/girl.jpg"),
    Card(Deu("die Mädchen"), Eng("the Girls"), "images/girls.jpg"),
    # child
    Card(Deu("ein Kind"), Eng("a child"), "images/child.jpg"),
    Card(Deu("das Kind"), Eng("the child"), "images/child.jpg"),
    Card(Deu("die Kinder"), Eng("the children"), "images/children.jpg"),
    # boy
    Card(Deu("ein Junge"), Eng("a Boy"), "images/boy.jpg"),
    Card(Deu("der Junge"), Eng("the Boy"), "images/boy.jpg"),
    Card(Deu("die Jungen"), Eng("the Boys"), "images/boys.jpg"),

    # I, you, she/he/it, we, you (plural), they
    # I am
    Card(Deu("Ich"), Eng("I")),
    Card(Deu("Bin ich schön?"), Eng("Am I Beautiful?"), "images/bin_ich_schon.jpg"),
    Card(Deu("Ich bin"), Eng("I am"), "images/ich_bin.jpg"),
    Card(Deu("Ich bin ein Hamburger"), Eng("I am a Hamberger"), "images/ich_bin.jpg"),

    # du and forms
    Card(Deu("Krank"), Eng("Ill")),
    Card(Deu("Du bist krank"), Eng("You are ill"), "images/you_are_ill.jpg"),
    Card(Deu("Bist du krank?"), Eng("Are you sick?"), "images/you_are_ill.jpg"),

    # we
    Card(Deu("Wir"), Eng("We")),
    Card(Deu("Wir sind"), Eng("We are"), "images/wir-sind.jpg"),

    # she/he/it
    Card(Deu("Er"), Eng("He")),
    Card(Deu("Er ist"), Eng("He is")),
    Card(Deu("Es"), Eng("It")),
    Card(Deu("Es ist"), Eng("It is")),
    Card(Deu("Sie"), Eng("She")),
    Card(Deu("Sie ist"), Eng("She is")),

    # you are (plural)
    Card(Deu("Ihr seid"), Eng("You are")),

    # they
    Card(Deu("Sie sind"), Eng("They are")),
    Card(Deu("Schön"), Eng("Beautiful")),
]

if __name__ == "__main__":
    from random import shuffle

    shuffle(Words)

    deck = ed.Deck("Duo.Deu.Basics_I&II")
    for c in Words:

        deck.default(
            c.eng.image(c.img).sound(c.snd),
            c.deu.image(c.img).sound(c.snd),
        )

    deck.save(__file__.replace(".py", ""))
