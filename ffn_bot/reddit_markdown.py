import re

from bs4.dammit import EntitySubstitution

linebreak = "---"


def bold(string):
    return '**' + string + '**'


def italics(string):
    return '*' + string + '*'


def superscript(string):
    if ')' not in string:
        return '^(' + string + ')'
    return '^' + re.sub(' +', ' ^', string)


def remove_superscript(string):
    return re.sub('\^', '', string)


def quote(string):
    return "> " + string.replace("\n", "\n> ")


def encode_url(string):
    encoder = EntitySubstitution()
    return encoder.substitute_html(string)


def escape(string):
    return re.sub(r"([\\\[\]\-(){}+_!.#`^>*])", r"\\\1", string)


def link(text, link):
    return "[" + text + "](" + link + ")"
