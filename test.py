
import spacy

nlp = spacy.load('en_core_web_sm')  # spacy model load

text = """Hello guys, my name is hoseop
and I am ready!\n
I can do this all day"""

doc = nlp(text)
print(doc)
lemmatized_sentence = " ".join(token.lemma_ for token in doc)
print(lemmatized_sentence)
