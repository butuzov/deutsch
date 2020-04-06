from dataclasses import dataclass
from typing import Optional, List
from os.path import (basename, dirname)

import slovo
import easydecks as ed

# Datastuctures


class Deu(slovo.Word):
    lang = "de"


class Eng(slovo.Word):
    lang = "en"


@dataclass
class Card:
    deu: str
    eng: str
    img: Optional[str] = None
    snd: Optional[str] = None


Words: List[Card] = [
    Card("'Die Katze", "cat", "images/cat.svg"),
    Card("Der Hund", "dog", "images/dog.svg"),
    Card("Die Maus", "mouse", "images/mouse.svg"),
    Card("Das Apfel", "apple", "images/apple.svg"),
    Card("Das Aubergine", "aubergine", "images/aubergine.svg"),
    Card("Die Banane", "banan", "images/banana.svg"),
    Card("Der Bär", "bear", "images/bear.svg"),
    Card("Der Vogel", "bird", "images/bird.svg"),
    Card("Der Schmetterling", "butterfly", "images/butterfly.svg"),
    Card("Die Karotte", "carrot", "images/carrot.svg"),
    Card("Die Kirsche", "cherry", "images/cherry.svg"),
    Card("Die Schokolade", "chocolate", "images/chocolate.svg"),
    Card("Die Kuh", "cow", "images/cow.svg"),
    Card("Die Libelle", "dragonfly", "images/dragonfly.svg"),
    Card("Die Fliege", "fly", "images/fly.svg"),
    Card("Die Biene", "bee", "images/bee.svg"),
    Card("Das Bier", "beer", "images/beer.svg"),
    Card("Der Käfer", "beetle", "images/beetle.svg"),
    Card("Das Obst", "fruits", "images/fruits.svg"),
    Card("Der Honig", "honey", "images/honey.svg"),
    Card("Das Insekt", "insect", "images/insect.svg"),
    Card("Das Fleisch", "meat", "images/meat.svg"),
    Card("Die Melone", "melon", "images/melon.svg"),
    Card("Die Wassermelone", "watermelon", "images/watermelon.svg"),
    Card("Das Öl", "oil", "images/oil.svg"),
    Card("Der Käse", "cheese", "images/cheese.svg"),
    Card("Die Suppe", "soup", "images/soup.svg"),
    Card("Der Orangesaft", "orange juice", "images/orange-juice.svg"),
    Card("Die Orange", "orange", "images/orange.svg"),
    Card("Die Papaya", "papaya", "images/papaya.svg"),
    Card("Die Nudeln", "pasta", "images/pasta.svg"),
    Card("Das Schwein", "pig", "images/pig.svg"),
    Card("Der Fisch", "fish", "images/fish.svg"),
    Card("Das Pferd", "horse", "images/horse.svg"),
    Card("Der Kaffee", "coffee", "images/coffee.svg"),
    Card("Das Milch", "milk", "images/milk.svg"),
    Card("Das Ai", "egg", "images/egg.svg"),
    Card("Die Erdbeere", "strawberry", "images/strawberry.svg"),
    Card("Die Kartoffel", "potato", "images/potatoes.svg"),
    Card("Der Reis", "rice", "images/rice.svg"),
    Card("Das Salz und der Pfeffer", "salt and papper", "images/salt-n-pepper.svg"),
    Card("Die Spinne", "spider", "images/spider.svg"),
    Card("Der Tintenfisch", "squid", "images/squid.svg"),
    Card("Das Gemüse", "vegetables", "images/vegetables.svg"),
    Card("Der Wine", "wine", "images/wine.svg"),
    Card("Das Haustier", "pet", "images/pet.svg"),
    Card("Die Eiscreme", "ice cream", "images/ice.svg"),
]

if __name__ == "__main__":
    from random import shuffle

    shuffle(Words)

    deck = ed.Deck("Duo.Deu.Food&Animales")
    for c in Words:

        deck.default(
            Eng(c.eng).image(c.img).sound(c.snd),
            Deu(c.deu).image(c.img).sound(c.snd),
        )

    deck.save(__file__.replace(".py", ""))
