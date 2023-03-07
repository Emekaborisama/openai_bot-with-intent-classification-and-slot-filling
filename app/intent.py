
try:
    from app.load_model import initialize_model
except:
    from load_model import initialize_model
classifier  = initialize_model()


def intent_classifier(input_value):
    try:
        return classifier(input_value)
    except:
        pass