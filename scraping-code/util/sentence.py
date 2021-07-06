# Taken from https://stackoverflow.com/a/31505798
# License is CC By SA 4.0

from nltk import tokenize

def split_into_sentences(text):
    return tokenize.sent_tokenize(text)
