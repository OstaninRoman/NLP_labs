import nltk
import pymorphy3
from nltk.tokenize import sent_tokenize, word_tokenize

def agree(first, second):
    allowed_pos = {"NOUN", "ADJF"}
    
    if first.tag.POS not in allowed_pos or second.tag.POS not in allowed_pos:
        return False
    if first.tag.number is None or first.tag.number != second.tag.number:
        return False
    if first.tag.case is None or first.tag.case != second.tag.case:
        return False
    if first.tag.number == "plur":
        return True

    return first.tag.gender is not None and first.tag.gender == second.tag.gender

with open("..\\text\\text.txt", "r", encoding="utf-8") as file:
    text = file.read()

nltk.download("punkt_tab", quiet=True)

sentences = sent_tokenize(text, language="russian")

morph = pymorphy3.MorphAnalyzer()

for sentence in sentences:
    tokens = word_tokenize(
        sentence,
        language="russian",
        preserve_line=True,
    )

    for left, right in zip(tokens, tokens[1:]):
        first = morph.parse(left.lower())[0]
        second = morph.parse(right.lower())[0]

        if agree(first, second):
            print(first.normal_form, second.normal_form)