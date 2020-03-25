# This file is crating a verb card with easydecks module for duolingo deutsch course verbs from
# level 1.
#
from enum import Enum, auto
import re
import easydecks as ed
from random import choice, shuffle

# actual functionality


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
            self.Sie: ['Sie']
        }[self])


def present_indicative(verb, extra={}):
    """ Form a forms of the present indicative tense """
    data = {}
    endings = {
        Pronoun.Ich: 'e',
        Pronoun.Du: 'st',
        Pronoun.Er_Sie_Es: 't',
        Pronoun.Wir: 'en',
        Pronoun.Ihr: 't',
        Pronoun.Sie: 'en',
    }

    for pron, ends in endings.items():
        if pron in extra:
            data[pron] = '<span class="irregular">%s</span>' % extra[pron]
        else:
            data[pron] = '<span class="base">%s</span><span class="changed">%s</span>' % (
                verb[:-2], ends)

    return data


def to_struct(translation: str, addition: str, is_regular: bool, extra={}):
    return {
        'translation': translation,
        'addition': addition,
        'regular': is_regular,
        'extra': extra,
    }


# Verbs in Level 1 Duolingo Deutsch

Varbs = {
    'kommen': to_struct('to come', 'aus Deutschland', True),
    'trinken': to_struct('to drink', 'wasser', True),
    'verstehen': to_struct('to understand', 'es nicht', True),
    'sprechen': to_struct('to speak', 'Deutsch', True),
    'lesen': to_struct(
        'to read', 'Zeitung', False, {
            Pronoun.Du: 'liest',
            Pronoun.Er_Sie_Es: 'liest',
        }),
    'essen': to_struct('to eat', 'Brot', False, {
        Pronoun.Du: 'isst',
        Pronoun.Er_Sie_Es: 'isst',
    }),
    'haben': to_struct('to have', 'Brot', False, {
        Pronoun.Du: 'hast',
        Pronoun.Er_Sie_Es: 'hat',
    }),
}

if __name__ == "__main__":

    data = []
    for verb, item in Varbs.items():
        for pron, form in present_indicative(verb).items():
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

    shuffle(data)

    deck = ed.Deck("Duo.Deu.Basics_Verbs")
    [deck.card('verbs', *item) for item in data]
    deck.save(__file__.replace(".py", ""))
