from enum import Enum, auto
import re
import easydecks as ed
from random import choice, shuffle

# Verbs in Present Indicative form


def strip_tags(value):
    return re.sub(r'<[^>]*?>', '', value)


class Pronoun(Enum):
    Ich = auto()
    Du = auto()
    Er_Sie_Es = auto()
    Wir = auto()
    Ihr = auto()
    Sie = auto()

    def __str__(self):
        return choice({
            self.Ich: ['Ich'],
            self.Du: ['Du'],
            self.Er_Sie_Es: ['Er', 'Sie', 'Es'],
            self.Wir: ['Wir'],
            self.Ihr: ['Ihr'],
            self.Sie: ['Sie'],
        }[self])


def forms(verb, extra={}):
    data = {}
    endings = {
        Pronoun.Ich: 'e',
        Pronoun.Du: 'st',
        Pronoun.Er_Sie_Es: 't',
        Pronoun.Wir: 'en',
        Pronoun.Ihr: 't',
        Pronoun.Sie: 'en',
    }

    base = verb[:-2]
    for pron, ends in endings.items():
        if pron in extra:
            data[pron] = '<span class="irregular">%s</span>' % extra[pron]
        else:
            data[pron] = '<span class="base">%s</span><span class="changed">%s</span>' % (
                base, ends)

    return data


Irregular = {
    'essen': 'to eat', # du: isst, er/sie/es: isst
    'lesen': 'to read', # du 	liest, er/sie/es: liest
    'haben': 'to have', # du hast, es/sie/es: hat
}


def to_struct(translation: str, addition: str, is_regular: bool, extra={}):
    return {
        'translation': translation,
        'addition': addition,
        'regular': is_regular,
        'extra': extra,
    }


Varbs = {
    'essen': to_struct('to eat', 'Brot', False, {
        Pronoun.Du: 'isst',
        Pronoun.Er_Sie_Es: 'isst',
    }),
    'kommen': to_struct('to come', 'aus Deutschland', True),
    'trinken': to_struct('to drink', 'wasser', True),
    'verstehen': to_struct('to understand', 'es nicht', True),
    'lesen': to_struct(
        'to read', 'Zeitung', False, {
            Pronoun.Du: 'liest',
            Pronoun.Er_Sie_Es: 'liest',
        }),
}

data = []
for verb, item in Varbs.items():
    for pron, form in forms(verb).items():
        verb_form = form if pron not in item['extra'] else item['extra'][pron]
        sentence_q = "%s ... %s" % (pron, item['addition'])
        sentence_a = sentence_q.replace("...", '<strong>%s</strong>' % verb_form)

        if verb_form == form:
            rule_p = "<strong>verben</strong> - <strong>%s %s</strong>" % (
                pron, forms("verben")[pron])
            rule_r = "<strong>%s</strong> - <strong>%s %s</strong>" % (verb, pron, verb_form)
        else:
            rule_r = rule_p = "<em>ir</em> <strong class='irregular'>%s</strong>" % verb_form

        data.append((verb, item['translation'], sentence_q, sentence_a, rule_p, rule_r))

deck = ed.Deck("Duo.Deu.Basics_Verbs")

shuffle(data)
for item in data:
    deck.card('verbs', *item)

deck.save(__file__.replace(".py", ""))
