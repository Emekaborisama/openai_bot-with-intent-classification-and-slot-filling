import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp(text)

def entity_extraction(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "DATE":
            print("Date:", ent.text)
        elif ent.label_ == "CARDINAL":
            print("Number:", ent.text)
        elif ent.label_ == "ORDINAL":
            print("Ordinal Number:", ent.text)
        elif ent.label_ == "MONEY":
            print("Currency:", ent.text)
