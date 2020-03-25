import slovo
import easydecks as ed

Deu = slovo.Word.constr("Deu", "de")
Eng = slovo.Word.constr("Eng", "en")
Proverbs = [
    ("Ende gut, Alles gut", "All's Well That Ends Well"),
    ("Es ist noch kein meister vom Himmel gefallen", "So far no master has fallen from the sky!"),
    ("Deutsch sprache schwere sprache", "German Langauge, Hard Language"),
    ("Viele Köche verderben den Brei", "Too many cooks spoil the broth"),
    ("Der tropfen der das Fass zum Uberlaufen bringt", "The drop the barrel overflows"),
    ("Überlaufen", "Overflow"),
    ("Auch ein blindes huhn findet mal ein korn", "But even a blind chicken finds a corn once"),
    ("Es schüttet wie aus Eimern", "It poured out like cats and dogs"),
    ("Die Feder ist mächtiger als das Schwert", "The pen is mightier then the sword"),
    ("Lachen ist die beste Medizin", "The laughter is the best medicine"),
    ("Das ist Schnee von gestern", "Its a show from yesterday"),
    ('Er ist bekannt wie ein "bunter Hund"', 'He is famously as "colored dog"'),
    ('Halt die Ohren steif!', 'Keep a ears up!'),
    ('Aus den Augen, aus dem Sinn', 'Out of eyes, out of head!'),
]

deck = ed.Deck("Duo.Deu.Skills_Idioms")

for pair in Proverbs:
    deck.card('DEFAULT', Eng(pair[1]), Deu(pair[0]))

deck.save(__file__.replace(".py", ""))
